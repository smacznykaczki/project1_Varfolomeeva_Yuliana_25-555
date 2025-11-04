# labyrinth_game/constants.py
ROOMS = {
    'entrance': {
        'description': 'Вы в темном входе лабиринта. Стены покрыты мхом. На полу лежит старый факел.',
        'exits': {'north': 'hall', 'east': 'trap_room'},
        'items': ['torch'],
        'puzzle': None
    },
    'hall': {
        'description': 'Большой зал с эхом. По центру стоит пьедестал с запечатанным сундуком.',
        'exits': {'south': 'entrance', 'west': 'library', 'north': 'treasure_room', 'east': 'dining_room'},
        'items': [],
        'puzzle': ('На пьедестале надпись: "Назовите число, которое идет после девяти". Введите ответ цифрой или словом.', '10')
    },
    'trap_room': {
          'description': 'Комната с хитрой плиточной поломкой. На стене видна надпись: "Осторожно — ловушка".',
          'exits': {'west': 'entrance', 'east': 'alchemist_room'},
          'items': ['rusty_key'],
          'puzzle': ('Система плит активна. Чтобы пройти, назовите слово "шаг" три раза подряд (введите "шаг шаг шаг")', 'шаг шаг шаг')
    },
    'library': {
          'description': 'Пыльная библиотека. На полках старые свитки. Где-то здесь может быть ключ от сокровищницы.',
          'exits': {'east': 'hall', 'north': 'armory'},
          'items': ['ancient_book'],
          'puzzle': ('В одном свитке загадка: "Что растет, когда его съедают?" (ответ одно слово)', 'резонанс')  
    },
        'armory': {
          'description': 'Старая оружейная комната. На стене висит меч, рядом — небольшая бронзовая шкатулка.',
          'exits': {'south': 'library'},
          'items': ['sword', 'bronze_box'],
          'puzzle': None
    },
    'treasure_room': {
          'description': 'Комната, на столе большой сундук. Дверь заперта — нужен особый ключ.',
          'exits': {'south': 'hall'},
          'items': ['treasure_chest'],
          'puzzle': ('Дверь защищена кодом. Введите код (подсказка: это число пятикратного шага, 2*5= ? )', '10')
    },
    'dining_room': {
        'description': 'Огромный обеденный зал с каменным столом.',
        'exits': {'west': 'hall', 'south': 'kitchen'},
        'items': ['goblet'],
        'puzzle': ('На столе лежит предмет. Полон зубов, но не кусается. Что это?', 'вилка')
    },
    'kitchen': {
        'description': 'Мрачная каменна кухня. Над тлеющим очагом огромный котел с мутной жидкостью',
        'exits': {'north': 'dining_room'},
        'items': ['wine_bottle', 'sausauge'],
        'puzzle': None
    },
    'alchemist_room': {
        'description': 'Заставленная склянками комната с густым запахом серы и трав. Повсюду склянки, свитки и таинственные символы на стенах',
        'exits': {'west': 'trap_room'},
        'items': ['unknown_potion', 'old_manuscript'],
        'puzzle': ('Переведите неизвестное слово aenigma на одном из свитков', 'загадка')
    }
}