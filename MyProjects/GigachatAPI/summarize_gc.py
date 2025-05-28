import json
from pprint import pprint
from langchain.prompts import load_prompt
from langchain.chains.summarize import load_summarize_chain
from langchain_community.chat_models import GigaChat
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
# from gigachat import GigaChat
from dotenv import load_dotenv
import os, requests, uuid, base64

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

GIGA = GigaChat(
    credentials=AUTH,
    # model='GigaChat-Pro',
    verify_ssl_certs=False,
    # profanity_check=False,
    scope="GIGACHAT_API_PERS"
)


def put_file_to_gigachat(filename: str) -> str:
    """Put file to Gigachat for Processing, return file id"""

    file = GIGA.upload_file(open(filename, "rb"))
    return file.id_


def get_file_list(access_token: str) -> list[str]:
    """get my files from Gigachat"""

    url = "https://gigachat.devices.sberbank.ru/api/v1/files"
    payload = {}
    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.request("GET", url, headers=headers, data=payload, verify='chain.pem')
    answer = response.json()
    for_del = answer.get('data')
    file_list_id = [item['id'] for item in for_del]

    return file_list_id


def del_file_by_id(access_token: str, id: str) -> bool:
    """Delete file by ID from the Gigachat storage"""

    url = f"https://gigachat.devices.sberbank.ru/api/v1/files/{id}/delete"
    payload = {}
    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.request("POST", url, headers=headers, data=payload, verify='chain.pem')

    return response.json().get('deleted')


def processing_by_gc(file_id: str):
    """Summarize book or other txt by Gigachat"""

    result = GIGA.chat(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "Напиши краткое содержание книги объёмом в 1000 символов",
                    "attachments": [file_id],
                }
            ],
            "temperature": 0.1
        }
    )

    print(result.choices[0].message.content)


def main():
    # load file to GC
    file_id_4_processing = put_file_to_gigachat('input/Толстой Лев. Война и мир. Книга 1 - royallib.ru.txt')

    # process txt by GC
    processing_by_gc(file_id_4_processing)

    # get all files from GC
    all_gc_files = get_file_list(ACCESS_TOKEN)
    # print(all_gc_files)

    # del all files from GC
    for file in all_gc_files:
        del_file_by_id(ACCESS_TOKEN, file)


if __name__ == '__main__':
    main()

# loader = TextLoader(r'input/Толстой Лев. Война и мир. Книга 1 - royallib.ru.txt', encoding='utf8')
# documents = loader.load()
#
# text_splitter = RecursiveCharacterTextSplitter(
#     chunk_size=7000,
#     chunk_overlap=0,
#     length_function=len,
#     is_separator_regex=False,
# )
#
# documents = text_splitter.split_documents(documents)
# print(f'Number of documents: {len(documents)}')
#
# book_map_prompt = load_prompt('lc://prompts/summarize/map_reduce/summarize_book_map.yaml')
# print(f'Book map: {book_map_prompt}')
# book_combine_prompt = load_prompt('lc://prompts/summarize/map_reduce/summarize_book_combine.yaml')
#
# chain = load_summarize_chain(giga, chain_type='map_reduce',
#                              map_prompt=book_map_prompt,
#                              combine_prompt=book_combine_prompt,
#                              verbose=False)
#
# res = chain.invoke({'input_documents': documents})
# print(res['output_text'].replace('. ', '.\n'))
