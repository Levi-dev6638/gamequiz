import random
import json
import os 
from tkinter import messagebox


score = [0,0]
players = ["jogador1","jogador2"] 
current_player = 0
current_rounds = 0 
perguntas = []

# it created the questions archive in case it didn't already exist
QUESTION_FILE = "questions/quiz_data.json" 
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

def finalizar_quiz():
    if score[0] > score[1]:
        vencedor = "player 1 wins"
    elif score[1]> score[0]:
        vencedor = "player 2 wins"
    else:
        vencedor = "empate"

    messagebox.showinfo(
        "fim do quiz",
        f"placar final:\n"
        f"jogador 1: {score[0]}\n"
        f"player 2 : {score [1]}\n"
        f"{vencedor}"
    )


def show_questions ():
    question = perguntas[current_rounds]

    lbl_question.config(text=question["pergunta"])
    lbl_player.config(text = f"vez de {players[current_player]}")
    lbl_pontos.config(text=f"J1: {score[0]} / J2: {score[1]} / Round: {current_rounds+1}")

    resposta1.config(text=pergunta["opcoes"][0])
    resposta2.config(text=pergunta["opçoes"][1])
    resposta3.config(text=pergunta["opçoes"][3])


def responder(resposta):
    pergunta = perguntas[current_rounds]

    verificar_resposta(resposta,pergunta)
    next_move()
#function to select randomly
def select_random():
    global current_player
    current_player = random.randint(0,1)


def verificar_resposta(resposta_do_usuario,pergunta):
    global score,current_player

    if resposta_do_usuario == pergunta["resposta"]:
        score +=1
        return

def next_move():
    global current_rounds

    select_random()

    if current_player == 0:
        current_rounds +=1

    if current_rounds < len(perguntas):
        show_questions()
    else:
        finalizar_quiz()


#function that randomly selects questions
def draw_questions(qnt):
    questions = load_data()
    random_question = random.sample(questions,qnt)
    return random_question

def check_answers(resposta_escolhida):
    return
     