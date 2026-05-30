from langchain_chroma import Chroma 
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import AIMessage

load_dotenv()
parser =StrOutputParser()
embed=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.1,
    max_tokens=1024
)

def brain(user_query:str):
    vectoreStore=Chroma(
        persist_directory="chroma_database",
        embedding_function=embed
    )

    docs=vectoreStore.similarity_search(user_query,k=5)
    context="\n".join([doc.page_content for doc in docs ])
    prompt=PromptTemplate.from_template(template="Answer the user querry {user_query} only from the relevant context {context} if you dont know the answer just say I don't know stictly")

    chain=prompt|llm|parser

    response=chain.invoke({"user_query":user_query,"context":context})

    return response