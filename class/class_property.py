class Programmer(object):
        hobby = "Play Computer"

        def __init__(self, name, age, weight):
                self.name = name
                self._age = age
                self.__weight = weight

        def get_weight(self):
                return self.__weight


if __name__ == "__main__":
        programmer = Programmer("Bob", 25, 80)
        print(dir(programmer))
        print(programmer.__dict__)   # 构造函数的键值对
        print(programmer.get_weight())
        print(programmer._Programmer__weight)   # 变相的是由属性访问
