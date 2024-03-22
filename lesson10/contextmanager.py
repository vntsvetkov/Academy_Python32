from lesson10 import Time
import time


class Timer:

    def __init__(self):
        self.start_time: time = None

    def __enter__(self):
        self.start_time = int(time.time()) + int(Time(3, 0, 0))
        now = Time.from_seconds(self.start_time)
        print("Начальное время: ", now)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        now = time.time() + int(Time(3, 0, 0))
        elapsed_time = int(now - self.start_time)
        now_time = Time.from_seconds(int(now))
        print("Конечное время: ", now_time)
        print(f"Всего прошло: {elapsed_time} секунд")


# Пример использования контекстного менеджера
with Timer() as timer:
    # Ваш блок кода
    time.sleep(2)

# Завершение with