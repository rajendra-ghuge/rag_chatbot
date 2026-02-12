from langgraph.graph import StateGraph, START, END
from chatbot.schemas.state import ChatState
from chatbot.llm.model import llm

def chatbot_node(state: ChatState):
    response = llm.invoke(state["messages"])
    return {"messages": state["messages"] + [response]}

builder = StateGraph(ChatState)

builder.add_node("chatbot", chatbot_node)
builder.add_edge(START, "chatbot")
builder.add_edge("chatbot", END)

chat_bot = builder.compile()
