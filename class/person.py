class Person(object):

        def __init__(self, name, job = None, pay = 0):
                self.name = name
                self.job = job
                self.pay = pay

        def lastName(self):
                return self.name.split()[-1]

        def giveRaise(self, percent):
                return int(self.pay * (1 + percent))

        def __str__(self):
                return "{0} ---> {1} ---> {2}".format(self.name, self.job, self.pay)


class Manager(Person):
        def giveRaise(self, percent, bonus = 0.1):
                return Person.giveRaise(self, percent + bonus)
                

if __name__ == "__main__":
    bob = Person("Bob Smith")
    print(bob.name)
    sue = Person("Sue Jone", job = "dev", pay = 10000)
    print("{0}'s job is {1}, and gets pay {2}".format(sue.name, sue.job, sue.pay))
    print("last name {}".format(sue.lastName()))
    print("Now, {0}'s job is {1}, and gets pay {2}".format(sue.name, sue.job, sue.giveRaise(0.1)))
    print(sue)

    print("*" * 20)
    tom = Manager("Tom", "manager", 10000)
    tom.pay = tom.giveRaise(0.1)
    print(tom)
    print(tom.__class__.__name__)
    # print(tom.__bases__)
    print(tom.__dict__)
    print(tom.__dict__.keys())
