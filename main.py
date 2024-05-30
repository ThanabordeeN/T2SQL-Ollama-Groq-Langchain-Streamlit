from langchain_experimental.sql import SQLDatabaseChain
from langchain_community.llms import Ollama #can change to other llm
from langchain_community.utilities import  SQLDatabase
import streamlit as st
from langchain_groq import ChatGroq

def sql_to_text(sql_url: str, method: str, question: str, model_input: str, api_key: str | None = None) -> str:
    """
    Converts an input question into a SQL query, executes the query on a database, and returns the answer.

    Args:
        sql_url (str): The URL of the SQL database.
        method (str): The method to use for language model. Possible values are "ollama" or "groq".
        question (str): The input question.
        model_input (str): The model input to use for the language model.
        api_key (str | None, optional): The API key for the "groq" method. Defaults to None.

    Returns:
        str: The final answer.

    Raises:
        Exception: If the specified model is not found.

    """
    

    # setup llm
    try:
        if method == "ollama":
            llm = Ollama(temperature=0, model=model_input)
        elif method == "groq":
            llm = ChatGroq(temperature=0, groq_api_key=api_key, model_name=model_input)
    except:
        st.error("Model not found, please try again")
        st.stop()

    # Create db chain
    QUERY = """
    Given an input question, first create a syntactically correct postgresql query to run, then look at the results of the query and return the answer.
    Use the following format:

    "Question": "Question here"
    "SQLQuery": "SQL Query to run"
    "SQLResult": "Result of the SQLQuery"
    "Answer": "Final answer here"

    "Command: {question}"
    """
    # setup database
    db = SQLDatabase.from_uri(sql_url)
    # Setup the database chain
    db_chain = SQLDatabaseChain(llm=llm, database=db, verbose=False)
    # input prompt
    question = QUERY.format(question=question)
    result = db_chain.run(question)
    st.write("Result: ")
    st.write(result)


st.title("SQL Database Chain")
st.write("This is a SQL Database Chain that can answer questions about a database. \
    It can answer questions like 'What is the name of the person with id 1?' \
    @cepheusn_22")
st.write("Please input your question below:")

model_provider = st.sidebar.selectbox("Model Provider", ("ollama","groq"))
if model_provider == "ollama":
    st.sidebar.write("Please input the model below:")
    model = st.sidebar.text_input("Model")
if not model_provider:
    st.sidebar.info("Please select a model provider")
elif model_provider == "groq":
    st.sidebar.write("Please input the model below:")
    api_key= st.sidebar.text_input("API Key") 
    if model_provider == "groq" and not api_key:
        st.sidebar.info("Please enter an API key")
    model = st.sidebar.text_input("Model")

if model_provider == "ollama" and not model:
    st.sidebar.info("Please enter a model")
if not model_provider:
    st.sidebar.info("Please select a model provider")
sql_url = st.sidebar.text_input("SQL URL", "postgresql://postgres:postgres@localhost:5432/postgres")

with st.form("question_form",clear_on_submit= False):
    question = st.text_input("Question")
    submit_button = st.form_submit_button("Submit")
    try:
        if not question:
            st.info("Please enter a question")
    except:
        st.info("try again")
        pass
    if submit_button:  
        if model_provider == "groq":
            sql_to_text(sql_url, model_provider, question, model, api_key)
        elif model_provider == "ollama":
            sql_to_text(sql_url, model_provider, question, model)
    

