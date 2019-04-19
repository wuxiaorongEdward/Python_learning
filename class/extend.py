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

class BackenedProgrammer(Programmer):

        def __init__(self, name, age, weight, language):
                super(BackenedProgrammer, self).__init__(name, age, weight)
                self.language = language


if __name__ == "__main__":
        programmer = BackenedProgrammer("Bob", 21, 80, "Python")
        print(dir(programmer))
        print(programmer.__dict__)
        print(type(programmer))
        print(isinstance(programmer, Programmer))
        print(isinstance(programmer, BackenedProgrammer))
