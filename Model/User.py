import os


class User:
    def __init__(self, Username='', Password='', Fullname='', Address='', phone_number='', email='', user_type=''):
        self.Username = Username
        self.Password = Password
        self.Fullname = Fullname
        self.Address = Address
        self.phone_number = phone_number
        self.email = email
        self.user_type = user_type

    def write_to_file(self, filename=os.path.join(os.path.dirname(os.path.dirname(__file__)), "Database\AMUser.txt")):
        #  check if UserName already exists in file
        if not self.read_from_file(filename):
            with open(filename, "a") as file:
                file.write(f"{self.Username},{self.Password},{self.Fullname},{self.Address},{self.phone_number},"
                           f"{self.email},{self.user_type}\n")
            return True
        else:
            return False

    def read_from_file(self, filename=os.path.join(os.path.dirname(os.path.dirname(__file__)), "Database\AMUser.txt")):
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                line = line.split(",")
                if line[0] == self.Username:
                    self.Password = line[1]
                    self.Fullname = line[2]
                    self.Address = line[3]
                    self.phone_number = line[4]
                    self.email = line[5]
                    self.user_type = line[6]
                    return True
            return False

    def readAllUsers(self, filename=os.path.join(os.path.dirname(os.path.dirname(__file__)), "Database\AMUser.txt")):
        data = []
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                line = line.split(",")
                user = User(line[0], line[1], line[2], line[3], line[4], line[5], line[6])
                data.append(user)
        return data

    def checkUsernameExists(self, filename=os.path.join(os.path.dirname(os.path.dirname(__file__)), "Database\AMUser"
                                                                                                    ".txt")):
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                line = line.split(",")
                if line[0] == self.Username:
                    return True
            return False

    def convertToList(self):
        return [self.Username, self.Password, self.Fullname, self.Address, self.phone_number, self.email, self.user_type]

    def convertToListForUser(self):
        return [self.Fullname, self.Address, self.phone_number, self.email]

    def __str__(self):
        return f"{self.Username},{self.Password},{self.Fullname},{self.Address},{self.phone_number},{self.email}," \
               f"{self.user_type} "


if __name__ == '__main__':
    model = User(Username='temp', Password='temp', Fullname='temp', Address='qwerty',
                 phone_number='123123',
                 email='temp@temp.com', user_type='Admin')
    # get directory of project and append Database/AMUser.txt to it
    print(model.write_to_file())
    # print(model.read_from_file())
    # model.write_to_file()
    # print(model.readAllUsers())
