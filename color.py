from termcolor import colored

COLOR = {
    'TP': 'green',
    'TN': 'black',
    'FP': 'red',  # Type 1 Error
    'FN': 'magenta',  # Type 2 Error
}


def coloring(word, true, predict):
    if true == 'O':
        if predict == 'O':
            print(word, end=' ')
        elif predict == 'B-KP':
            print(colored(word, COLOR['FP']), end=' ')
        else:
            print(colored(word, COLOR['FP']), end=' ')
    elif true == 'B-KP':
        if predict == 'O':
            print(colored(word, COLOR['FN']), end=' ')
        elif predict == 'B-KP':
            print(colored(word, COLOR['TP']), end=' ')
        else:
            print(colored(word, COLOR['TP']), end=' ')
    else:
        if predict == 'O':
            print(colored(word, COLOR['FN']), end=' ')
        elif predict == 'B-KP':
            print(colored(word, COLOR['TP']), end=' ')
        else:
            print(colored(word, COLOR['TP']), end=' ')
