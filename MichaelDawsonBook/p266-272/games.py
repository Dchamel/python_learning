class Player(object):
    '''Player'''

    def __init__(self, name, score=0):
        self.name = name
        self.score = score

    def __str__(self):
        rep = self.name + ':\t' + str(self.score)
        return rep


def ask_yes_no(question):
    '''Ask Yes/No Question'''
    response = None
    while response not in ('y', 'n', 'yes', 'no'):
        response = input(question).lower()
    return response


def ask_number(question, low, high):
    '''Ask Number from special range'''
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response


if __name__ == '__main__':
    print('You try to run this module Directly, without Import')
    input('Press Any key for Exit')
