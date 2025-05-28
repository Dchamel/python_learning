# Chain of Thoughts (CoT)

from langchain_community.chat_models import GigaChat
from langchain import PromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough, RunnableLambda

from dotenv import load_dotenv
import os, requests, uuid

# Load environment variables from the .env file
load_dotenv()

# Access environment variables
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
AUTH = os.getenv('AUTH')


def get_access_token(auth: str) -> str:
    rq_uid = str(uuid.uuid4())

    payload = 'scope=GIGACHAT_API_PERS'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json',
        'RqUID': rq_uid,
        'Authorization': f'Basic {auth} '
    }
    url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"
    response = requests.request('POST', url, headers=headers, data=payload, verify='chain.pem')
    access_token = response.json().get('access_token')

    return access_token


ACCESS_TOKEN = get_access_token(AUTH)


def processing_by_gc():
    """Summarize book or other txt by Gigachat"""

    llm = GigaChat(
        credentials=AUTH,
        verify_ssl_certs=False,
        model="GigaChat:latest"
    )

    BASELINE_PROMPT = '''Ответь на вопрос. Избегай лишних деталей в своем ответе.
    
    Вопрос: {query}
    
    Ответ:'''

    baseline_response_prompt_template = PromptTemplate.from_template(BASELINE_PROMPT)
    baseline_response_chain = baseline_response_prompt_template | llm | StrOutputParser()

    VERIFICATION_QUESTION_PROMPT = '''Твоя задача: составить 2-4 вопроса, 
    ответы на которые позволят убедиться в корректности исходного ответа (Baseline Response)
    на вопрос (Actual Question).
    Начинай каждый вопрос с новой строки.
    ВАЖНО: не задавай вопросы, ответы на которые не помогут проверить или скорректировать Baseline Response.
    
    Actual Question: {query}
    Baseline Response: {base_response}
    
    Final Verification Questions:'''

    verification_question_generation_prompt_template = PromptTemplate.from_template(VERIFICATION_QUESTION_PROMPT)
    verification_question_generation_chain = verification_question_generation_prompt_template | llm | StrOutputParser()

    VERIFICATION_QUESTION_PROMPT = '''{input}'''

    base_verification_prompt_template = PromptTemplate.from_template(VERIFICATION_QUESTION_PROMPT)
    base_verification_chain = base_verification_prompt_template | llm | StrOutputParser()

    verification_chain = RunnablePassthrough.assign(
        split_questions=lambda x: x['verification_questions'].split('\\n'),
    ) | RunnablePassthrough.assign(
        answers=(lambda x: [{'input': q, 'chat_history': []} for q in x['split_questions']]) |
                base_verification_chain.map()
    ) | (lambda x: '\\n'.join(['Question: {} Answer: {} \\n'.format(question, answer) for question, answer in
                               zip(x['split_questions'], x['answers'])]))

    FINAL_ANSWER_PROMPT = """Тебе будут даны 'Original Query' и 'Baseline Answer', 
    проанализируй 'Verification Questions & Answers', чтобы скорректировать 
    'Baseline Answer' и дать максимально корректный ответ Final Refined Answer.
    ВАЖНО: не включай в ответ лишнюю информацию, не отвечающую на вопрос Original Query!
    
    Original Query: {query}
    Baseline Answer: {base_response}
    
    Verification Questions & Answers Pairs: 
    {verification_answers}
    Final Refined Answer:"""

    final_answer_pompt_template = PromptTemplate.from_template(FINAL_ANSWER_PROMPT)
    final_answer_chain = final_answer_pompt_template | llm | StrOutputParser()

    chain = RunnablePassthrough.assign(
        base_response=baseline_response_chain
    ) | RunnablePassthrough.assign(
        verification_questions=verification_question_generation_chain
    ) | RunnablePassthrough.assign(
        verification_answers=verification_chain
    ) | RunnablePassthrough.assign(
        final_answer=final_answer_chain
    )

    # user_input = input('Введите вопрос: ')
    # response = chain.invoke({'query': user_input})
    response = chain.invoke({'query': 'есть ли жизнь ?'})

    # print(response)

    dialog = f'''
#=========================   Вопрос  =========================
{response['query']}

#=========================   Базовый ответ  =========================
{response['base_response']}

#=========================   Проверочные вопросы  =========================
{response['verification_questions']}

#=========================   Проверочные ответы  =========================
{response['verification_answers']}

#=========================   Итоговый ответ  =========================
{response['final_answer']}
'''
    print(dialog)


def main():
    # process by GC
    processing_by_gc()


if __name__ == '__main__':
    main()
