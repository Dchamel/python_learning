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

# db2 = Chroma.from_texts(texts, embeddings)
# retriever = db.as_retriever()
# retrieved_docs = retriever.invoke('Что сказала Анна ?')
# print(retrieved_docs[0].page_content)

# Base Retriever
# 'k' - docs number in return
# 'score_threshold' - порог схожести для расстояния между эмбедингами, в результаты попадут только дки, для которых значение метрики расстояния до запроса превышает порог

retriever = db.as_retriver(
    search_kwargs={
        'k': 1,
        'score_threshold': 0.5
    }
)
docs = retriever.get_relevant_documents('Кто такая Анна ?')

# MMR (Maximum Marginal Relevance)
# Если в бвзе дубли - MMR, алгоритм поиска и ранжирования. Он учитывает релевантность каждого документа и "новизну" информации в нём относительно отобранных ранее.
# MMR позволяет получить релевантные и при этом максимально насыщенные информацие доки без дублирования

retriever = db.as_retriver(search_type='mmr')

# MultiQuery
# MQR - для получения максимально релеванной информации и полной по отдельному запросу. Расширяет запрос, генерируя похожие на него по смыслу.
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain.chat_models import GigaChat

question = 'Где была Анна в начале книги ?'

llm = GigaChat()
retriever_from_llm = MultiQueryRetriever.from_llm(
    retriever=vectordb_as_retriever(), llm=llm
)

# HyDE
# Hypothetical Document Embeddings
# Поиск релевантных документов и генерация гипотетического, необязательно достоверного
from langchain.chains import HypotheticalDocumentEmbedder
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings

base_embeddings = SentenceTransformerEmbeddings(model='all-MiniLM-L6-v2')
llm = GigaChat()

embeddings = HypotheticalDocumentEmbedder.from_llm(llm, base_embeddings, 'web_search')

db = Chroma.from_texts(texts, embeddings)

query = 'Кто есть Анна ?'
docs = db.similarity_search(query)
