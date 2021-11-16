from collections import UserDict


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[name] = record


class Record:
    def __init__(self, name):
        self.name = name
        self.phones = []
    def add_field(self, phone):
        self.phones.append(phone)
    def change_field(self, phone, new_phone):
        self.phones[self.phones.index(phone)] = new_phone
    def delete_field(self, phone):
        self.phones.remove(phone)


class Field:
    pass


class Name(Field):
    def __init__(self, name):
        self.name = name


class Phone(Field):
    def __init__(self, phone):
        self.phone = phone


name = Name('Sasha')
phone = Phone('456757532')
phone2 = Phone('000000000')
r = Record(name)
r.add_field(phone)
r.add_field(phone2)
print(r.name.name)
print(r.phones[0].phone)
print(r.phones[1].phone)
phone3 = Phone('11111111')
r.change_field(phone, phone3)
print(r.phones[0].phone)
r.delete_field(phone)
print(r.phones[0].phone)