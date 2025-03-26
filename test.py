from langchain.embeddings import OpenAIEmbeddings
import os
from dotenv import load_dotenv

load_dotenv()


print (os.environ['OPENAI_API_KEY'])

embeddings = OpenAIEmbeddings(
    model="text-embedding-ada-002",
    openai_api_key=os.environ['OPENAI_API_KEY']
)
print(embeddings.embed_query("Hello, world!"))
