from Model import User


def addUserToDatabase(user):
    user.write_to_file()


class Manager:

    def __init__(self, name, age, salary, bonus):
        self.name = name
        self.age = age
        self.salary = salary
        self.bonus = bonus

    def get_total_salary(self):
        return self.salary + self.bonus
