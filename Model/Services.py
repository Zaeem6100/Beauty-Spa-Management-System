import os


class Services:

    def __init__(self, name='', price=0.0):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.price} "

    def __repr__(self):
        return f"{self.name} - {self.price}"

    def write_to_file(self, filename=os.path.join(os.path.dirname(os.path.dirname(__file__)), "Database\Services.txt")):
        with open(filename, "a") as file:
            file.write(f"{self.name},{self.price}\n")

    @staticmethod
    def read_from_file(filename=os.path.join(os.path.dirname(os.path.dirname(__file__)), "Database\Services.txt")):
        services = []
        with open(filename, "r") as file:
            for line in file:
                name, price = line.strip().split(",")
                services.append(Services(name, price))
        return services

    @staticmethod
    def get_service_by_name(name):
        for service in Services.read_from_file():
            if service.name == name:
                return service

    def convertToList(self):
        return [self.name, self.price]


if __name__ == '__main__':
    services = Services.read_from_file()
    print(services)
    # service = Services.get_service_by_name("Haircut")
    # print(service)
    # service = Services("Haircut", 20)
    # service.write_to_file()
