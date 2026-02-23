from fastapi import APIRouter
from app.models.chat_models import MoviePreferences, MovieResponse
from app.services.chat_service import ChatService

router = APIRouter()

@router.post("/recommend", response_model=MovieResponse)
def recommend_movies(preferences: MoviePreferences):
    movies = ChatService.recommend_movies(preferences)

    return MovieResponse(recommendations=movies)