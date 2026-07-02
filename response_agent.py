from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from configs.settings import MODEL_NAME

llm = ChatGroq(
    model_name=MODEL_NAME,
    temperature=0
)
response_prompt = ChatPromptTemplate.from_template("""
You are a helpful HR analytics assistant.

User Question:
{query}

Database Result:
{result}

Generate a concise business-friendly answer.
If records are returned:
summarize them.
If aggregate values are returned:
explain them clearly.
If no records are found:
say so politely.
""")

def response_agent(state):
    query = state["query"]
    result = state.get("output", [])
    response = llm.invoke(
        response_prompt.format_messages(
            query=query,
            result=result
        )
    )
    state["final_answer"] = response.content
    return state