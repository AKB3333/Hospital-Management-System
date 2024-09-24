class Address:
    def __init__(self, street, city, state, zip_code, country):
        self.__street_address = street
        self.__city = city
        self.__state = state
        self.__zip_code = zip_code
        self.__country = country
    
    def __str__(self):
        return f"{self.__street_address}, {self.__city}, {self.__state} {self.__zip_code}, {self.__country}"
