import threading
import  time


class Knight(threading.Thread):
    
    def __init__(self, name, power):
        super().__init__(name=name)
        self.name = name
        self.power = power
        self.enemies = 100


    def run(self):
        print(f"{self.name}, на нас напали!")
        days = 0
        while self.enemies > 0:
            time.sleep(1)
            if self.enemies <= self.power:
                self.enemies = 0
            else:
                self.enemies -= self.power
            days += 1
            print(f"\n{self.name} сражается {days} дней..., осталось {Knight.total_enemies} воинов")
        print(f"{self.name} одержал победу спустя {days} дней")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
