from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model = OllamaLLM(model="llama3.2")

template = """
You are an expert in answering questions about a Pizaa Restaurant

Here are some reviews: {reviews}

Here is the question: {question}
"""

prompt = ChatPromptTemplate.from_template(template=template)
chain = prompt | model


def handle_coversation():
    print("Welcome to the AI Agent! Type 'q' to exit.")
    print("You can ask questions about the restaurant reviews.")
    print("The AI Agent will use the reviews to answer your questions.")
    while True:
        print("\n\n------------------------------------------")
        question = input("Ask your question (q to exit): ")
        print("\n\n")
        if question.lower() == "q":
            break
        
        reviews = retriever.invoke(question)
        result = chain.invoke({"reviews": reviews, "question": question})
        print(result)


if __name__ == "__main__":
    handle_coversation()