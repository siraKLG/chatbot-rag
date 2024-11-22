from langchain.llms import OpenAI

def generate_response_without_rag(query, temperature=0.7):
    llm = OpenAI(model_name="text-davinci-003", temperature=temperature)
    return llm(query)
