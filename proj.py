
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

    def replace_word(self, word, replacement):
        with open(self.path, 'r') as file :
            filedata = file.read()

        # Replace the target string
        filedata = filedata.replace(word, replacement)

        # Write the file out again
        with open('file.txt', 'w') as file:
            file.write(filedata)


test = StringStat('cat in the hat.txt')
test.return_stats()

