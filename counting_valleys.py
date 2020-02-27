

n = 8
s = 'DDUUDDUDUUUD'


def countLetter(s, l):
    return sum(map(lambda x: 1 if l in x else 0, s))


def countingValleys(n, s):

    elevation = 0

    hill_count = 0

    for letter in range(len(s)):
        if s[letter] == 'U':
            elevation += 1
        if s[letter] == 'D':
            elevation -= 1

        try:
            if elevation == -1 and s[letter+1] == 'U':
                # print('climbed a valley')
                hill_count += 1
        except IndexError:
            # print('error')
            pass

    return hill_count


countingValleys(n, s)
