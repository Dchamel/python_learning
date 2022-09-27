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
    global questionScore
    category = nextLine(file)
    question = nextLine(file)
    answers = []
    for i in range(4):
        answers.append(nextLine(file))
    correct = nextLine(file)
    questionScore = nextLine(file)
    if questionScore != '':
        questionScore = int(questionScore)
    else:
        questionScore = 0
    explanation = nextLine(file)
    return category, question, answers, correct, questionScore, explanation

def welcome(title):
    '''Welcomes Player'''
    print('Welcome to the Trivia game\n')
    print(f'\t\t{title}\n')

def main():
    global questionScoreAll
    file = openFile('trivia.txt', 'r')
    title = 'Let`s the battle begin!'
    welcome(title)
    playerName = input('Input your name: ')
    score = 0
    category, question, answers, correct, questionScore, explanation = nextBlock(file)
    while category:
        print(category)
        print(question)
        for i in range(4):
            print(f'\t{i+1} - {answers[i]}')
        answer = input('Input your suggestion(Number): ')
        if answer == correct.strip():
            print('You`re right !')
            score += questionScore
        else:
            print('You`re wrong')
        print(explanation)
        print(f'Score: {score}\n')
        questionScoreAll += questionScore
        category, question, answers, correct, questionScore, explanation = nextBlock(file)
    file.close()
    print('It was the last question !')
    if questionScoreAll == score:
        print(f'You`re winner ! Score is: {score}')
    else:
        print(f'You loose ! You`re score is: {score} But should be: {questionScoreAll}')
    return playerName, score


questionScore = 0
questionScoreAll = 0
playerName, score = main()
gameData = {str(playerName), str(score)}
print(gameData)
with open('score_storage.txt','a', encoding='utf-8') as file:
    file.writelines(gameData)
    file.write('\n')
input('Press Enter for Exit')