from fastapi import APIRouter,Form
from langchain_core.messages import HumanMessage
from chatbot.graph.graph import chat_bot
from chatbot.schemas.request import ChatRequest
from fastapi.responses import Response

import uuid
from fastapi import FastAPI, Header
from pydantic import BaseModel
from database import Base, engine, SessionLocal
from models import Chat
from chatbot.llm.model import ask_bot

Base.metadata.create_all(engine)

router = APIRouter()

def twiml_message(body: str):
    xml = f"""
    <Response>
        <Message>{body}</Message>
    </Response>
    """
    return Response(content=xml, media_type="application/xml")

@router.post("/whatsapp-chat")
async def whatsapp_chat(Body: str = Form(...), From: str = Form(...)):
    print("Message:", Body)
    print("Sender:", From)
    state = {
        "messages": [HumanMessage(content=Body)]
    }

    result = chat_bot.invoke(state)

    reply = result["messages"][-1].content

    return twiml_message(reply)

def get_session(session_id: str | None):
    return session_id or str(uuid.uuid4())

@router.post("/chat/create")
def create_chat(session_id: str | None = Header(default=None)):
    session_id = get_session(session_id)

    db = SessionLocal()
    chat = Chat(session_id=session_id)
    db.add(chat)
    db.commit()
    db.refresh(chat)
    db.close()

    return {"session_id": session_id, "chat_id": chat.id}

class ChatInput(BaseModel):
    message: str
    
@router.post("/chat/{chat_id}")
def chat_api(data: ChatInput, chat_id: str):
    reply = ask_bot(chat_id, data.message)
    return {"response": reply}    