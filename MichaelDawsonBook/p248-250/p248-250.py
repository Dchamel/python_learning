class Card(object):
    '''One Card'''
    RANKS = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    #c - clubs(крести),d - diamonds(буби), h - hearts(червы), s - spades(пики)
    SUITS = ['c','d','h','s']
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    def __str__(self):
        rep = self.rank + self.suit
        return rep
