from dotenv import load_dotenv
import os
from langchain_gigachat.chat_models import GigaChat
from langchain.schema import HumanMessage, SystemMessage
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables from the .env file
load_dotenv()

# Access environment variables
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
auth = os.getenv('AUTH')

prompt = ChatPromptTemplate.from_template('Скажи, каким будет лето в {страна} ?')

chat = GigaChat(
    credentials=auth,
    verify_ssl_certs=False
)

output_parser = StrOutputParser()

messages = [
    HumanMessage(content='Шалом')
]

chain = prompt | chat | output_parser
answer = chain.invoke({'страна': 'россия'})
print(answer)
