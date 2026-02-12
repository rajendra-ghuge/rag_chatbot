from database import SessionLocal
from models import Message
from langchain.messages import HumanMessage, AIMessage


def load_history(chat_id):
    db = SessionLocal()
    rows = db.query(Message).filter_by(chat_id=chat_id).all()
    db.close()

    messages = []

    for r in rows:
        if r.role == "user":
            messages.append(HumanMessage(content=r.content))
        else:
            messages.append(AIMessage(content=r.content))

    return messages


def save_message(chat_id, role, content):
    db = SessionLocal()
    db.add(Message(chat_id=chat_id, role=role, content=content))
    db.commit()
    db.close()
