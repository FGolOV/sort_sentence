def sort_sentence(sentence):
    lowercase_letters=sentence.lower()
    l= lowercase_letters.split()
    sorted_sentence = ""
    for i in sorted(l, key=lambda a: len(a)):
        sorted_sentence = sorted_sentence + " " + i
    word1=sorted_sentence.split()[0]
    word_1_with_a_capital_letter=''.join(word1.upper()[:1]+word1[1:])
    other_words=' '.join(sorted_sentence.split()[1:])
    all_words= word_1_with_a_capital_letter+' '+ other_words
    return all_words

if __name__ == '__main__':
    sentence=str(input("Введите строку с большой буквы и без знаков препинания"))
    print(sort_sentence(sentence))


