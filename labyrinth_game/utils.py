# labyrinth_game/utils.py
 
from constants import ROOMS
 
def describe_current_room(game_state):
    """
    Функция для описания текущей комнаты
    """
    current_room_name = game_state['current_room']
    room = ROOMS[current_room_name]
    
    # Выводим название комнаты в верхнем регистре
    print(f"\n== {current_room_name.upper()} ==")
    
    # Выводим описание комнаты
    print(room['description'])
    
    # Выводим заметные предметы
    if room['items']:
        print("\nЗаметные предметы:")
        for item in room['items']:
            print(f"  - {item}")
    
    # Выводим доступные выходы
    if room['exits']:
        print("\nВыходы:")
        for direction, target_room in room['exits'].items():
            print(f"  - {direction}: {target_room}")
    
    # Сообщение о наличии загадки
    if room['puzzle']:
        print("\nКажется, здесь есть загадка (используйте команду solve).")
    
    print()  # Пустая строка для читабельности