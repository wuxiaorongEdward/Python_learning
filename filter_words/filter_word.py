class Input(object):
    """  
	输入词语，找出是否存在文件中，找到返回查找的词, 否则返回Not existed
	"""
	
    def __init__(self):
	    self.filtered_words = []
	    self.in_string = ""
	    self.out_string = "Human Rigths, Not existed"
	    self.load_filtered_words()   # 类初始化时自动执行了把文件内的单词加载带 self.filtered_words 的列表中
		
    def load_filtered_words(self, filename="filter_words.txt"):
	    with open(filename, "r", encoding="utf-8") as f:
		    for line in f.readlines():
			    self.filtered_words.append(line.strip())
				
    def filter_words(self):
	    for word in self.filtered_words:
		    if self.in_string.find(word) != -1:
			    self.out_string = word + " founded "
			    return
				
    def user_input(self):
	    self.in_string = input("user input <quit to exit> ->")
		
    def std_output(self):
	    self.filter_words()
	    print(self.out_string)
	    self.out_string = "Human Rigths, Not existed"
	    
    def search_word(self):
        while True:
            self.user_input()
            if self.in_string == "quit":
                print("welcome again...")
                break
            self.std_output()
		
if __name__ == "__main__":
    user = Input()
    user.search_word()
    
