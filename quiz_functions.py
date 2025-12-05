import random
import json
import os 
import pygame
pygame.init()
pygame.mixer.init()
print(">>> quiz_functions IMPORTADO NOVAMENTE")

score = [0,0]
players = ["jogador1","jogador2"] 
current_player = 0
current_rounds = 0 
perguntas = []

# it created the questions archive in case it didn't already exist
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
QUESTION_FILE = os.path.join(BASE_DIR, "questions", "quiz_data.json") 
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

def get_winner():
    if score[0] > score[1]:
        return  "player 1 wins"
    elif score[1]> score[0]:
        return  "player 2 wins"
    else:
        return  "empate"

def verificar_resposta(resposta_do_usuario,pergunta):
    global score,current_player
       
    if resposta_do_usuario.strip() == pergunta["resposta"].strip():
        
        score[current_player] +=1
        return hit_sound(),True
    else:
        return error_sound(),False


def next_move():
     global current_rounds,current_player
     current_player = (current_player + 1) % 2  # alterna jogadores
     current_rounds += 1



def reset_game():
    global score, current_rounds, current_player
    score = [0, 0]
    current_rounds = 0
    current_player = 0

    print("RESETANDO O JOGO!")

#function that randomly selects questions
def draw_questions(qnt):
    questions = load_data()
    if qnt > len(questions):
        qnt = len(questions)
    return random.sample(questions, qnt)


def hit_sound():
    music_path = "somquiz.mp3"

    if not pygame.get_init():
        pygame.init()
    if not pygame.mixer.get_init():
        pygame.mixer.init()

    pygame.mixer.music.load(music_path)
    pygame.mixer.music.set_volume(0.7)

def error_sound():
    music_path = "somquiz.mp3"

    if not pygame.get_init():
        pygame.init()
    if not pygame.mixer.get_init():
        pygame.mixer.init()

    pygame.mixer.music.load(music_path)
    pygame.mixer.music.set_volume(0.7)