from faker import Faker
from dataclasses import dataclass, field
import random


Faker.seed()
fake = Faker('ru_RU')

@dataclass
class Person:
    """Генерирует тестовые данные для человека
    
    - full_name = ФИО;
    - email = Email-адрес;
    - current_address = Текущий адрес;
    - permanent_address = Постоянный адрес;

    - first_name = Имя;
    - last_name = Фамилия;
    - age = Возраст (от 1 до 100);
    - salary = Зарплата;
    - department = Отдел;
    
    - subject = Предмет;
    - phone = Номер телефона.
    """

    full_name: str = field(default_factory=fake.name)
    email: str = field(default_factory=fake.email)
    current_address: str = field(default_factory=fake.address)
    permanent_address: str = field(default_factory=fake.address)

    first_name: str = field(default_factory=fake.first_name)
    last_name: str = field(default_factory=fake.last_name)
    age: int = field(default_factory=lambda: fake.random_int(1, 100))
    salary: int = field(default_factory=lambda: fake.random_int(20000, 100000))
    department: str = field(default_factory=fake.word)

    subject: str = field(default_factory=fake.word)
    phone: str = field(default_factory=fake.phone_number)

colors = ["Red", "Blue", "Green", "Yellow", "Purple", "Black", "White", "Voilet", "Indigo", "Magenta", "Aqua"]

@dataclass
class Colors:
    """Выбирает случайный цвет из массива"""
    colors: str = field(default_factory=lambda: random.choice(colors))
