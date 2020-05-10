"""
This is a module to test code review.
"""

class Person:
    """
    This class models a person with their firstname and lastname.
    """
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def __str__(self):
        return "{0}, {1}".format(self.firstname, self.lastname)

    def is_correct(self):
        """
        return is a person is correctly formed
        :return: true if all attributes are defined.
        """
        return self.firstname is not None and self.lastname is not None


def print_person(person):
    """
    Show the representation of a person as a string
    :param person: the person to print
    :return: a string that represent the person, None if not possible
    """
    if not person:
        return None
    return "{0} {1}".format(person.firstname, person.lastname)


p = Person("John", "Doe")

print("first name of the object just created is {0}".format(p.firstname))

print("using function: {0}".format(print_person(p)))
