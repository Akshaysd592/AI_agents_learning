from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv
load_dotenv()

pdf_path = Path(__file__).parent/"nodejs.pdf"

#Load this file in python program
loader = PyPDFLoader(file_path=pdf_path)
docs = loader.load() # this will load each page into docs 


#Chunking the docs into smaller chunks
text_splitter  = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    overlap=400 # overlap is needed because we don't want go lost context from previous paragraph, because may be little information is needed from last paragraph which is take by overlap

)

chunks = text_splitter.split_documents(documents=docs)

# Vector embedding
embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-large"
)

vector_store = QdrantVectorStore.from_documents(
    documents=chunks,
    embedding=embedding_model,
    url="http://localhost:6333",
    collection_name="learning_rag"

)

print("Indexing of document done")
# After running this code you can check the vector database having vector embeddings
