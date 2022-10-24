import unittest
from time import perf_counter

t1 = perf_counter()


# Cards v3.0
class Card(object):
    '''One Card'''
    RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    # c - clubs(крести),d - diamonds(буби), h - hearts(червы), s - spades(пики)
    SUITS = ['c', 'd', 'h', 's']

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


class Deck(Hand):
    '''Deck of playing cards'''

    def populate(self):
        self.cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self, hands, perHand=1):
        for rounds in range(perHand):
            for hand in hands:
                if self.cards:
                    topCard = self.cards[0]
                    self.give(topCard, hand)
                else:
                    print('Can\'t deal cards anymore. The cards are over.')


class UnprintableCard(Card):
    '''A Card that won't reveal its rank or suit when printed.'''

    def __str__(self):
        return 'Unprintable Card'


class PositionableCard(Card):
    '''A card that can be placed face up or down.'''

    def __init__(self, rank, suit, isfaceUp=True):
        super(PositionableCard, self).__init__(rank, suit)
        self.isFaceUp = isfaceUp

    def __str__(self):
        if self.isFaceUp:
            rep = super(PositionableCard, self).__str__()
        else:
            rep = 'XX'
        return rep

    def flip(self):
        self.isFaceUp = not self.isFaceUp


#Test Section
class AllTestsCards(unittest.TestCase):

    def setUp(self):
        pass

    def test_Card(self):
        actual = Card(rank='A', suit='c')
        self.assertEqual(actual.__str__(), 'Ac')

    def test_Hand(self):
        hand_test = Hand()
        hand_test.add(card1)
        hand_test.add(card2)
        actual = hand_test.__str__().strip()
        self.assertEqual(actual, 'Ac 2c')

    def test_Deck_populate(self):
        deck_test = Deck()
        deck_test.populate()
        actual = len(deck_test.cards)
        self.assertEqual(actual, 52)

    def test_Deck_deal(self):
        deck_test = Deck()
        deck_test.populate()
        hand_test1 = Hand()
        hand_test2 = Hand()
        hands_test = [hand_test1, hand_test2]
        deck_test.deal(hands_test, perHand=4)

        actual1 = hand_test1.__str__().strip()
        self.assertEqual(actual1, 'Ac 3c 5c 7c')

        actual2 = hand_test2.__str__().strip()
        self.assertEqual(actual2, '2c 4c 6c 8c')

    def test_PositionableCard(self):
        test_card = PositionableCard('Q','s')

        self.assertEqual(test_card.__str__(), 'Qs')

        test_card.isFaceUp = False
        self.assertEqual(test_card.__str__(), 'XX')


card1 = Card('A','c')
card2 = UnprintableCard('A','d')
card3 = PositionableCard('A','h')
card3.isFaceUp = False
print(card3)


card1 = Card(rank='A', suit='c')
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

deck1 = Deck()
deck1.populate()
# deck1.shuffle()
print(f'New Card Deck has been created:\n{deck1}')
myHand = Hand()
yourHand = Hand()
hands = [myHand, yourHand]
deck1.deal(hands, perHand=5)
deck1.clear()
print(deck1)
print('All cards have been dealt')
print(f'My Hand: {myHand}\nYour Hand: {yourHand}')

t2 = perf_counter()
print(f'{t2 - t1:.5f} sec')
