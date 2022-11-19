class Services:

    def __init__(self, name, price, duration):
        self.name = name
        self.price = price
        self.duration = duration

    def __str__(self):
        return f"{self.name} - {self.price} - {self.duration}"

    def __repr__(self):
        return f"{self.name} - {self.price} - {self.duration}"

    def write_to_file(self):
        with open("Services.txt", "a") as file:
            file.write(f"{self.name},{self.price},{self.duration}\n")

    @staticmethod
    def read_from_file(filename="Services.txt"):
        services = []
        with open(filename, "r") as file:
            for line in file:
                name, price, duration = line.strip().split(",")
                services.append(Services(name, price, duration))
        return services

    @staticmethod
    def get_service_by_name(name):
        for service in Services.read_from_file():
            if service.name == name:
                return service
