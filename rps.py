import tkinter as tk
import random

class RockPaperScissorsApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Rock, Paper, Scissors")

        self.label_instruction = tk.Label(master, text="Choose rock, paper, or scissors:")
        self.label_instruction.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        self.button_rock = tk.Button(master, text="Rock", command=lambda: self.play("rock"))
        self.button_rock.grid(row=1, column=0, padx=10, pady=10)

        self.button_paper = tk.Button(master, text="Paper", command=lambda: self.play("paper"))
        self.button_paper.grid(row=1, column=1, padx=10, pady=10)

        self.button_scissors = tk.Button(master, text="Scissors", command=lambda: self.play("scissors"))
        self.button_scissors.grid(row=1, column=2, padx=10, pady=10)

        self.result_label = tk.Label(master, text="")
        self.result_label.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

        self.history_label = tk.Label(master, text="Last Five Games:")
        self.history_label.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

        self.history_text = tk.Text(master, height=5, width=40, state=tk.DISABLED)
        self.history_text.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

        self.user_score = 0
        self.computer_score = 0
        self.round_number = 1
        self.max_rounds = 3
        self.history = []

    def play(self, user_choice):
        choices = ['rock', 'paper', 'scissors']
        computer_choice = random.choice(choices)

        result = self.determine_winner(user_choice, computer_choice)
        self.update_score(result)
        self.update_history(user_choice, computer_choice, result)

        if self.round_number == self.max_rounds:
            self.display_final_result()
        else:
            self.result_label.config(text=f"Round {self.round_number}: You chose {user_choice}. Computer chose {computer_choice}. {result} \nYour Score: {self.user_score}, Computer's Score: {self.computer_score}")
            self.round_number += 1

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            return "You win!"
        else:
            return "Computer wins!"

    def update_score(self, result):
        if "You win" in result:
            self.user_score += 1
        elif "Computer wins" in result:
            self.computer_score += 1

    def update_history(self, user_choice, computer_choice, result):
        self.history.append((user_choice, computer_choice, result))
        if len(self.history) > 5:
            self.history.pop(0)  # Remove the oldest game

    def display_final_result(self):
        if self.user_score > self.computer_score:
            winner = "You"
        elif self.user_score < self.computer_score:
            winner = "Computer"
        else:
            winner = "It's a tie"

        self.result_label.config(text=f"Game Over! {winner} wins.\nYour Score: {self.user_score}, Computer's Score: {self.computer_score}")
        self.update_history_text()

    def update_history_text(self):
        self.history_text.config(state=tk.NORMAL)
        self.history_text.delete('1.0', tk.END)
        for game in self.history:
            self.history_text.insert(tk.END, f"User: {game[0]}, Computer: {game[1]}, Result: {game[2]}\n")
        self.history_text.config(state=tk.DISABLED)

def main():
    root = tk.Tk()
    app = RockPaperScissorsApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
