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
    players = list(range(N))
    schedules = []

    def find_schedules(current_matches, remaining_players):
        if not remaining_players:
            schedules.append(current_matches)
            print(current_matches) # Вывод расписания
            return

        match1 = list(itertools.combinations(remaining_players, 2))[0] # Берём первый матч
        remaining_after_match1 = list(set(remaining_players) - set(match1))

        if len(remaining_after_match1) == 0 :
            find_schedules(current_matches + [match1], remaining_after_match1)
        else:
           for match2 in itertools.combinations(remaining_after_match1, 2):
                 find_schedules(current_matches + [match1, match2], list(set(remaining_after_match1) - set(match2)))
    
    find_schedules([], players)
    return schedules

def main_iterative():
    N = 4 
    start_time = time.time()
    schedules = generate_schedules_iterative(N)
    end_time = time.time()
    print(f"Итеративный подход ({N} игроков): {len(schedules)} расписаний," + 
        f" время: {end_time - start_time:.4f} сек.")


def generate_schedules_itertools(N):
    players = list(range(N))
    all_matches = list(itertools.combinations(players, 2))
    
    if N == 4 :
        schedules = []
        for p in itertools.permutations(all_matches):
            
            match1, match2, match3, match4, match5, match6 = p
            
            schedule = []
            
            players_in_round1 = set()
            for match in [match1, match2]:
                for player in match:
                  players_in_round1.add(player)
            
            players_in_round2 = set()
            for match in [match3, match4]:
                for player in match:
                  players_in_round2.add(player)
            
            players_in_round3 = set()
            for match in [match5, match6]:
                for player in match:
                  players_in_round3.add(player)
             
            if len(players_in_round1) == N and len(players_in_round2) == N and len(players_in_round3) == N:
               schedule.append([match1, match2])
               schedule.append([match3, match4])
               
               
               if [match5, match6] not in [([match1, match2]), ([match3, match4])]: 
                    schedule.append([match5, match6])
                    if schedule not in schedules:
                        schedules.append(schedule)
                        print(schedule) # Вывод расписания
        return schedules
    
    return []

def main_itertools():
    N = 4
    start_time = time.time()
    schedules = generate_schedules_itertools(N)
    end_time = time.time()
    print(f"Itertools подход ({N} игроков): {len(schedules)} расписаний, " +
        f"время: {end_time - start_time} сек.")

def main():
    main_iterative()
    main_itertools()

if __name__ == "__main__":
    main()
