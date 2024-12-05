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