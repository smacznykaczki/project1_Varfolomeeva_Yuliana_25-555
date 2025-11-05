# labyrinth_game/player_actions.py

from constants import ROOMS

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