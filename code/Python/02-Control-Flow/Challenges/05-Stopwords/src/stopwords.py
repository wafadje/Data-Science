"""
Select only the meaningful words in a sentence.
"""

def main():
    sentence = ("Why is it always the innocents who suffer most "
    "when you high Lords play your Game of Thrones")

    stopwords =  ['about', 'once', 'during', 'out', 'very', 'having', 'with', 'they', 'own',
    'an', 'be', 'some', 'for', 'do', 'its', 'yours', 'such', 'into', 'of',
    'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who', 'as',
    'from', 'him', 'each', 'the', 'themselves', 'until', 'below', 'are', 'we',
    'these', 'your', 'his', 'through', 'don', 'nor', 'me', 'were', 'her',
    'more', 'himself', 'this', 'down', 'should', 'our', 'their', 'while',
    'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all', 'no', 'when',
    'at', 'any', 'before', 'them', 'same', 'and', 'been', 'have', 'in', 'will',
    'on', 'does', 'yourselves', 'then', 'that', 'because', 'what', 'over',
    'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you', 'herself',
    'has', 'just', 'where', 'too', 'only', 'myself', 'which', 'those', 'i',
    'after', 'few', 'whom', 't', 'being', 'if', 'theirs', 'my', 'against', 'a',
    'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than']

    # TODO: split the sentence into a list of `words`
    words = sentence.split(" ")
    #print(words)

    # TODO: lowercase all the words in a single line of code
    lower_words = [word.lower() for word in words]
    print(lower_words)

    # TODO: remove stop words from your list to create `tokens` in a single line of code
    word_list = [word for word in lower_words for stopword in stopwords if word == stopword]
    print(word_list)

if __name__ == '__main__':
    main()
