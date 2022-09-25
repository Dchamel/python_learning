import sys
from time import perf_counter

def openFile(fileName, mode):
    '''Check\'n\'Open file'''
    try:
        file = open(fileName, mode)
    except IOError as errorMessage:
        print(f'Can\'t open the file - {fileName}\n'
              f'Program terminated.\n'
              f'SysMessage - {errorMessage}')
        input('Press Enter for Exit')
        sys.exit()
    else:
        return file

def nextLine(file):
    '''Read and prepare another string from the file'''
    line = file.readline()
    line = line.replace('/', '\n')
    return line

def nextBlock(file):
    '''Read another Block from the file'''
    category = nextLine(file)
    question = nextLine(file)
    answers = []
    for i in range(4):
        answers.append(nextLine(file))
    correct = nextLine(file)
    explanation = nextLine(file)
    return category, question, answers, correct, explanation

def welcome(title):
    '''Welcomes Player'''
    print('Welcome to the Trivia game\n')
    print(f'\t\t{title}\n')

def main():
    file = openFile('trivia.txt', 'r')
    title = 'Let`s the battle begin!'
    welcome(title)
    score = 0
    category, question, answers, correct, explanation = nextBlock(file)
    while category:
        print(category)
        print(question)
        for i in range(4):
            print(f'\t{i+1} - {answers[i]}')
        answer = input('Input your suggestion(Number): ')
        print(type(answer), answer)
        print(type(correct), correct)
        if answer == correct:
            print('You`re right !')
            score += 1
        else:
            print('You`re wrong')
        print(explanation)
        print(f'Score: {score}\n')
        category, question, answers, correct, explanation = nextBlock(file)
    file.close()
    print('It was the last question !')
    print(f'Your total score: {score}')

main()
input('Press Enter for Exit')


