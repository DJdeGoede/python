
class Person:
    def __init__ (self, name, age, pay=0, job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job

    def __str__ (self):
        return 'Name: %s, Age: %s, Pay: %s, Job: %s' % (self.name, self.age, self.pay, self.job)

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)

class Manager(Person):
    def __init__ (self, name, age, pay):
        Person.__init__(self, name, age, pay, 'manager')

    def giveRaise(self, percent, bonus=0.1):
        self.pay *= (1.0 + percent + bonus)

if __name__ == '__main__':
    bob = Person('Bob Smith', 42, 30000, 'software')
    sue = Person('Sue Jones', 45, 40000, 'hardware')
    tom = Manager('Tom Doe', 50, 40000)

    print(bob.name, sue.pay)
    print(bob.lastName())
    
    sue.giveRaise(.10)
    tom.giveRaise(.20)

    print(sue.pay)
    print(tom.pay)
    print(tom.lastName())   # inherits def from Person class

    print(bob)
    print(tom)
