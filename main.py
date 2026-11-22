from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM

from vector import retriever

model = OllamaLLM(model="qwen3:4b")

template = """
You are a highly skilled expert in answering questions about a pizza restuarant

Here are some relevant reviews:
{reviews}

Here is the question to answer:
{questions}
"""

prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model

while True:
    question = input("Ask anything (q for quit): ").strip()

    if question == "q":
        break

    reviews = retriever.invoke(question)

    result = chain.invoke({"reviews": reviews, "questions": question})
    print(result)
