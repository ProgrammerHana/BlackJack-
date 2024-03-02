import tkinter as tk
from tkinter import messagebox
from blackjack import Blackjackgame
import time

class BlackjackGUI:
    def __init__(self,root):
        self.root = root
        self.root.title("BlackJack Game")

        self.game = Blackjackgame()

        self.player_label = tk.Label(root, text="Player Hand:")
        self.player_label.pack()
        self.player_hand_label = tk.Label(root, text="")
        self.player_hand_label.pack()

        self.dealer_label = tk.Label(root, text="Dealer Hand:")
        self.dealer_label.pack()
        self.dealer_hand_label = tk.Label(root, text="")
        self.dealer_hand_label.pack()

        self.hit_button = tk.Button(root, text="Hit", command=self.hit)
        self.hit_button.pack()

        self.stand_button = tk.Button(root, text="Stand", command=self.stand)
        self.stand_button.pack()


        self.update_ui()


    def hit(self):
        self.game.deal_card(self.game.get_player_hand(),False)
        self.update_ui()
        player_score = self.game.calculate_score(self.game.get_player_hand())
        if player_score>21:
            self.end_game("You busted, Dealer wins.")

    def stand(self):
        while self.game.calculate_score(self.game.get_dealer_hand())<17:
            self.game.deal_card(self.game.get_dealer_hand(),False)
            self.update_ui()
            time.sleep(2)

        self.determine_winner()


    def determine_winner(self):
        player_score = self.game.calculate_score(self.game.get_player_hand())
        dealer_score = self.game.calculate_score(self.game.get_dealer_hand())
        if dealer_score > 21 or player_score > dealer_score:
            self.end_game("Congrats, You won!")
        elif player_score < dealer_score:
            self.end_game("Dealer wins")
        else:
            self.end_game("It's a draw")

    def update_ui(self):
        player_hand_list = [card['rank'] for card in self.game.get_player_hand()]
        dealer_hand = self.game.get_dealer_hand()
        dealer_hand_list = [dealer_hand[0]['rank']]

        if dealer_hand[1]['hidden']:
            dealer_hand_list.append('Hidden Card')
            self.game.get_dealer_hand()[1]['hidden'] = False
        elif dealer_hand_list[-1] == 'Hidden Card':
            dealer_hand_list.pop()
            dealer_hand_list.append(dealer_hand[2]['rank'])
        else:
            dealer_hand_list.append(dealer_hand[-1]['rank'])

        player_hand_str = ", ".join(player_hand_list)
        dealer_hand_str = ", ".join(dealer_hand_list)

        self.player_hand_label.config(text=f"Player Hand: {player_hand_str}")
        self.dealer_hand_label.config(text=f"Dealer Hand: {dealer_hand_str}")

    def end_game(self, message):
        messagebox.showinfo("Game Over", message)
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    gui = BlackjackGUI(root)
    root.mainloop()