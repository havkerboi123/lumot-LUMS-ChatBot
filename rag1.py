from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import embeddings
from dotenv import load_dotenv
import os
from langchain_huggingface import HuggingFaceEmbeddings

# Load environment variables from .env file
load_dotenv()

# Now you can access the API key
os.environ['GOOGLE_API_KEY'] = "AIzaSyCgv7f-P8hqxOhPVLdmf8_-7u2IZh1QAeM"
text_splitter = RecursiveCharacterTextSplitter()

file_path = 'reddit-lums/data.txt'
load_dotenv


with open(file_path, 'r') as file:
    content = file.read()

chunks = text_splitter.split_text(content)


# Load the Chroma vector store from the stored directory
embed = HuggingFaceEmbeddings()
CHROMA_PATH='chroma/final'
db = Chroma.from_documents(chunks, OpenAIEmbeddings(), persist_directory=CHROMA_PATH)
db.persist()



import os
os.environ['GOOGLE_API_KEY'] = "AIzaSyCgv7f-P8hqxOhPVLdmf8_-7u2IZh1QAeM"
from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-pro")
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import WebBaseLoader
from langchain.chains import StuffDocumentsChain
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate

from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-pro",
                 temperature=0.7, top_p=0.85)

prompt_template = """
  Please answer the question in as much detail as possible based on the provided context.
  Ensure to include all relevant details. If the answer is not available in the provided context,
  kindly respond with "The answer is not available in the context." Please avoid providing incorrect answers.
\n\n
  Context:\n {context}?\n
  Question: \n{question}\n

  Answer:
"""

prompt = PromptTemplate(template = prompt_template, input_variables = ["context", "question"])
# chain = load_qa_chain(llm, chain_type="stuff", prompt=prompt)
question="how are the hostels at lums"

docs = db.similarity_search("hostel")
print(docs)