#!/usr/bin/env python3

# Импорт модулей

import constants
import player_actions
import utils

# Импорт переменных и функций

from constants import ROOMS
from utils import describe_current_room
from player_actions import get_input

#Состояние игрока

game_state = {
    'player_inventory': [], # Инвентарь игрока
    'current_room': 'entrance', # Текущая комната
    'game_over': False, # Значения окончания игры
    'steps_taken': 0 # Количество шагов
  }

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
    print("-" * 50)
    
    # Описываем стартовую комнату
    describe_current_room(game_state)
    
    # Основной игровой цикл
    while not game_state['game_over']:
        
        # Считываем команду от пользователя
        user_input = get_input("Введите команду: ").strip().lower()
    
if __name__ == "__main__":
    main()
