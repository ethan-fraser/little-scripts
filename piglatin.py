#! python3

'''
    Pig Latin Translator
Takes an input string and converts it to Pig Latin

'''

VOWELS = ('a','e','i','o','u')
CONSONANTS = ('b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z')

def translate(phrase):
    '''Translates a given phrase to pig latin and returns it'''
    
    phrase = phrase.lower()

    if not all(c.isalpha() or c.isspace() for c in phrase):
        print('Please enter a word or phrase consisting only of alphabetic characters (no punctuation)')
        return 0
    words = phrase.strip().split()
    for word in range(len(words)):
        word_l = list(words[word])
        
        if len(word_l) == 1 and word_l[0] in CONSONANTS:
            continue
        elif word_l[0] in VOWELS:
            words[word] += '-way'
        elif word_l[0] in CONSONANTS:
            first = word_l.pop(0)
            words[word] = ''.join(word_l) + '-' + first + 'ay'

    return ' '.join(words)

if __name__ == '__main__':
    while True:
        phrase = input('\n\nEnter a phrase to be translated: ')
        translated = translate(phrase)
        if not translated == 0: print(translated)

        if input("\nAgain? (y/n) ").lower() == 'n': break
    
    input('\nPress enter to quit.')
        
        