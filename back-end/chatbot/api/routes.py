from fastapi import APIRouter,Form
from langchain_core.messages import HumanMessage
from chatbot.graph.graph import chat_bot
from chatbot.schemas.request import ChatRequest
from fastapi.responses import Response
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

@router.post("/chat")
def chat_endpoint(request: ChatRequest):
    state = {
        "messages": [HumanMessage(content=request.message)]
    }

    result = chat_bot.invoke(state)

    return {
        "reply": result["messages"][-1].content
    }
