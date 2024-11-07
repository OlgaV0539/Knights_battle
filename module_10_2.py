import threading
import  time


class Knight(threading.Thread):
    total_enemies = 100

    def __init__(self, name, power):
        super().__init__(name=name)
        self.name = name
        self.power = power


    def run(self):
        print(f"{self.name}, на нас напали!")
        days = 0
        while Knight.total_enemies > 0:
            time.sleep(1)
            if Knight.total_enemies <= self.power:
                Knight.total_enemies = 0
            else:
                Knight.total_enemies -= self.power
            days += 1
            print(f"{self.name} сражается {days} дней..., осталось {Knight.total_enemies} воинов")
        print(f"{self.name} одержал победу спустя {days} дней")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
