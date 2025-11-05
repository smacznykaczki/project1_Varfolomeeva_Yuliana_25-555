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
    
def take_item(game_state, item_name):
    """
    Функция для взятия предмета из комнаты
    """
    current_room = game_state['current_room']
    room_data = ROOMS[current_room]
    
    # Проверяем, есть ли предмет в комнате
    if item_name in room_data['items']:
        # Добавляем предмет в инвентарь игрока
        game_state['player_inventory'].append(item_name)
        
        # Удаляем предмет из списка предметов комнаты
        room_data['items'].remove(item_name)
        
        # Печатаем сообщение о том, что игрок подобрал предмет
        print(f"Вы подняли: {item_name}")
        return True
    else:
        # Если такого предмета в комнате нет
        print("Такого предмета здесь нет.")
        return False
    
def use_item(game_state, item_name):
    """
    Функция для использования предмета из инвентаря
    """
    inventory = game_state['player_inventory']
    
    # Проверяем, есть ли предмет в инвентаре
    if item_name not in inventory:
        print("У вас нет такого предмета.")
        return False
    
    # Уникальные действия для каждого предмета
    if item_name == 'torch':
        print("Вы зажгли факел. Стало светлее, теперь можно разглядеть детали комнаты.")
        return True
    
    elif item_name == 'sword':
        print("Вы почувствовали уверенность, держа меч в руках. Теперь не так страшно!")
        return True
    
    elif item_name == 'bronze_box':
        print("Вы открыли бронзовую шкатулку.")
        if 'rusty_key' not in inventory:
            print("Внутри вы нашли старый ржавый ключ!")
            game_state['player_inventory'].append('rusty_key')
            return True
        else:
            print("Шкатулка пуста.")
            return True
    
    else:
        # Для остальных предметов
        print(f"Вы не знаете, как использовать {item_name}.")
        return False