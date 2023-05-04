import multiprocessing
import time
import random


# Функция подсчета числа П
# Сделать квадрат 1х1 и нарисовать в нем круг. Затем разделить на 4.
# Взять два случайных значения (x, y).
# Если x^2 + y^2 <= 1, то точка находится в круге.
# Повторить вышеуказанное i раз.
def calc_pi(i):
    k = 0
    x = random.random()
    y = random.random()
    k += (x * x + y * y) <= 1
    return k


# Функция вывода имени процесса
def multi(x):
    print(f'Процесс {multiprocessing.current_process().name}')
    time.sleep(1)
    return x


# Функция вывода номера процесса. Pool отвечает за параллелизм данных
# apply_async отвечает за асинхронность
def process():
    p = multiprocessing.Pool(processes=4)
    for i in range(4):
        p.apply_async(multi, args=(i,))
    p.close()
    p.join()


if __name__ == '__main__':  # Объявляется для запуска функций в нужном порядке
    process()
    PI25DT = 3.141592653589793238462643
    num_cores = multiprocessing.cpu_count()
    print(f'Количество ядер = {num_cores}')
    iterations = range(500000)
    start_time = time.time()
    pool = multiprocessing.Pool(processes=4)

    # Подсчитать внутренние точки, разделить на все количество выполнений и
    # умножить на четыре. Чем больше итераций, тем точнее расчет.
    num_pi = (4 * (sum(pool.map(calc_pi, iterations))) / 500000)

    end_time = time.time()
    print(f'Результат: {num_pi}. '
          f'Расхождение с эталоном: {abs(num_pi - PI25DT)}')
    print(f'Время работы {end_time - start_time:.6f} секунд')
