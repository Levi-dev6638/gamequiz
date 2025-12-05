import tkinter as tk
from tkinter import messagebox
import quiz_functions as qf

root = tk.Tk()
root.title("Gerenciador de Músicas")
root.geometry("900x850")
root.config(bg="#e8e8e8")

var_resposta = tk.StringVar()
lbl_pergunta = None
resposta1 = None
resposta2 = None
resposta3 = None
lbl_confirmation = None
fm_quiz = None
dark_theme = False
def show_questions():
    
    
    qf.pergunta = qf.perguntas[qf.current_rounds]

    lbl_pergunta.config(text=qf.pergunta["pergunta"])
    resposta1.config(text=qf.pergunta["opcoes"][0], value=qf.pergunta["opcoes"][0])
    resposta2.config(text=qf.pergunta["opcoes"][1], value=qf.pergunta["opcoes"][1])
    resposta3.config(text=qf.pergunta["opcoes"][2], value=qf.pergunta["opcoes"][2])

    lbl_confirmation.config(text=f"Vez de {qf.players[qf.current_player]}", fg="black")
    var_resposta.set("")  


def responder():
    resposta = var_resposta.get()
    if not resposta:
        messagebox.showwarning("Atenção", "Selecione uma resposta!")
        return

    pergunta = qf.perguntas[qf.current_rounds]
    correta = qf.verificar_resposta(resposta, pergunta)

    if correta:
        lbl_confirmation.config(text="✔ Resposta correta!", fg="green")
    else:
        lbl_confirmation.config(text="✘ Resposta errada!", fg="red")

    root.after(3000, proxima_pergunta)
    print("DEBUG resposta selecionada:", var_resposta.get())

def proxima_pergunta():
    qf.next_move()
    if qf.current_rounds < len(qf.perguntas):
        show_questions()
    else:
        messagebox.showinfo(
            "Fim do Quiz",
            f"Placar final:\n"
            f"Jogador 1: {qf.score[0]}\n"
            f"Jogador 2: {qf.score[1]}\n"
            f"{qf.get_winner()}"
        )
        root.destroy()
    print(">>> Entrou em proxima_pergunta()")



def build_quiz_screen():

    global lbl_pergunta, resposta1, resposta2, resposta3, lbl_confirmation, fm_quiz

    fm_quiz = tk.Frame(root, bg="#ffffff", bd=2, relief="groove")
    fm_quiz.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    lbl_pergunta = tk.Label(fm_quiz, text="", font=("Arial", 18))
    lbl_pergunta.grid(row=0, column=0, columnspan=2, pady=20)

    var_resposta.set("")

    resposta1 = tk.Radiobutton(fm_quiz, text="", variable=var_resposta, value="", font=("Arial", 14))
    resposta1.grid(row=1, column=0, sticky="w", pady=10)

    resposta2 = tk.Radiobutton(fm_quiz, text="", variable=var_resposta, value="", font=("Arial", 14))
    resposta2.grid(row=2, column=0, sticky="w", pady=10)

    resposta3 = tk.Radiobutton(fm_quiz, text="", variable=var_resposta, value="", font=("Arial", 14))
    resposta3.grid(row=3, column=0, sticky="w", pady=10)

    bt_response = tk.Button(fm_quiz, text="Responder", bg="#0d097f", fg="#FFFFFF",
                            font=("Arial", 14, "bold"), height=2, width=30,
                            command=responder)
    bt_response.grid(row=4, column=0, pady=20)

    lbl_confirmation = tk.Label(fm_quiz, text="", font=("Arial", 20))
    lbl_confirmation.grid(row=5, column=0, pady=20)


def starting_the_game():
    qnt = entry_rounds.get()
    if not qnt.isdigit():
        messagebox.showerror("Erro", "Digite um número válido!")
        return
    qnt = int(qnt)

    qf.reset_game()


    qf.perguntas = qf.draw_questions(qnt)
    print("Quantidade de perguntas carregadas:", len(qf.perguntas))

    if len(qf.perguntas) == 0:
        messagebox.showerror("Erro", "Nenhuma pergunta encontrada!")
        return

    global players
    qf.players[0] = entry_player1.get() or "Jogador 1"
    qf.players[1] = entry_player2.get() or "Jogador 2"


    frame.destroy()
    build_quiz_screen()
    show_questions()




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

entry_rounds = tk.Entry(frame,justify="center",font=("arial",14))
entry_rounds.grid(row=5,column=0,padx=5,pady=30)

bt_alttema = tk.Button(frame, text="Alterar Tema", bg="#0d097f", fg="#FFFFFF",
                 font=("Arial", 14, "bold"),height=2,width=30,command=toggle_theme)
bt_alttema.grid(row=6, column=0, padx=5, pady=30)

bt_start = tk.Button(frame, text="Iniciar Jogo", bg="#0b148b", fg="#ffffff",
                 font=("Arial", 14, "bold"),command=starting_the_game,height=2,width=30)
bt_start.grid(row=7, column=0, padx=5, pady=30)



root.mainloop()
