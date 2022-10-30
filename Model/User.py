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

    # @property
    # def username(self):
    #     return self.Username
    #
    # @username.setter
    # def username(self, username):
    #     self.Username = username
    #
    # @property
    # def password(self):
    #     return self.Password
    #
    # @password.setter
    # def password(self, password):
    #     self.Password = password
    #
    # @property
    # def fullname(self):
    #     return self.Fullname
    #
    # @fullname.setter
    # def fullname(self, fullname):
    #     self.Fullname = fullname
    #
    # @property
    # def address(self):
    #     return self.Address
    #
    # @address.setter
    # def address(self, address):
    #     self.Address = address
    #
    # @property
    # def phone_number(self):
    #     return self.phone_number
    #
    # @phone_number.setter
    # def phone_number(self, phone_number):
    #     self.phone_number = phone_number
    #
    # @property
    # def email(self):
    #     return self.email
    #
    # @email.setter
    # def email(self, email):
    #     self.email = email
    #
    # @property
    # def user_type(self):
    #     return self.user_type
    #
    # @user_type.setter
    # def user_type(self, user_type):
    #     self.user_type = user_type

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
                print(line)
        return data


if __name__ == '__main__':
    model = User(Username='zaeem12445678932', Password='1234', Fullname='Zaeem6100', Address='qwerty',
                 phone_number='123123',
                 email='zaeem@zaeem.com', user_type='Admin')
    # get directory of project and append Database/AMUser.txt to it
    # print(model.write_to_file())
    # print(model.read_from_file())
    # model.write_to_file()
    # print(model.readAllUsers())
