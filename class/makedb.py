from person import Person
import shelve

bob = Person("Bob Smith", job = "Manager", pay = 10000)
sue = Person("Sue Jones")

db = shelve.open("persondb")
for obj in (bob, sue):
        db[obj.name] = obj
db.close()

db = shelve.open("persondb")
for key in db.keys():
        person = db[key]
        print(person)

db.close()
