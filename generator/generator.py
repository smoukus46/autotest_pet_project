from faker import Faker
from dataclasses import dataclass, field
import random


Faker.seed()
fake_ru = Faker('ru_RU')
fake_en = Faker('EN')

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

    full_name: str = field(default_factory=fake_ru.name)
    email: str = field(default_factory=fake_ru.email)
    current_address: str = field(default_factory=fake_ru.address)
    permanent_address: str = field(default_factory=fake_ru.address)

    first_name: str = field(default_factory=fake_ru.first_name)
    last_name: str = field(default_factory=fake_ru.last_name)
    age: int = field(default_factory=lambda: fake_ru.random_int(1, 100))
    salary: int = field(default_factory=lambda: fake_ru.random_int(20000, 100000))
    department: str = field(default_factory=fake_ru.word)

    subject: str = field(default_factory=fake_ru.word)
    phone: str = field(default_factory=fake_ru.phone_number)

colors = ["Red", "Blue", "Green", "Yellow", "Purple", "Black", "White", "Voilet", "Indigo", "Magenta", "Aqua"]

@dataclass
class Colors:
    """Выбирает случайный цвет из массива"""
    colors: str = field(default_factory=lambda: random.choice(colors))

@dataclass
class Date:
    """Генерирует даты

    - year = Год;
    - month = Месяц;
    - day = День месяца;
    - time = Время;
    """
    year: str = field(default_factory=fake_en.year)
    month: str = field(default_factory=fake_en.month)
    day: str = field(default_factory=fake_en.day_of_month)
    time: str = field(default_factory=fake_en.time)
