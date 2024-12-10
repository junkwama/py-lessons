import random

# ranks = [     
    # {'rank': 'A', 'value': 11}, {'rank': '2', 'value': 2}, {'rank': '3', 'value': 3}, {'rank': '4', 'value': 4},  
    # {'rank': '5', 'value': 5},  {'rank': '6', 'value': 6},  {'rank': '7', 'value': 7},  {'rank': '8', 'value': 8},  
    # {'rank': '9', 'value': 9}, {'rank': '10', 'value': 10}, {'rank': 'J', 'value': 10}, {'rank': 'Q', 'value': 10}, 
    # {'rank': 'K', 'value': 10} 
# ]

class Deck:

    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal(self, n):
        cards_dealt = []
        if len(self.cards):
            for i in range(n):
                cards_dealt.append(self.cards.pop())
        return cards_dealt

    def __init__(self):

        _ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.ranks = [{"rank": n, "value": 11 if n == "A" else 10 if n in ["J", "Q", "K"] else int(n)} for n in _ranks]
        self.suits = ["spades", "clubs", "hearts", "diamonds"]
        self.cards = []

        for suit in self.suits:
            for rank in self.ranks:
                self.cards.append(( suit, rank ))
    
deck1 = Deck()
deck1.shuffle()


cards_dealt = d.deal(2)
card = cards_dealt[0]
print(card)