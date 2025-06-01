from helper import validate_habit_question, habits_ai
import json

def main():
    print("Assistente de Criação de Hábitos (digite 'sair' para sair)\n")
    
    while True:
        try:
            user_input = input("Qual hábito você gostaria de criar?\n").strip()
            
            if user_input.lower() in ["sair"]:
                print("Saindo....")
                break
                
            if not user_input:
                print("Por favor descreva um hábito válido\n")
                continue
                
            if not validate_habit_question(user_input):
                print("Isso não é um hábito. Por favor descreva um hábito que você gostaria de criar.\n")
                continue
                
            response = habits_ai(user_input)
            habit_data = json.loads(response.content)
            
            if not habit_data or "name" not in habit_data:
                raise ValueError("Falha ao criar um hábito válido. Tente novamente.\n")
            
            print(json.dumps(habit_data, indent=2, ensure_ascii=False))

        except json.JSONDecodeError:
            print("Erro ao criar o hábito. Tente novamente.\n")
        except ValueError as e:
            print(f"Erro: {e}\n")
        except Exception as e:
            print(f"Um erro inesperado aconteceu: {e}\n")

if __name__ == "__main__":
    main()