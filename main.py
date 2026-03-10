from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
# Load environment variables from .env file
load_dotenv()


def main():
    print("Hello from langchain!!")

    information = """
Dr. Ing. h.c. F. Porsche AG, commonly known as Porsche,[a] is a German automobile manufacturer specializing in luxury, high-performance sports cars, SUVs and sedans, headquartered in Stuttgart, Baden-Württemberg, Germany. The company is owned by Volkswagen AG, a controlling stake of which is owned by Porsche Automobil Holding SE, usually shortened to Porsche SE. Porsche's current lineup includes the 911, Panamera, Macan, Cayenne and Taycan[8].
    """
    summary_template = """
    Given the information {information} about a company, I want you to provide:
    1. A short summary about the company 
    2. Two fun facts about the company
    """

    summary_prompt_template = PromptTemplate(input_variables=["information"], template = summary_template)

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    #llm = ChatOllama(model="gemma3:270m", temperature=0)
    # | is a pipe operator that chains the prompt template and the LLM, output from the prompt template is passed to the LLM
    chain = summary_prompt_template | llm
    response = chain.invoke(input = {"information": information})
    print(response.content)

if __name__ == "__main__":
    main()

