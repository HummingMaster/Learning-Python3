user_words = input("Enter your word: ")


def rev(word):
    rev_word_list = word.split()
    rev_word = ' '.join(rev_word_list[::-1])
    print(rev_word)

rev(user_words)


