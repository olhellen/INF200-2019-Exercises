def char_counts(textfilename):
    with open(textfilename, 'r') as file:
        txt = file.read()
        results = [0] * 256
        for letter in txt:
            ind = ord(letter)
            if ind not in results:
                results[ind] += 1
        return results


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
