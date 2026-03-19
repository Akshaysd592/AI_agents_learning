

from openai import OpenAI
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
load_dotenv()

embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-large"
)

openai_client  = OpenAI()

vector_db = QdrantVectorStore.from_existing_collection(
    embedding=embedding_model,
    url="http://localhost:6333",
    collection_name="learning_rag"
)

# take user input
user_query = input("Ask questions: ")

#relevant chunks from vector db for user query
search_result = vector_db.similarity_search(query=user_query) # this will conver user_query into vector embedding and then check with vector embeddings stored in vector database


context = "\n\n\n".join([f"Page Content: {result.page_content}\nPage Number: {result.metadata['page_label']}\nFile Location: {result.metadata['source']}" for result in search_result])


SYSTEM_PROMPT= f""" 
 You are a helpful AI assistant who answers user query on the available context retrived from a PDF file along with page_content and page number.

 You should only answer the user based on the following context and navigate the user to open the right page number to know more

 Context:
 {context}
"""


response = openai_client.chat.completions.create(
    model="gpt-5",
    messages=[
        {"role":"system","content":SYSTEM_PROMPT},
        {"role":"user","content":user_query}
    ]

)

print(f"Response: {response.choices[0].message.content}")
# Now run the program since index.py alread completed indexing phase and vector db had vector embeddings with chunks
# questions like: can you help me understand debugging in nodejs
