def ask_number(question, low, high, step=1):
    '''ask user for number in range, return - integer'''
    response = ''
    while response not in range(low, high, step):
        response = int(input(question))
    return response

print(ask_number('qqq: ', 1, 10, 2))
