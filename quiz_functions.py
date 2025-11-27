import random
import json
import os 

# it created the questions archive in case it didn't already exist
QUESTION_FILE = "questions/quizquestions.json" 
os.makedirs("questions", exist_ok=True)


# function to load all data
def load_data():
    if os.path.exists(QUESTION_FILE):
        with open(QUESTION_FILE, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

#function to select randomly
def select_random(lista):
    return random.choice(lista)


#function that randomly selects questions
def draw_questions(qnt):
    questions = load_data()
    random_question = random.sample(questions,qnt)
    return random_question

def check_answers(resposta_escolhida):
    return
     