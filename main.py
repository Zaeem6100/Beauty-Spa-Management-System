from Model import User as model

if __name__ == '__main__':
    model = model.User(Username='zaeem123', Password='1234', Fullname='Zaeem6100', Address='qwerty', phone_number='123123',
                       email='zaeem@zaeem.com', user_type='Admin')

    model.write_to_file()
