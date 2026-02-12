from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from chatbot.api.routes import router



app = FastAPI(title="LangGraph Chatbot API")



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # or ["http://localhost:5173"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router)

@app.get("/")
def root():
    return {"status": "Chatbot running"}
