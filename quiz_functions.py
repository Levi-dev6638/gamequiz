import random
import json
import os 
import pygame

pygame.init()
pygame.mixer.init()

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


#this function shows the winner
def get_winner():
    if score[0] > score[1]:
        return f" {players[0]} wins"
    elif score[1]> score[0]:
        return f"{players[1]} wins"
    else:
        return  "draw"

#check if the answer is correct and play the sound
def check_answer(user_response,question):
    global score,current_player
       
    if user_response.strip() == question["resposta"].strip():
        
        score[current_player] +=1
        hit_sound()
        return True
    
    else:
        error_sound()
        return False

#alternates the players and the round
def next_move():
     global current_rounds,current_player
     current_player = (current_player + 1) % 2  
     current_rounds += 1


#resets the value of the variables to zero
def reset_game():
    global score, current_rounds, current_player
    score = [0, 0]
    current_rounds = 0
    current_player = 0

#function that randomly selects questions
def draw_questions(qnt):
    questions = load_data()
    if qnt > len(questions):
        qnt = len(questions)
    return random.sample(questions, qnt)


def hit_sound():
    music= "somcerto.mp3"

    if not pygame.get_init():
        pygame.init()
    if not pygame.mixer.get_init():
        pygame.mixer.init()

    pygame.mixer.music.load(music)
    pygame.mixer.music.set_volume(0.7)
    pygame.mixer.music.play()

def error_sound():
    print("pygame:", pygame.get_init())
    print("mixer:", pygame.mixer.get_init())

    music_path = "somerro.mp3"

    if not pygame.get_init():
        pygame.init()
    if not pygame.mixer.get_init():
        pygame.mixer.init()

    pygame.mixer.music.load(music_path)
    pygame.mixer.music.set_volume(0.7)
    pygame.mixer.music.play()