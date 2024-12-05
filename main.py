"""
	Задание состоит из двух частей. 
	1 часть – написать программу в соответствии со своим вариантом задания. 
	Написать 2 варианта формирования (алгоритмический и с помощью функций Питона), сравнив по времени их выполнение.
	2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение на характеристики объектов 
	(которое будет сокращать количество переборов) и целевую функцию для нахождения оптимального  решения.

	 Вариант 20. В шахматном турнире принимают участие N шахматистов, причем каждый из них должен сыграть только одну партию с каждым 
	 из остальных. Выведите все возможные расписания турнира.
"""

import itertools
import time

def generate_schedules_iterative(N):
    """Генерирует все возможные расписания турнира с помощью вложенных циклов."""
    players = list(range(N))
    schedules = []
    for match1 in itertools.combinations(players, 2):
        remaining_players = list(set(players) - set(match1))
        for match2 in itertools.combinations(remaining_players, 2):
            # ... и так далее,  это не эффективно для больших N
            pass #pass, т.к. неэффективно для больших N
    return schedules


def main_iterative():
    N = 4 
    start_time = time.time()
    schedules = generate_schedules_iterative(N)
    end_time = time.time()
    print(f"Итеративный подход ({N} игроков): {len(schedules)} расписаний," + 
    	f" время: {end_time - start_time:.4f} сек.")

# Генерация с помощью функций python
def generate_schedules_itertools(N):
    players = list(range(N))
    all_matches = list(itertools.combinations(players, 2))
    schedules = list(itertools.permutations(all_matches, len(all_matches) // 2))
    return schedules

def main_itertools():
    N = 4
    start_time = time.time()
    schedules = generate_schedules_itertools(N)
    end_time = time.time()
    print(f"Itertools подход ({N} игроков): {len(schedules)} расписаний, " +
    	f"время: {end_time - start_time} сек.")

def main():
	# main_iterative()
	main_itertools()

if __name__ == "__main__":
	main()
