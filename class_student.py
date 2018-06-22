class Student(object):
     def __init__(self, name,gender,score):
          self.__name = name
          self.__score = score
          self.__gender = gender
     def get_score(self):
           if self.__score >= 90:
                 return 'A'
           elif self.__score > 70:
                 return 'B'
           elif self.__score >= 60:
                 return 'C'
           else :
                 return 'D'
     def get_gender(self):
           return self.__gender
     def set_gender(self, gender):
            self.__gender = gender

     def get_name(self):
          return self.__name
     def set_name(self, name):
          self.__name = name

     def print_score(self):
           print("{} : {}".format(self.__name, self.get_score()))

wu = Student('wuxiaorong', 'male', 90)
wu.__name = 'wusad'
print(wu.get_name())
wu.set_name('xiaorong')
wu.print_score()

if wu.get_gender() != 'male':
        print('fail !')
else:
     wu.set_gender('female')
     if wu.get_gender() != "female":
        print('fail')
     else : 
           print("success !")
