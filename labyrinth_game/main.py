#!/usr/bin/env python3
# labyrinth_game/main.py

# Импорт переменных и функций


from .constants import ROOMS
from .utils import describe_current_room, solve_puzzle, attempt_open_treasure
from .player_actions import get_input, show_inventory, move_player, take_item, use_item

def process_command(game_state, command):
    """
    Функция для обработки пользовательских команд
    """
    command = command.strip().lower()
    if not command:
        return
    
    # Разделяем строку на части, чтобы отделить команду от аргумента
    parts = command.split()
    main_command = parts[0]
    argument = ' '.join(parts[1:]) if len(parts) > 1 else ''
    
    # Используем match/case для определения команды
    match main_command:
        case 'quit' | 'exit':
            print("Спасибо за игру! До свидания!")
            game_state['game_over'] = True
        
        case 'look':
            describe_current_room(game_state)
        
        case 'inventory' | 'inv':
            show_inventory(game_state)
        
        case 'go':
            if argument in ['north', 'south', 'east', 'west']:
                move_player(game_state, argument)
            else:
                print("Укажите направление: go [north/south/east/west]")
        
        case 'north' | 'south' | 'east' | 'west':
            move_player(game_state, main_command)
        
        case 'take':
            if argument:
                take_item(game_state, argument)
            else:
                print("Укажите предмет: take [предмет]")
        
        case 'use':
            if argument:
                use_item(game_state, argument)
            else:
                print("Укажите предмет: use [предмет]")

        case 'solve':
            # Если в комнате с сокровищами, пытаемся открыть сундук
            if game_state['current_room'] == 'treasure_room':
                attempt_open_treasure(game_state)
            else:
                # В других комнатах решаем обычные загадки
                solve_puzzle(game_state)
        
        case 'help':
            print("\n=== СПРАВКА ПО КОМАНДАМ ===")
            print("  look - осмотреться в текущей комнате")
            print("  go [направление] - перемещение (north, south, east, west)")
            print("  take [предмет] - взять предмет")
            print("  use [предмет] - использовать предмет из инвентаря")
            print("  inventory - показать инвентарь")
            print("  help - показать эту справку")
            print("  quit - выйти из игры")
            print()
        
        case _:
            print("Неизвестная команда. Введите 'help' для списка команд.")

def main():
    """
    Основная функция игры - игровой цикл
    """
    # Состояние игры
    game_state = {
        'player_inventory': [],      # Инвентарь игрока
        'current_room': 'entrance',  # Текущая комната
        'game_over': False,          # Флаг окончания игры
        'steps_taken': 0             # Количество шагов
    }
    
    # Приветственное сообщение
    print("=== ДОБРО ПОЖАЛОВАТЬ В ЛАБИРИНТ СОКРОВИЩ! ===")
    print("Используйте команды: look, go [направление], take [предмет], use [предмет], inventory, quit")
    print("Введите 'help' для получения справки по командам")
    print("-" * 50)
    
    # Описываем стартовую комнату
    describe_current_room(game_state)
    
# Основной игровой цикл
    while not game_state['game_over']:
        try:
            # Считываем команду от пользователя
            user_input = get_input("Введите команду: ")
            
            # Обрабатываем команду через process_command
            process_command(game_state, user_input)
                
        except Exception as e:
            print(f"Произошла ошибка: {e}")


    # Поздравительное сообщение после победы
    if game_state['game_over'] and game_state['current_room'] == 'treasure_room':
        print("\n" + "="*50)
        print("🎉 ПОЗДРАВЛЯЕМ С ПОБЕДОЙ! 🎉")
        print(f"Вы прошли лабиринт за {game_state['steps_taken']} шагов!")
        print("="*50)# Поздравительное сообщение после победы
    
if __name__ == "__main__":
    main()
