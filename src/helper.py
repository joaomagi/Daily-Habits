from config import ia_model

groq = ia_model()

def validate_habit_question(question: str):
    """Valida se a pergunta é sobre criação de um hábito"""
    prompt = [
        ("system", 
         "You are a habit validation expert. Strictly analyze if this is a request to create or modify a habit.\n"
         "Consider only these as valid habit requests:\n"
         "- Creating new habits\n"
         "- Modifying existing habits\n"
         "- Habit tracking requests\n"
         "- Habit improvement suggestions\n\n"
         "If the input is unclear, too short, or not about habits, reject it.\n"
         "Answer only 'yes' or 'no'."),
        ("human", question)
    ]
    response = groq.invoke(prompt)
    return "yes" in response.content.lower()

def habits_ai(question: str):
    """Gera um hábito com base na entrada do usuário"""
    prompt = [
        ("system", 
        "You are a habit creation expert. Your task is to read the user's request and generate a JSON with:\n"
        "- 'name': short habit name\n"
        "- 'description': detailed description\n"
        "- 'color': integer 1-5 (random if unspecified)\n"
        "- 'daysOfTheWeek': list of days (0=Sunday)\n"
        "Respond ONLY with valid JSON, no additional text and traslate to brazilian portuguese."),
        ("human", question),
    ]
    return groq.invoke(prompt)