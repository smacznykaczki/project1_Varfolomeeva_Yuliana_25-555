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


def solve_puzzle(game_state):
    """
    Функция для решения загадок в текущей комнате
    """
    current_room = game_state['current_room']
    room_data = ROOMS[current_room]
    
    # Проверяем, есть ли загадка в текущей комнате
    if not room_data['puzzle']:
        print("Загадок здесь нет.")
        return False
    
    # Получаем вопрос и правильный ответ
    question, correct_answer = room_data['puzzle']
    
    # Выводим вопрос
    print(f"\nЗагадка: {question}")
    
    # Получаем ответ от пользователя
    user_answer = get_input("Ваш ответ: ").strip()
    
    # Сравниваем ответ пользователя с правильным ответом
    if user_answer.lower() == correct_answer.lower():
        # Если ответ верный
        print("Поздравляем! Загадка разгадана! 🎉")
        
        # Убираем загадку из комнаты
        room_data['puzzle'] = None
        
        # Добавляем игроку награду (золотые монеты)
        if 'gold_coins' not in game_state['player_inventory']:
            game_state['player_inventory'].append('gold_coins')
            print("Вы получили награду: золотые монеты! 💰")
        
        return True
    else:
        # Если ответ неверный
        print("Неверно. Попробуйте снова.")
        return False