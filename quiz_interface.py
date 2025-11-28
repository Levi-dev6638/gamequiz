import tkinter as tk
from tkinter import messagebox
import os

root = tk.Tk()
root.title("Gerenciador de Músicas")
root.geometry("900x850")
root.config(bg="#e8e8e8")

def starting_the_game():
    start = tk.Toplevel()
    start.title("quiz interativo")
    start.geometry("900x850")
    start.config(bg="#e8e8e8")

    lbl_pergunta = tk.Label(start,text="gnfdgnfgnjkgfgdfjkgnfkjgfkgbfkjgbfkjgbfkdjgbfdkjbgfdkj",width=40,font=("Arial",14))
    lbl_pergunta.grid(row=0,column=2,padx=5,pady=30)

    resposta1 = tk.Radiobutton(start,text="r")
    resposta1.grid(row=1,column=0,padx=5,pady=30)

    resposta2 = tk.Radiobutton(start,text="r")
    resposta2.grid(row=2,column=0,padx=5,pady=30)

    resposta3 = tk.Radiobutton(start,text="r")
    resposta3.grid(row=3,column=0,padx=5,pady=30)

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

lbl_nameplayers = tk.Label(frame,text="number of rounds:",width=40,font=("Arial",14))
lbl_nameplayers.grid(row=4,column=0,padx=5,pady=10)

entry_player2 = tk.Entry(frame,justify="center",font=("arial",14))
entry_player2.grid(row=5,column=0,padx=5,pady=30)

bt_alttema = tk.Button(frame, text="Alterar Tema", bg="#0d097f", fg="#FFFFFF",
                 font=("Arial", 14, "bold"),height=2,width=30)
bt_alttema.grid(row=6, column=0, padx=5, pady=30)

bt_alttema = tk.Button(frame, text="Iniciar Jogo", bg="#0b148b", fg="#ffffff",
                 font=("Arial", 14, "bold"),command=starting_the_game,height=2,width=30)
bt_alttema.grid(row=7, column=0, padx=5, pady=30)



root.mainloop()
