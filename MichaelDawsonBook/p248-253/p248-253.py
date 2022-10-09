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

class Hand(object):
    '''Hand - the cards in player's hand that he/she is available to play '''

    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ''
            for card in self.cards:
                rep += str(card) + ' '
        else:
            rep = 'Empty'
        return rep

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, otherHand):
        self.cards.remove(card)
        otherHand.add(card)

card1 = Card(rank='A', suit='c')
print(card1)
card2 = Card(rank='2', suit='c')
card3 = Card(rank='3', suit='c')
card4 = Card(rank='4', suit='c')
card5 = Card(rank='5', suit='c')

myHand = Hand()
myHand.add(card1)
myHand.add(card2)
myHand.add(card3)
myHand.add(card4)
myHand.add(card5)
print(myHand)

yourHand = Hand()
myHand.give(card2, yourHand)
myHand.give(card4, yourHand)
print(myHand)
print(yourHand)

myHand.clear()
print(myHand)