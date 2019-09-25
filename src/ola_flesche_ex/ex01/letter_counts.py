
def letter_freq(txt):
    lett = [bok.lower() for bok in txt]
    lett.sort()
    coun = []
    for n in lett:
        coun.append(lett.count(n))
        dictio = dict(zip(lett, coun))
    return dictio


if __name__ == '__main__':
    text = input('Please enter text to analyse: ')

    frequencies = letter_freq(text)
    for letter, count in frequencies.items():
        print('{:3}{:10}'.format(letter, count))
