from faker import Faker
from datetime import datetime, timedelta
from dataclasses import dataclass, field
import random


Faker.seed()
fake_ru = Faker('ru_RU')
fake_en = Faker('EN')


def calculate_next_time():
    now = datetime.now()
    nearest_quarter_hour = (now + timedelta(minutes=15 - now.minute % 15)).replace(second=0, microsecond=0)
    return nearest_quarter_hour.strftime("%H:%M")


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
    - month_number = номер месяца;
    - month_name = Название месяца;
    - day = День месяца;
    - time = Время в формате {HH:MM};
    """
    year_for_date_and_time: str = field(default_factory=lambda: fake_ru.random_int(2019, 2029))
    year_for_select_date: str = field(default_factory=fake_en.year)
    month_number: str = field(default_factory=fake_en.month)
    month_name: str = field(default_factory=fake_en.month_name)
    day: str = field(default_factory=fake_en.day_of_month)
    time: str = field(default_factory=calculate_next_time)

select_values = ["Group 1, option 1", "Group 1, option 2", "Group 2, option 1", "Group 2, option 2", "A root option", "Another root option"]

@dataclass
class SelectValues:
    """Выбирает случайное значение из массива"""
    select_values: str = field(default_factory=lambda: random.choice(select_values))
