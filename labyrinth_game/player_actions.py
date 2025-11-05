# labyrinth_game/player_actions.py

from constants import ROOMS
from utils import describe_current_room

def show_inventory(game_state):
    """
    Функция для отображения инвентаря игрока
    """
    inventory = game_state['player_inventory']
    
    if inventory:
        print("\n=== ВАШ ИНВЕНТАРЬ ===")
        for i, item in enumerate(inventory, 1):
            print(f"{i}. {item}")
        print(f"Всего предметов: {len(inventory)}")
    else:
        print("\nВаш инвентарь пуст.")
    print()  # Пустая строка для читабельности

 
def get_input(prompt="> "):
    """
    Функция для безопасного ввода пользователя
    """
    try:
        return input(prompt)
    except (KeyboardInterrupt, EOFError):
        print("\nВыход из игры.")
        return "quit"
    
def move_player(game_state, direction):
    """
    Функция для перемещения игрока между комнатами
    """
    current_room = game_state['current_room']
    room_data = ROOMS[current_room]
    
    # Проверяем, существует ли выход в этом направлении
    if direction in room_data['exits']:
        # Получаем название новой комнаты
        new_room = room_data['exits'][direction]
        
        # Обновляем текущую комнату
        game_state['current_room'] = new_room
        
        # Увеличиваем шаг на единицу
        game_state['steps_taken'] += 1
        
        # Выводим сообщение о перемещении
        print(f"Вы переместились {direction}.")
        
        # Выводим описание новой комнаты
        describe_current_room(game_state)
        return True
    else:
        # Если выхода нет
        print("Нельзя пойти в этом направлении.")
        return False