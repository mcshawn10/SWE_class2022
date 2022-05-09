
from collections import Counter
import unittest
from Test import TestStringStat



class StringStat:
    
    def __init__(self, path):
        self.path = path

    def return_stats(self):
        txt_file = open(self.path, 'r')

        TestStringStat().test_return_stats(self.path) # unit test


        txt = txt_file.read()
        txt = txt.lower()
        all_words = txt.split()
        all_words = [word.strip(" '.,!?") for word in all_words]
        all_words.sort()
        counter = Counter(all_words)
        unq = set(all_words)

        for i in unq:

            print(i, "appears" , counter[i])

    def replace_word(self, word, replacement):


        TestStringStat().test_replace_word(word, self.path) # unit test

        with open(self.path, 'r') as file :
            new_txt = file.read()

        
        new_txt = new_txt.replace(word, replacement)

        
        with open('file.txt', 'w') as file:
            file.write(new_txt)

    def grepline(self, word):

        TestStringStat().test_replace_word(word, self.path) # unit test

        input_file = open(self.path, 'r')
        index = 0
        i = 1
        line_occurence = []

        for line in input_file.readlines():
            
            
            if word in line:
                
                line_occurence.append(i)
            i+=1

        print(word, "appears on lines: ", line_occurence)
        

        



if __name__ == '__main__':
    test = StringStat('cat in the hat.txt')

    #test.return_stats() # requirement 1


    #test.replace_word("cat", "dog") #requirement 2


    test.grepline("dog") #requirement 3
    
    

