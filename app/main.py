from fastapi import FastAPI
from app.controllers.chat_controller import router as chat_router

app = FastAPI(title="AI Movie Chatbot")

app.include_router(chat_router)