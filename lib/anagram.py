# your code goes here!
class Anagram:

    def __init__(self, word):

        self.word = word

        self.sorted_word = ''.join(sorted(word))


    def match(self, words_list):

        anagrams = []

        for word in words_list:

            if self.sorted_word == ''.join(sorted(word)):

                anagrams.append(word)

        return anagrams