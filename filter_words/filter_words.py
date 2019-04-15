class Input(object):
        """
           敏感词替换
        """
        def __init__(self):
                self.filtered_words = list()
                self.in_string = ""
                self.out_string = "Human Rights"
                self.load_filtered_words()

        def load_filtered_words(self, filename="filter_words.txt"):
              with open(filename, "r", encoding='utf-8') as f:
                      for line in f.readlines():
                              self.filtered_words.append(line.strip())

        def filter_words(self):
                self.out_string = self.in_string
                for word in self.filtered_words:
                        if word in self.out_string:
                                self.out_string = self.out_string.replace(word, len(word) * "*")

        def user_input(self):
                self.in_string = input(">")

        def std_output(self):
                self.filter_words()
                print(self.out_string)


if __name__ == '__main__':
        user = Input()
        user.user_input()
        user.std_output()
