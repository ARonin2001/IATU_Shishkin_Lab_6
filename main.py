import time
import itertools

def generate_tournament_schedule_algorithmic(players):
    """Генерирует расписание турнира алгоритмическим способом."""
    matches = []
    for i in range(len(players)):
        for j in range(i + 1, len(players)):
            matches.append((players[i], players[j]))
    return matches

def generate_tournament_schedule_itertools(players):
    """Генерирует расписание турнира с использованием itertools.combinations."""
    return list(itertools.combinations(players, 2))

def print_schedule(schedule):
    """Выводит расписание турнира на экран."""
    for match in schedule:
        print(f"{match[0]} vs {match[1]}")

def measure_execution_time(func, *args):
    """Измеряет время выполнения функции."""
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time

# --- Часть 1: Сравнение методов ---
print("--- Часть 1: Сравнение методов ---")
players = ["Player " + str(i) for i in range(1, 6)] # Создадим список игроков

# Алгоритмический метод
algorithmic_schedule, algorithmic_time = measure_execution_time(generate_tournament_schedule_algorithmic, players)
print("Расписание (Алгоритмический метод):")
print_schedule(algorithmic_schedule)
print(f"Время выполнения: {algorithmic_time:.6f} секунд\n")

# itertools метод
itertools_schedule, itertools_time = measure_execution_time(generate_tournament_schedule_itertools, players)
print("Расписание (itertools метод):")
print_schedule(itertools_schedule)
print(f"Время выполнения: {itertools_time:.6f} секунд\n")


# Сравнение времени выполнения
print("Сравнение времени выполнения:")
if algorithmic_time < itertools_time:
  print("Алгоритмический метод быстрее")
else:
  print("itertools метод быстрее")


# --- Часть 2: Усложнение с ограничением и целевой функцией ---

print("\n--- Часть 2: Усложнение с ограничением и целевой функцией ---")
def generate_constrained_schedule(players, max_matches_per_day):
    """Генерирует расписание с ограничением на количество матчей в день и целевой функцией."""
    all_matches = list(itertools.combinations(players, 2))
    
    # Создадим словарь матчей
    matches_dict = {match: False for match in all_matches}
    
    schedule = []
    
    while True:
      daily_schedule = []
      matches_this_day = 0
      
      for match, played in matches_dict.items():
        if not played and matches_this_day < max_matches_per_day:
          daily_schedule.append(match)
          matches_dict[match] = True
          matches_this_day+=1
          
      if not daily_schedule:
         break
         
      schedule.append(daily_schedule)
    return schedule

def calculate_schedule_balance(schedule):
  """Вычисляет баланс расписания (целевая функция - минимальное отклонение от среднего количества матчей в день)."""
  if not schedule:
    return 0
  
  matches_per_day = [len(day_schedule) for day_schedule in schedule]
  
  avg_matches_per_day = sum(matches_per_day) / len(matches_per_day)
  
  deviation = sum(abs(matches - avg_matches_per_day) for matches in matches_per_day) / len(matches_per_day)
  
  return deviation

def print_constrained_schedule(schedule):
    """Выводит расписание с ограничением на экран."""
    for day, matches in enumerate(schedule):
        print(f"День {day + 1}:")
        for match in matches:
            print(f"  {match[0]} vs {match[1]}")

max_matches_per_day = 2  # Ограничение: не более 2 матчей в день
constrained_schedule = generate_constrained_schedule(players, max_matches_per_day)

print("Ограниченное расписание:")
print_constrained_schedule(constrained_schedule)

schedule_balance = calculate_schedule_balance(constrained_schedule)
print(f"\nОтклонение от среднего количества матчей в день: {schedule_balance:.2f}")