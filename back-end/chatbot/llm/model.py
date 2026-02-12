from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
from memory import load_history, save_message
from langchain.messages import HumanMessage, AIMessage

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
    api_key=os.getenv("OPENAI_API_KEY")
)


def ask_bot(chat_id: str, user_text: str):

    history = load_history(chat_id)

    history.append(HumanMessage(content=user_text))

    response = llm.invoke(history)

    save_message(chat_id, "user", user_text)
    save_message(chat_id, "assistant", response.content)

    return response.content