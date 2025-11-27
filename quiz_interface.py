import tkinter as tk
from tkinter import messagebox
import os

root = tk.Tk()
root.title("Gerenciador de Músicas")
root.geometry("900x850")
root.config(bg="#e8e8e8")

frame = tk.Frame(root, bg="#ffffff", bd=2, relief="groove",width=30,height=50)
frame.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

lbl_name_game = tk.Label(frame,text="MUSICAL QUIZ",font=("Arial",30))
lbl_name_game.grid(row=0,column=3,padx=5,pady=5)

lbl_nameplayers = tk.Label(frame,text="report the players' names",font=("Arial",10))
lbl_nameplayers.grid(row=1,column=3,padx=5,pady=5)

entry_player1 = tk.Entry(frame,font=("arial",13))
entry_player1.grid(row=2,column=3,padx=5,pady=5)

root.mainloop()
