
from collections import Counter



class StringStat:
    
    def __init__(self, path):
        self.path = path

    def return_stats(self):
        txt_file = open(self.path, 'r')
        txt = txt_file.read()
        txt = txt.lower()
        all_words = txt.split()
        all_words = [word.strip(" '.,!?") for word in all_words]
        all_words.sort()
        counter = Counter(all_words)
        unq = set(all_words)

        for i in unq:

            print(i, "appears" , counter[i])

    def replace_word(self):
        pass


