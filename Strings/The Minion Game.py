def minion_game(string):
    vowel = 'aeiou'.upper()
    l = len(string)
    kevin_score = sum(l-i for i in range(l) if string[i]in vowel)
    stuart_score = l*(l+1) /2 - kevin_score
    if kevin_score == stuart_score:
        print('Draw')
    elif kevin_score>stuart_score:
        print('Kevin', int(kevin_score))
    else:
        print('Stuart',int(stuart_score))

if __name__ == '__main__':
    s = input()
    minion_game(s)