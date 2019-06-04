from abstract_factory import *

class PlaneBullet(AbstractBullet):
    def plane_bullet_shoot_logic(self, power):
        print('>> PlaneBullet.plane_bullet_shoot_logic: shoot logic with power = ' + str(power))

class PlaneUnit(AbstractUnit):
    def shoot(self, bullet):
        print('>> PlaneUnit: shoot')
        bullet.plane_bullet_shoot_logic(42)

class PlaneFactory(AbstractFactory):
    def create_unit(self):
        print('>> PlaneFactory: new PlaneUnit')
        return PlaneUnit()
    
    def create_bullet(self):
        print('>> PlaneFactory: new PlaneBullet')
        return PlaneBullet()
