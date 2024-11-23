class WordsFinder:

    def __init__(self,*file_name):
        self.file_name = file_name

    def get_all_words(self):
        all_words = {}
        text = []
        for file_name in self.file_name:
            with open(file_name, 'r', encoding='utf-8') as file:
                for string in file:
                    string = string.lower()
                    for s in string:
                        if s in [',', '.', '=', '!', '?', ';', ':', ' - ','\n']:
                            string = string.replace(s, '')
                    text.append(string.split(sep=' '))
        all_words[self.file_name] = [x for y in text for x in y]
        return all_words

    def find(self, word):
        dict_ = self.get_all_words()
        for name, words in dict_.items():
            for w in words:
                if word.lower() in w.lower():
                    index = int(words.index(w) + 1)
                    dict_[self.file_name] = index
                    break
        return dict_

    def count(self, word):
        dict_ = self.get_all_words()
        count = 0
        for name, words in dict_.items():
            for w in words:
                if word.lower() in w.lower():
                    count += 1
        dict_[self.file_name] = count
        return dict_

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего