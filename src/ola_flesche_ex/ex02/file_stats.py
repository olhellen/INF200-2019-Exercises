def char_counts(textfilename):
    file = open('textfilename', 'r')
    results = [None] * 256
    for letter in file:
        results[ord(letter)] += 1
    return results
    file.close()


if __name__ == '__main__':

    filename = 'file_stats.py'
    frequencies = char_counts(filename)
    for code in range(256):
        if frequencies[code] > 0:
            character = ''
            if code >= 32:
                character = chr(code)

            print(
                '{:3}{:>4}{:6}'.format(
                    code, character, frequencies[code]
                )
            )
