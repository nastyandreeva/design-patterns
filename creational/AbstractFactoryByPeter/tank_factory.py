from abstract_factory import *

class TankBullet(AbstractBullet):
    def tank_bullet_shoot_logic(self):
        print('>> TankBullet.tank_bullet_shoot_logic: shoot logic')

class TankUnit(AbstractUnit):
    def shoot(self, bullet):
        print('>> TankUnit: shoot')
        bullet.tank_bullet_shoot_logic()

class TankFactory(AbstractFactory):
    def create_unit(self):
        print('>> TankFactory: new TankUnit')
        return TankUnit()
    
    def create_bullet(self):
        print('>> TankFactory: new TankBullet')
        return TankBullet()
