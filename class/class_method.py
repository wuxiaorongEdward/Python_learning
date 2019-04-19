# 函数和方法
# 函数可以直接调用， 方法是依附于对象的

class Programmer(object):
        hobby = "Play Computer"

        def __init__(self, name, age, weight):
                self.name = name
                self._age = age
                self.__weight = weight

        @classmethod
        def get_hobby(cls):
                return cls.hobby
        
        @property
        def get_weight(self):
                return self.__weight


if __name__ == "__main__":
        programmer = Programmer("Bob", 25, 80)
        print(dir(programmer))
        print(programmer.__dict__)   # 构造函数的键值对
        print(programmer.get_weight)  # method -> property
        print(Programmer.get_hobby())
        print(programmer.get_hobby())
