# %%
import requests
from bs4 import BeautifulSoup
import langchain_text_splitters
import llm_functions 
from openai import OpenAI
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
import streamlit as st
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveJsonSplitter


@st.cache_resource
def scrap_data():

    def scrape_page(url):
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        
        soup = BeautifulSoup(response.text, 'html.parser')
        data = soup.get_text()

        return data

        
    urls_dict = {"CPF contribution rate for SPR": 'https://help.swingvy.com/knowledge/cpf-contribution-rate-for-singapore-permanent-residencespr',
                "Employer CPF Act under MOM" : "https://www.mom.gov.sg/employment-practices/central-provident-fund/employers-contributions",
                "CPF wage ceilings" : "https://www.dbs.com.sg/personal/articles/nav/retirement/how-the-cpf-changes-impact-you",
                "CPF contributions for platform workers" : "https://www.mom.gov.sg/employment-practices/platform-workers-act/cpf-contributions-for-platform-workers"
    }

    scrapped_all = {}   
    for name, url in urls_dict.items():
        scrapped_all[name] = scrape_page(url)


    splitter = RecursiveJsonSplitter(max_chunk_size=400)

    json_chunks = splitter.split_json(json_data=scrapped_all)

    json_docs = splitter.create_documents(texts=[scrapped_all])
    for chunk in json_chunks:
        print(chunk)


    embeddings_model = OpenAIEmbeddings(model='text-embedding-3-small')
    vectorstore = FAISS.from_documents(documents=json_docs, embedding=embeddings_model)

    return vectorstore


prompt = ChatPromptTemplate([ ("human", "You are an assistant for question-answering tasks related to CPF contribution.\
                                Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. You can present the findings in a table or in point form. \
Question: {question} \
Context: {context} \
Answer:")])

qa_chain = RetrievalQA.from_chain_type(
    ChatOpenAI(model='gpt-4o-mini', temperature=0), retriever=scrap_data().as_retriever(), chain_type_kwargs={"prompt": prompt}
)

def ask_tax_relief_qn(question):
    result = qa_chain.invoke({"query": question})
    return(result["result"])




