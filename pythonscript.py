import logging


class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname


def print_person(person):
    if not person:
        return None
    else:
        return "{0} {1}".format(person.firstname, person.lastname)


p = Person("John", "Doe")

print("first name of the object just created is {0}".format(p.firstname))

print("using function: {0}".format(print_person(p)))
