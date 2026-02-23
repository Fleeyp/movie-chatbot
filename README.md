This project was created as a study case, and has no financial purpose.
All the code was made by me, assisted by AI, following good structure and architect behavior.
If you wish to test it, provide your own working OpenAI secret key in your .env,
run 'uvicorn app.main:app --reload' and test on your desired platform.

Here's the JSON I sent on Postman:

{
  "genre": "horror",
  "era": "modern",
  "country": "", #tested the blank country possibility
  "duration": "long"
}

And the response was:

{
    "recommendations": [
        "1. It Follows (2014) - USA - 100 minutes",
        "2. The Witch (2015) - USA - 92 minutes",
        "3. Hereditary (2018) - USA - 127 minutes",
        "4. Midsommar (2019) - USA - 148 minutes",
        "5. The Invisible Man (2020) - USA - 124 minutes",
        "6. The Conjuring (2013) - USA - 112 minutes",
        "7. The Cabin in the Woods (2011) - USA - 95 minutes",
        "8. Doctor Sleep (2019) - USA - 152 minutes",
        "9. The Babadook (2014) - Australia - 93 minutes",
        "10. It (2017) - USA - 135 minutes"
    ]
}

I also tested:

{
  "genre": "thriller",
  "era": "modern",
  "country": "South Korea",
  "duration": "long"
}

And got:

{
    "recommendations": [
        "1. The Wailing (2016) - South Korea - 156 minutes",
        "2. Parasite (2019) - South Korea - 132 minutes",
        "3. The Call (2020) - South Korea - 112 minutes",
        "4. Time to Hunt (2020) - South Korea - 138 minutes",
        "5. The Drug King (2018) - South Korea - 140 minutes",
        "6. Night in Paradise (2020) - South Korea - 130 minutes",
        "7. The Outlaws (2017) - South Korea - 141 minutes",
        "8. Oldboy (2003) - South Korea - 120 minutes"
    ]
}

Feel free to make usage of this code as a basis. Have fun.