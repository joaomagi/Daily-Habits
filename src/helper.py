import json 
from src.config import ia_model

groq = ia_model()


def validate_habit_question(question: str):
    prompt = [
        ("system","Is the following question related to creating or changing personal habits? Answer only 'yes' or 'no'."),
        ("human", question)
    ]
    response = groq.invoke(prompt)
    if "yes" not in response.content.lower():
        raise ValueError("A pergunta não parece estar relacionada à criação de hábitos.")
    return True

def to_json(question: str):     
    return json.dumps({"question": question, "category":"habit"}) 
  

def habits_ia(json_question: str):
    prompt = [
        ("system", "You are a Habit Formation Specialist with expertise in behavioral psychology and neuroscience. "
        "Your role is to deliver personalized, evidence-based habit plans that turn goals into automatic, lasting routines—without asking follow-up questions, "
        "translate to English respond in JSON format so I can consume it on my websit"),
        ("human", json_question),
    ]
    return prompt