
from collections import Counter


txt_file = open('cat in the hat.txt', 'r')
txt = txt_file.read()
txt = txt.lower()
all_words = txt.split()
all_words = [word.strip(" '.,!?") for word in all_words]
all_words.sort()
counter = Counter(all_words)

unq = set(all_words)


for i in unq:

    print(i, "appears" , counter[i])


class StringStat:
    
    def __init__(self):
        pass

    def return_stats(self):
        pass
    


