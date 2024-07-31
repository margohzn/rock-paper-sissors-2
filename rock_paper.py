import tkinter as tk
import random

player_score = 0 
computor_score = 0 
options = [("rock", 0), ("paper", 1), ("scissors", 2)]

#fonction to select computor option
def get_computor_choice():
    return random.choice(options)

def get_player_choice(player_input):
    global player_score, computor_score
    computor_input = get_computor_choice
    print(computor_input)
    print(player_input)
    

    






window = tk.Tk()
window.title("Rock Paper Sicorss")
window.geometry("550x600")
window.configure(background = "white")

title = tk.Label(window, text = "Rock Paper Sicorss!", bg = "white", fg = "black", font = ("Helvetica", 35), bd = 3, pady = 5, relief = tk.RIDGE).pack(pady = 10)
winner_text = tk.Label(window, text = "", bg = "white", fg = "green", font = ("times", 20))

#top frame
option_frame = tk.Frame(window, borderwidth = 5, relief = tk.GROOVE)
option_frame.configure(background = "#641A5D")

choice_label = tk.Label(option_frame, text = "Your options:", bg = "#641A5D", fg = "black", font = ("times", 40)).pack()
rock_button = tk.Button(option_frame, text = "Rock").pack(pady = 5)
paper_button = tk.Button(option_frame, text = "Paper").pack(pady = 20)
scissors_button = tk.Button(option_frame, text = "Scissors").pack(pady = 5)

option_frame.pack(fill = tk.BOTH, expand = True, pady = 10, padx = 2)


#bottom frame
result_frame = tk.Frame(window, relief = tk.GROOVE, borderwidth = 3)
result_frame.configure(background = "#192581")

score_label = tk.Label(result_frame, text = "Score:", font = ("times", 40), bg = "#192581", fg = "black").pack(side = "left", anchor = tk.NW)
player_choice_label = tk.Label(result_frame, text = "You selected:", fg = "black", bg = "#192581", font = ("times", 20))
player_score_label = tk.Label(result_frame, text = "Player score:", fg = "black", bg = "#192581", font = ("times", 20))
computor_choice_label = tk.Label(result_frame, text = "Computor choice:", bg = "#192581", fg = "black", font = ("times", 20))
computor_score_label = tk.Label(result_frame, text = "Computor score:", fg = "black", bg = "#192581", font = ("times", 20))

player_choice_label.place(x = 10, y = 50)
player_score_label.place(x = 300, y = 50)
computor_choice_label.place(x = 10, y = 100)
computor_score_label.place(x = 300, y = 100)

result_frame.pack(fill = tk.BOTH, expand = True, padx = 10, pady = 2)

winner_text.pack()



window.mainloop()
