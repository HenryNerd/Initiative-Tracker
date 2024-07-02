import tkinter as tk
from tkinter import simpledialog

class PlayerCycleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Initiative Tracker")
        self.root.geometry("400x300")
        self.root.minsize(300, 200)
        self.root.configure(bg="#f0f0f0")

        self.players = []
        self.current_index = 0
        self.round = 1

        self.label_round = tk.Label(root, text=f"Round {self.round}", font=("Helvetica", 24, "bold"), bg="#f0f0f0", fg="#333333")
        self.label_round.pack(pady=20)

        self.label = tk.Label(root, text="", font=("Helvetica", 20), bg="#f0f0f0", fg="#555555")
        self.label.pack(pady=10)

        self.button_next = tk.Button(root, text="Next Player", bg="#4CAF50", fg="white", font=("Helvetica", 16, "bold"), command=self.next_player)
        self.button_next.pack(pady=20, fill=tk.X, padx=30)

        self.button_reset = tk.Button(root, text="Reset", bg="#F44336", fg="white", font=("Helvetica", 12, "bold"), command=self.reset_setup)
        self.button_reset.pack(side=tk.RIGHT, pady=10, padx=10, anchor="se")

        self.init_players()

    def init_players(self):
        self.players = []
        self.current_index = 0
        self.round = 1
        self.label_round.config(text=f"Round {self.round}")

        playercount = simpledialog.askinteger("Input", "How many players (1-6)", minvalue=1, maxvalue=6)
        if not playercount:
            self.root.destroy()
            return

        for i in range(playercount):
            player_name = simpledialog.askstring("Input", f"Player {i + 1} Name")
            if player_name:
                self.players.append(player_name)
            else:
                self.root.destroy()
                return

        self.label.config(text=self.players[self.current_index])

    def next_player(self):
        if not self.players:
            return

        self.current_index = (self.current_index + 1) % len(self.players)
        if self.current_index == 0:
            self.round += 1
            self.label_round.config(text=f"Round {self.round}")

        self.label.config(text=self.players[self.current_index])

    def reset_setup(self):
        self.init_players()

if __name__ == "__main__":
    root = tk.Tk()
    app = PlayerCycleApp(root)
    root.mainloop()
