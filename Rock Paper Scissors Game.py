import random
import tkinter as tr
from tkinter import messagebox as mb


def determine_winner(user_choice, computer_choice):
    global ties
    if user_choice == computer_choice:
        ties += 1
        return "It's a tie!"
    elif( (user_choice == 'Rock' and computer_choice == 'Scissors') or (user_choice == 'Paper' and computer_choice == 'Rock') or (user_choice == 'Scissors' and computer_choice == 'Paper') ):
        return "You win!"
    else:
        return "Computer wins!"

#play
def play(user_choice):
    global rounds_played, user_score, computer_score, ties

    computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])
    result = determine_winner(user_choice, computer_choice)
    mb.showinfo("Result", f"You chose: {user_choice}\nComputer chose: {computer_choice}\n{result}")

    if result == "You win!":
        user_score += 1
    elif result == "Computer wins!":
        computer_score += 1

    rounds_played += 1
    if rounds_played >= total_rounds:
        end_game()

def end_game():
    global user_score, computer_score, rounds_played, ties
    if user_score > computer_score:
        winner = "You win the game!"
    elif computer_score > user_score:
        winner = "Computer wins the game!"
    else:
        winner = "It's a tie game!"

    play_again = mb.askyesno("Game Over", f"{winner}\nUser Score: {user_score}\nComputer Score: {computer_score}\nTies: {ties}\nDo you want to play again?")
    
    if play_again:
        reset_game()
    else:
        root.quit()

#reset game
def reset_game():
    global rounds_played, user_score, computer_score, ties
    rounds_played = 0
    user_score = 0
    computer_score = 0
    ties = 0
    rock_button.config(state=tr.NORMAL)
    paper_button.config(state=tr.NORMAL)
    scissors_button.config(state=tr.NORMAL)

#rounds
def update_total_rounds():
    global total_rounds
    total_rounds = game_mode_var.get()
    enable_game_buttons()

#game mode
def enable_game_buttons():
    rock_button.config(state=tr.NORMAL)
    paper_button.config(state=tr.NORMAL)
    scissors_button.config(state=tr.NORMAL)

#main window
root = tr.Tk()
root.title("Rock, Paper, Scissors Game")
root.configure(bg="black") 
button_width = 15
button_height = 2

rock_button = tr.Button(root, text="Rock", command=lambda: play("Rock"), width=button_width, height=button_height, state=tr.DISABLED)
paper_button = tr.Button(root, text="Paper", command=lambda: play("Paper"), width=button_width, height=button_height, state=tr.DISABLED)
scissors_button = tr.Button(root, text="Scissors", command=lambda: play("Scissors"), width=button_width, height=button_height, state=tr.DISABLED)

game_mode_var = tr.IntVar()
single_match = tr.Radiobutton(root, text="Single Match", variable=game_mode_var, value=1, command=update_total_rounds)
best_of_3 = tr.Radiobutton(root, text="Best of 3 Rounds", variable=game_mode_var, value=3, command=update_total_rounds)
best_of_5 = tr.Radiobutton(root, text="Best of 5 Rounds", variable=game_mode_var, value=5, command=update_total_rounds)

button_font = ('Calibri', 18)
button_text_color = "white"
button_bg_color = "gray"
rock_button.configure(font=button_font, fg=button_text_color, bg=button_bg_color)
paper_button.configure(font=button_font, fg=button_text_color, bg=button_bg_color)
scissors_button.configure(font=button_font, fg=button_text_color, bg=button_bg_color)

rock_button.pack(pady=10)
paper_button.pack(pady=10)
scissors_button.pack(pady=10)

single_match.pack()
best_of_3.pack()
best_of_5.pack()

# Initialize game variables
rounds_played = 0
user_score = 0
computer_score = 0
ties = 0
total_rounds = 1 

root.mainloop()
