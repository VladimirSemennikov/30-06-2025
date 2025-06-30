"""
1. объектно оринтировочное пространство
2. инкапсуляция, полиморфизм, абстракция, наследование
3. Класс - простое представление типа объекта. Это чертеж/план/шаблон описывающий детали объекта
4. Объект - это экземпляр класса, он имеет свое собственное состояние по идеи и идентичности

5. Инкапсуляция - это один из принципов ООП, который позволяет ограничить
доступ к атрибутам или методам класса.
5.2 это атрибут объекта, который содержит скрытые данные, эти скрытые данные могут быть доступны только членам класса

6. Полиморфизм - очень важная идея в программировании. Она заключается в использовании единственной
сущности.
6.2 это не что иное, как присвоение поведения или значения в подклассе чему то, что было объявлено в основном классе.

7. наследование происходит от родительского класса и берет все его свойства
7.2 это концепция в которой 1 класс разделяет структуру и поведения определенную в другом классе.

8. конструктор - __init__ создает (self,) объекта
8.2 этот метод используемый для инициализации состояния объекта, который вызывается в состоянии объекта.

9. метод находится внутри класса и описываются все действия в классе (записываются формулы и т.п.)
9.2 это описание набора инструкции, которую так же можно назвать функцией (но это метод).

10. модификатор доступа нужны для сокрытия данных (приватный, обычные и защищенные)
10.2 они помогают установить доступность классов, методов и атрибутов.

11. статикметод это декоратор (метод) работает внутри класса
11.2 статиккласс работает с классом

12. лямда функции это - укороченная функция.
12.2 это безымянная функция, это анонимная функция, которые могут включать только одно выражение,
они обычно используются для простых операций.

13. модуль это
13.2 это файл, который содержит определение функции классов, переменных и другого кода.
Который можно использовать в других программах или модулях.
"""


"""
Категории методов:
1. методы и атрибуды связанные с атрибутами объектов:
__getattr__
__getattribute__

рекурсия - это когда функция вызывает саму себя.
"""

# class User:
#     name1 = 'Vasya'
#     name2 = 'Masha'
#
#     def __getattribute__(self, item):
#         return f"Привет {object.__getattribute__(self, item)}"
# user = User()
# print(user.name1)           #Привет Vasya
# print(user.name2)           #Привет Masha

#Контроль доступа к атрибутам объекта

# class User:
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password
#
#     def __getattribute__(self, item):
#         if item == 'password':
#             raise AttributeError("Доступ к паролю запрещен")
#         return object.__getattribute__(self, item)
# user = User("Vasya", "secret")
# print(user.username)        #Vasya
# print(user.password)        #AttributeError: Доступ к паролю запрещен

# class User:
#     def __init__(self, number, number2):
#         self.number = number
#         self.number2 = number2
#
#     def __getattribute__(self, item):
#         return 10 + object.__getattribute__(self, item)
#
# user1 = User(20, 30)
# user2 = User(500, 100)
#
# print(user1.number, user1.number2)
# print(user2.number, user2.number2)

# class Men:
#     def __init__(self, name):
#         self.name = name
#
#     def __getattribute__(self, item):
#         return f"{object.__getattribute__(self, item)}Man"
#
# super = Men('Super')
# bat = Men('Bat')
# spider = Men('Spider')
#
# print(super.name)
# print(bat.name)
# print(spider.name)

"""
__getattr__
Предоставляет возможность определить поведение при обращении к не существующим атрибутам объектаю
Он позволяет программисту контролировать.

def __getattr__(self, name):
    код определяющий при обращении к несуществующему атрибуту.
"""

# Пример 1

# class Person:
#     def __getattr__(self, name):
#         return f"Атрибут {name} не найден."
#
# person = Person()
# print(person.age)       #Атрибут age не найден.

# Пример 2

# class Person:
#     def __getattr__(self, name):
#         if name == "age":
#             return 30
#         else:
#             return "Атрибут не найден"
# person = Person()
# print(person.age)       #30
# print(person.number)       #Атрибут не найден


# Пример 3
#использование гетер для доступа к словарю

# class Person:
#     def __init__(self):
#         self.attributes = {"name": "Илья", "age": 34}
#
#     def __getattr__(self, item):
#         if item in self.attributes:
#             return self.attributes[item]            #обращаемся к ключу item
#         else:
#             return "Атрибут не найден"
# person = Person()
# print(person.name)
# print(person.age)
# print(person.height)

# class Person:
#     def __init__(self):
#         self.attributes = [11,2,1,34]
#
#     def __getattr__(self, item):
#         if item in self.attributes:
#             return self.attributes[item]
#         else:
#             return "Атрибут не найден"
# person = Person()
# print(person.attributes[1])
# print(person.attributes[2])
# print(person.height)

# class Person:
#     name = "Vasya"
#     def __getattr__(self, item):
#         if item == "name":
#             return self.name
#         else:
#             return "Такого атрибута нет"
#
# person = Person()
# print(person.name)
# print(person.age)

"""
__setattr__
вызывается при установке значения атрибута экземпляра и позволяет определить 
поведение при установке значении атрибута экземпляра.
def __setattr(self, name, value):
    object.__setattr__(self, name, value)
или

def __setattr__(self, name, value):
    super().__setattr__(name, value)
"""

#Пример 1

# class Person:
#     def __setattr__(self, name, value):
#         if name == 'name':
#             print(f"Создали атрибут name со значением {value}")
#         else:
#             print("нет такого")
#         super().__setattr__(name, value)
#
# person = Person()
# person.name = "Vasya"               #Создали атрибут name со значением Vasya
# person.name = "Masha"               #Создали атрибут name со значением Masha
# person.name1 = "Masha"              #нет такого

#Пример 2

# class Person:
#     def __setattr__(self, name, value):
#         if name == "age" and value < 0:
#             raise ValueError("Возраст не может быть отрицателньым!")
#         else:
#             super().__setattr__(name, value)
# person = Person()
# person.age = 25
# person.age = -5         #ValueError: Возраст не может быть отрицателньым!


#Пример 3.
#Запрещает создавать атрибуту какое-то значение.
class Immutable:
    def __setattr__(self, key, value):
        raise AttributeError("Нельзя создавать объект")

imutable_obj = Immutable()
imutable_obj.name = "Vasya"         #AttributeError: Нельзя создавать объект
