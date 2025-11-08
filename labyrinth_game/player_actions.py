# labyrinth_game/player_actions.py

from .constants import ROOMS
from .utils import describe_current_room, attempt_open_treasure, random_event

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
    
    if direction in room_data['exits']:
        new_room = room_data['exits'][direction]
        game_state['current_room'] = new_room
        game_state['steps_taken'] += 1
        print(f"Вы переместились {direction}.")
        
        # Вызываем случайное событие после успешного перемещения
        random_event(game_state)
        
        # Выводим описание новой комнаты
        describe_current_room(game_state)
        return True
    else:
        print("Нельзя пойти в этом направлении.")
        return False
    
def take_item(game_state, item_name):
    """
    Функция для взятия предмета из комнаты
    """
    current_room = game_state['current_room']
    room_data = ROOMS[current_room]
    
    # Проверяем, не пытается ли игрок поднять сундук
    if item_name == 'treasure_chest':
        print('Вы не можете поднять сундук, он слишком тяжелый.')
        return False

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
    current_room = game_state['current_room']
    room_data = ROOMS[current_room]
    
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
        found_something = False
        
        # Проверяем и добавляем rusty_key, если его нет
        if 'rusty_key' not in inventory:
            print("Внутри вы нашли старый ржавый ключ! 🗝️")
            game_state['player_inventory'].append('rusty_key')
            found_something = True
        
        # Проверяем и добавляем treasure_key, если его нет
        if 'treasure_key' not in inventory:
            print("Внутри вы нашли ключ от сокровищницы! 🔑")
            game_state['player_inventory'].append('treasure_key')
            found_something = True
        
        # Если оба ключа уже есть
        if not found_something:
            print("Шкатулка пуста.")
        
        return True
    
    elif item_name == 'treasure_key':
        # Проверяем, есть ли в комнате сундук с сокровищами
        if 'treasure_chest' in room_data['items']:
            # Спрашиваем, применить ли ключ к сундуку
            answer = get_input("Применить ключ к сундуку с сокровищами? (да/нет): ").strip().lower()
            if answer == 'да':
                return attempt_open_treasure(game_state)
            else:
                print("Вы решаете не использовать ключ сейчас.")
                return False
        else:
            print("Здесь не к чему применить этот ключ.")
            return False
    
    elif item_name == 'treasure_chest':
        print("Вы не можете использовать сундук таким образом.")
        return False


    elif item_name == 'rusty_key':
        print("Этот ржавый ключ выглядит старым. Возможно, он от чего-то важного...")
        return True
    
    else:
        # Для остальных предметов
        print(f"Вы не знаете, как использовать {item_name}.")
        return False