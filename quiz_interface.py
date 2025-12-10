import tkinter as tk
from tkinter import messagebox
import quiz_functions as qf

root = tk.Tk()
root.title("music manager")
root.geometry("900x850")
root.config(bg="#000000")

var_response = tk.StringVar(value=None)
var_response.set(None)
lbl_question = None
response1 = None
response2 = None
response3 = None
lbl_confirmation = None
fm_quiz = None
dark_theme = False

# it shows the questions and whose turn it is
def show_questions():
    var_response.set(None)

    qf.pergunta = qf.perguntas[qf.current_rounds]

    lbl_question.config(text=qf.pergunta["pergunta"])
    response1.config(text=qf.pergunta["opcoes"][0], value=qf.pergunta["opcoes"][0])
    response2.config(text=qf.pergunta["opcoes"][1], value=qf.pergunta["opcoes"][1])
    response3.config(text=qf.pergunta["opcoes"][2], value=qf.pergunta["opcoes"][2])

    lbl_confirmation.config(text=f"Vez de {qf.players[qf.current_player]}", fg="black",bg="#FFFFFF") 
    if dark_theme:
        lbl_confirmation.config(text=f"Vez de {qf.players[qf.current_player]}", fg="white",bg="#370000")

def response():
    response = var_response.get()
    if not response:
        messagebox.showwarning("Atenção", "Selecione uma resposta!")
        return

    question = qf.perguntas[qf.current_rounds]
    correct = qf.check_answer(response, question)

    if correct:
        lbl_confirmation.config(text="✔ Resposta correta!", fg="green")
    else:
        lbl_confirmation.config(text="✘ Resposta errada!", fg="red")

    root.after(3000,next_question)

#new question
def next_question():
    qf.next_move()
    if qf.current_rounds < len(qf.perguntas):
        show_questions()
    else:
        messagebox.showinfo(
            "Fim do Quiz",
            f"Placar final:\n"
            f"Jogador {qf.players[0]} : {qf.score[0]}\n"
            f"Jogador {qf.players[1]} : {qf.score[1]}\n"
            f"{qf.get_winner()}"
        )
        root.destroy()
    



def build_quiz_screen():
    global lbl_question, response1, response2, response3, lbl_confirmation, fm_quiz

    fm_quiz = tk.Frame(root, bg="#ffffff", bd=2, relief="groove")
    fm_quiz.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    for i in range(7):      #row 0 a 6
        fm_quiz.rowconfigure(i, weight=1)
    for j in range(4):      #column 0 a 3
        fm_quiz.columnconfigure(j, weight=1)

    lbl_question = tk.Label(fm_quiz, text="", justify="center", font=("lexend", 18),bg="#FFFFFF",fg="black")
    lbl_question.grid(row=0, column=1, columnspan=2, pady=20, sticky="ew")

    response1 = tk.Radiobutton(fm_quiz, text="", variable=var_response, value="A", font=("lexend", 14),bg="#FFFFFF",fg="black")
    response1.grid(row=1, column=0, sticky="w", pady=10)

    response2 = tk.Radiobutton(fm_quiz, text="", variable=var_response, value="B", font=("lexend", 14),bg="#FFFFFF",fg="black")
    response2.grid(row=2, column=0, sticky="w", pady=10)

    response3 = tk.Radiobutton(fm_quiz, text="", variable=var_response, value="C", font=("lexend", 14),bg="#FFFFFF",fg="black")
    response3.grid(row=3, column=0, sticky="w", pady=10)

    bt_response = tk.Button(
        fm_quiz, text="Response", bg="#0F02C3", fg="#FFFFFF",
        font=("Arial", 14, "bold"), height=3, width=30,
        command=response
    )
    bt_response.grid(row=4, column=1, columnspan=2, pady=20, sticky="ew")

    lbl_confirmation = tk.Label(fm_quiz, text="", justify="center", font=("Arial", 20))
    lbl_confirmation.grid(row=5, column=1, columnspan=2, pady=20, sticky="ew")

    bt_exit = tk.Button(
        fm_quiz, text="Exit", justify="center", bg="#0F02C3", fg="#FFFFFF",
        font=("Arial", 14, "bold"), height=2, width=15,
        command=exit
    )
    bt_exit.grid(row=6, column=3, pady=20, sticky="ew")
    
    if dark_theme:
        fm_quiz.configure(bg="#370000")
        bt_response.config(bg="#000000", fg="white")
        bt_exit.config(bg="#000000", fg="white")
        
        response1.config(bg="#370000")
        response2.config(bg="#370000")
        response3.config(bg="#370000")

def exit():
    root.destroy()
    fm_quiz.destroy()   


def starting_the_game():
    qnt = entry_rounds.get()
    if not qnt.isdigit():
        messagebox.showerror("Erro", "Digite um número válido!")
        return
    qnt = int(qnt)

    qf.reset_game()

    qf.perguntas = qf.draw_questions(qnt)

    if len(qf.perguntas) == 0:
        messagebox.showerror("Erro", "Nenhuma pergunta encontrada!")
        return

    qf.players[0] = entry_player1.get() or "Jogador 1"
    qf.players[1] = entry_player2.get() or "Jogador 2"


    frame.destroy()
    build_quiz_screen()
    show_questions()




def toggle_theme():
    global dark_theme
    dark_theme = not dark_theme

    if dark_theme:
        root.configure(bg="#000000")
        frame.config(bg="#370000")
        lbl_name_game.config(bg="#370000", fg="white")
        lbl_rounds.config(bg="#370000", fg="white")
        lbl_nameplayers.config(bg="#370000", fg="white")
        bt_alttema.config(bg="#000000", fg="white")
        bt_start.config(bg="#000000", fg="white")
        
        
    else:
        root.configure(bg="black")
        frame.config(bg="#FFFFFF")
        lbl_name_game.config(bg="#FFFFFF", fg="black")
        lbl_nameplayers.config(bg="#FFFFFF", fg="black")
        lbl_rounds.config(bg="#FFFFFF", fg="black")
        bt_alttema.config(bg="#0F02C3", fg="white")
        bt_start.config(bg="#0f02c3", fg="white")


root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

frame = tk.Frame(root, bg="#ffffff", bd=2, relief="groove",width=5,height=50)
frame.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

frame.grid_columnconfigure(0, weight=1)

lbl_name_game = tk.Label(frame,text="MUSICAL QUIZ",font=("lexend",30,"bold"),fg="black",bg="#FFFFFF")
lbl_name_game.grid(row=0,column=0,padx=5,pady=30)

lbl_nameplayers = tk.Label(frame,text="Inform the players' names:",width=25,font=("Arial",14),fg="black",bg="#FFFFFF")
lbl_nameplayers.grid(row=1,column=0,padx=5,pady=30)

entry_player1 = tk.Entry(frame,justify="center",font=("lexend",14),width=30)
entry_player1.grid(row=2,column=0,padx=5,pady=30,)

entry_player2 = tk.Entry(frame,justify="center",font=("lexend",14),width=30)
entry_player2.grid(row=3,column=0,padx=5,pady=30)

lbl_rounds = tk.Label(frame,text="number of rounds:",width=20,font=("lexend",14),fg="black",bg="#FFFFFF")
lbl_rounds.grid(row=4,column=0,padx=5,pady=10)

entry_rounds = tk.Entry(frame,justify="center",font=("lexend",14))
entry_rounds.grid(row=5,column=0,padx=5,pady=30)

bt_alttema = tk.Button(frame, text="Alterar Tema", bg="#0F02C3", fg="white",
                 font=("lexend", 14, "bold"),height=2,width=30,command=toggle_theme)
bt_alttema.grid(row=6, column=0, padx=5, pady=30)

bt_start = tk.Button(frame, text="Iniciar Jogo", bg="#0F02C3", fg="white",
                 font=("lexend", 14, "bold"),command=starting_the_game,height=2,width=30)
bt_start.grid(row=7, column=0, padx=5, pady=30)



root.mainloop()
