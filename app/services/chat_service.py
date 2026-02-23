from app.prompts.movie_prompt import build_movie_prompt
from app.services.openai_service import OpenAIService
from app.models.chat_models import MoviePreferences

class ChatService:

    @staticmethod
    def recommend_movies(preferences: MoviePreferences):
        """makes the connection between the prompt creation function and the provided preferences and returns the recommendation"""
        prompt = build_movie_prompt(preferences)
        result = OpenAIService.get_movie_recommendations(prompt)

        movies = result.split("\n")
        movies = [movie.strip() for movie in movies if movie.strip()]

        return movies