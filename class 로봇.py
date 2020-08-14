class Robot:
    """repersents a robot, with a name."""
    population = 0

    def __init__(self,name):
        """initializes the data"""
        self.name = name
        print(f'initializing {self.name}')
        Robot.population += 1

    def die(self):
        """i amd dying"""
        print(f'{self.name} is being destroyed!')
        Robot.population -= 1
        if Robot.population == 0:
            print(f'{self.name} was the last one')
        else:
            print(f'there are still {Robot.population} robots working')
    def say_hi(self):
        """greeting by the robot. Yeah"""
        print(f'hi my master call me {self.name}')

    @classmethod
    def how_many(cls):
        print(f'we have {cls.population} robots')

droid = Robot('알파고1')
droid.say_hi()
droid2 = Robot('알파고2')
droid2.say_hi()
droid3 = Robot('알파고3')
droid3.say_hi()
Robot.how_many()
droid3.die()
droid2.die()
droid.die()
Robot.how_many()