
from langchain_core.runnables import RunnableLambda 


from src.config import ia_model

from src.helper import validate_habit_question
from src.helper import to_json
from src.helper import habits_ia



def main():
     while True: 
        try:
            user_input = input("Vamos criar um habito: ")

            if user_input.lower() == "sair":
                print("Saindo....")
                break

            valid_question = RunnableLambda(validate_habit_question)        
            json_question = RunnableLambda(to_json)
            ia_answer = RunnableLambda(habits_ia)
            groq = ia_model()
    
            chain = valid_question | json_question | ia_answer | groq

            response = chain.invoke(user_input)
            print(response.content)

            print("\nCaso queira sair digite Sair\n")

        except ValueError as e: 
            print("Tente novamente ")



if __name__ == "__main__": 
    main()