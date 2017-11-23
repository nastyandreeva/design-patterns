"""
Пример реализации шаблона "Одиночка"
"""
import functools


def singleton(cls):
    """
    Функция singleton() является механизмом
     декорирования класса MyClass(). Она принимает 
     в качестве входного аргумента cls - класс (например, MyClass)
     и подменяет его функцией getinstance(*args, *kwargs) 
     @functools.wraps(cls) позволяет сохранить аргументы, 
     с которыми объект класса MyClass создается. 
     В нашем случае - это 42, 100500

    """
    instance = None  # здесь храним единственный объект класса

    @functools.wraps(cls)
    def getinstance(*args, **kwargs):
        """
        
        *args, *kwargs - аргументы, с которым объект класса был создан
        Мы должны передать их по цепочке, чтобы они сохранились
        внутри объекта

        """
        nonlocal instance       # объемлющее значение переменной
        if instance is None:    # является None?

            # Если да, значит объект не создан 
            # и мы создаем объект класса cls
            instance = cls(*args, **kwargs)

            # Если нет, то сразу
        return instance         # возвращаем созданный объект
    return getinstance


@singleton
class MyClass:

    def __init__(self, value):
        self.value = value


if __name__ == '__main__':

    obj = MyClass(42)   # MyClass - это 'одиночка'
    print(obj.value)    # 42

    obj_2 = MyClass(100500)   # создали второй объект класс MyClass(),
    # инициализировав значением 100500

    print("id(obj) == id(obj_2) -> {}".format(id(obj) == id(obj_2)))
    print("obj is obj_2 -> {}".format(obj is obj_2))

    print("type(obj) = {}".format(type(obj)))
    print("isinstance(obj, type(obj)) = {}".format(isinstance(obj, type(obj))))
    print("isinstance(obj_2, type(obj)) = {}".format(
        isinstance(obj_2, type(obj))))
