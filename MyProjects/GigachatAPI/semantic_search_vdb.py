from langchain.document_loaders import TextLoader
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from pathlib import Path

file_path = Path('input/part1.txt')

if not file_path.exists():
    raise FileNotFoundError(f"Файл не найден по пути: {file_path.resolve()}")

loader = TextLoader(file_path, encoding='utf-8')
documents = loader.load()

text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

db = Chroma.from_documents(docs, embeddings)

query = 'Что сказала Анна ?'
docs = db.similarity_search(query)

for i, doc in enumerate(docs):
    print(f'Chunk N: {i}')
    print(doc.metadata)
    print(doc.page_content)
