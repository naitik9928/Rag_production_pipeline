from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
import os

embed=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

def load_documents(path:str):
    document_path=path

    loader=PyPDFDirectoryLoader(path)
    docs=loader.load()

    splitter=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=50)

    splited_docs=splitter.split_documents(docs)

    chroma_store=Chroma.from_documents(
        documents=splited_docs,
        embedding=embed,
        persist_directory="chroma_database"

    )

if __name__=="__main__":
    BASE_DIR=os.path.dirname(os.path.abspath(__file__))

    PATH=os.path.join(BASE_DIR,"docs")

    load_documents(PATH)