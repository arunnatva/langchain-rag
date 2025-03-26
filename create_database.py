from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
import openai 
from dotenv import load_dotenv
import os,sys
import shutil
import nltk

# Download NLTK modules
nltk.download("punkt_tab",download_dir="/Users/anatva/nltk_data")
nltk.download('averaged_perceptron_tagger_eng')


# Load environment variables. Assumes that project contains .env file with API keys
load_dotenv()
#---- Set OpenAI API key 
# Change environment variable name from "OPENAI_API_KEY" to the name given in 
# your .env file.
openai.api_key = os.environ['OPENAI_API_KEY']

#sys.exit(0)

CHROMA_PATH = "chroma"
#DATA_PATH = "data/books"
DATA_PATH = "data/policy_docs"



def main():
    generate_data_store()


def generate_data_store():
    documents = load_documents()
    chunks = split_text(documents)
    save_to_chroma(chunks)


#def load_documents():
#    loader = DirectoryLoader(DATA_PATH, glob="*.md")
#    documents = loader.load()
#    return documents

def load_documents():
    loader = PyPDFLoader(DATA_PATH + "/AGG-2023-12-01-AXAPlatinum-Generic.pdf")
    documents = loader.load()
    return documents



def split_text(documents: list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=2000,
        chunk_overlap=100,
        length_function=len,
        add_start_index=True,
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Split {len(documents)} documents into {len(chunks)} chunks.")

    document = chunks[10]
    print(document.page_content)
    print(document.metadata)

    return chunks


def save_to_chroma(chunks: list[Document]):
    # Clear out the database first.
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)

    # Create a new DB from the documents.
    db = Chroma.from_documents(
        chunks, OpenAIEmbeddings(), persist_directory=CHROMA_PATH
    )
    #db.persist()  ## from chroma 0.4 onwards, persist happens automatically, so this method is depracated
    print(f"Saved {len(chunks)} chunks to {CHROMA_PATH}.")


if __name__ == "__main__":
    main()
