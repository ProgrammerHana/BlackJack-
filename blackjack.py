import random

class Blackjackgame:
    def __init__(self):
        self.deck = self.create_deck()
        self._player_hand = []
        self._dealer_hand = []
        self.deal_card(self._player_hand,False)
        self.deal_card(self._player_hand,False)
        self.deal_card(self._dealer_hand,False)
        self.deal_card(self._dealer_hand,True)

    def create_deck(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        suits = ['hearts', 'diamonds', 'clubs', 'spades']
        deck = [{'rank': rank, 'suit': suit , 'hidden':False} for rank in ranks for suit in suits]
        random.shuffle(deck)
        return deck

    def deal_card(self,hand,is_second_card):
        card = self.deck.pop()
        card['hidden'] = is_second_card
        hand.append(card)

    def calculate_score(self,hand):
        score = sum(self.card_value(card['rank'])for card in hand)
        num_aces = sum(1 for card in hand if card['rank'] == 'A')
        while score > 21 and num_aces:
            score -= 10
            num_aces -= 1
        return score
    def card_value(self,rank):
        if rank in ['K', 'Q', 'J']:
            return 10
        elif rank == 'A':
            return 11
        else:
            return int(rank)

    def has_ace(self,hand):
        for card in hand:
            if card['rank'] == 'A':
                return True
        else: return False

        # Getter method for player_hand
    def get_player_hand(self):
        #print(self._player_hand)
        return self._player_hand

    # Getter method for dealer_hand
    def get_dealer_hand(self):
        #print(self._dealer_hand)
        return self._dealer_hand

    def set_dealer_hand(self):
        self._dealer_hand