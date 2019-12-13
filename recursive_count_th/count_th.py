'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    # check the length, if it's less than 2
    if len(word) < 2:
        return 0
    # remove the first th and increment the count
    elif word[:2] == 'th':
        return 1 + count_th(word[1:])
    # let the algo exit to base
    else:
        return count_th(word[1:])

    # TBC


print(count_th('eeeth'))
