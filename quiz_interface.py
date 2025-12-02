import tkinter as tk
from tkinter import messagebox
import os

root = tk.Tk()
root.title("Gerenciador de Músicas")
root.geometry("900x850")
root.config(bg="#e8e8e8")

def starting_the_game():
    fm_start = tk.Frame(root, bg="#ffffff", bd=2, relief="groove",width=5,height=50)
    fm_start.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

    lbl_pergunta = tk.Label(fm_start,text="",width=40,font=("Arial",14))
    lbl_pergunta.grid(row=0,column=2,padx=5,pady=30)

    resposta1 = tk.Radiobutton(fm_start,text="r")
    resposta1.grid(row=1,column=0,padx=5,pady=30)

    resposta2 = tk.Radiobutton(fm_start,text="r")
    resposta2.grid(row=2,column=0,padx=5,pady=30)

    resposta3 = tk.Radiobutton(fm_start,text="r")
    resposta3.grid(row=3,column=0,padx=5,pady=30)
   

dark_theme = False
def toggle_theme():
    global dark_theme
    dark_theme = not dark_theme

    if dark_theme:
        root.configure(bg="#2E2E2E")
        lbl_name_game.config(bg="#2E2E2E", fg="white")
        lbl_rounds.config(bg="#2E2E2E", fg="white")
        lbl_nameplayers.config(bg="#2E2E2E", fg="white")
        bt_alttema.config(bg="#555555", fg="white")
        bt_start.config(bg="#555555", fg="white")
        
    else:
        root.configure(bg="white")
        lbl_name_game.config(bg="#c1c1c4", fg="black")
        lbl_nameplayers.config(bg="#c1c1c4", fg="black")
        lbl_rounds.config(bg="#c1c1c4", fg="black")
        bt_alttema.config(bg="#0e10a3", fg="black")
        bt_start.config(bg="#0e10a3", fg="black")


root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

frame = tk.Frame(root, bg="#ffffff", bd=2, relief="groove",width=5,height=50)
frame.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

frame.grid_columnconfigure(0, weight=1)

lbl_name_game = tk.Label(frame,text="MUSICAL QUIZ",font=("Arial",30))
lbl_name_game.grid(row=0,column=0,padx=5,pady=30)

lbl_nameplayers = tk.Label(frame,text="Inform the players' names:",width=40,font=("Arial",14))
lbl_nameplayers.grid(row=1,column=0,padx=5,pady=30)

entry_player1 = tk.Entry(frame,justify="center",font=("arial",14),width=30)
entry_player1.grid(row=2,column=0,padx=5,pady=30,)

entry_player2 = tk.Entry(frame,justify="center",font=("arial",14),width=30)
entry_player2.grid(row=3,column=0,padx=5,pady=30)

lbl_rounds = tk.Label(frame,text="number of rounds:",width=40,font=("Arial",14))
lbl_rounds.grid(row=4,column=0,padx=5,pady=10)

entry_player2 = tk.Entry(frame,justify="center",font=("arial",14))
entry_player2.grid(row=5,column=0,padx=5,pady=30)

bt_alttema = tk.Button(frame, text="Alterar Tema", bg="#0d097f", fg="#FFFFFF",
                 font=("Arial", 14, "bold"),height=2,width=30,command=toggle_theme)
bt_alttema.grid(row=6, column=0, padx=5, pady=30)

bt_start = tk.Button(frame, text="Iniciar Jogo", bg="#0b148b", fg="#ffffff",
                 font=("Arial", 14, "bold"),command=starting_the_game,height=2,width=30)
bt_start.grid(row=7, column=0, padx=5, pady=30)



root.mainloop()
