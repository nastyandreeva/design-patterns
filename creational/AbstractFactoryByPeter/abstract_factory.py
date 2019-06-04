#from abc import ABC, abstractmethod

# класс абстрактной фабрики, создает технику и совместимые пули/снаряды
class AbstractFactory:
    # создание техники
    def create_unit(self):
        pass
    
    # создание пули/снаряда
    def create_bullet(self):
        pass

# класс абстрактной пули/снаряда
class AbstractBullet:
    pass

# класс абстрактной техники
class AbstractUnit:
    def shoot(self, bullet):
        pass