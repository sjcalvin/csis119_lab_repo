from random import seed, sample, choice
from os import linesep
from string import punctuation
from math import sqrt
from itertools import product

SEED_NUMBER = 1024
seed(SEED_NUMBER)
MAP_SIZE = 100
all_possible_symbols = frozenset(punctuation+'GSFT ')


def define_possible_objects(choices=punctuation):
    chars = choices
    chars += 'G'
    chars += 'T'*3
    chars += 'F'*3
    return chars


def generate_object(itera, available_coordinates, occupied_coordinates):
    symbol = sample(itera, 1)
    coordinates = choice(available_coordinates)
    available_coordinates.remove(coordinates)
    occupied_coordinates.append(coordinates)
    return symbol, coordinates


def set_up():
    symbols1 = define_possible_objects(punctuation)
    symbols2 = define_possible_objects('^&*'*5)
    return symbols1, symbols2


def generate_available_coordinates(map_size):
    return list(product(range(map_size), repeat=2))


def generate_empty_map(available_coordinates):
    galaxy_map = {}
    for coordinate in available_coordinates:
        galaxy_map[coordinate] = ' '
    galaxy_map[(0, 0)] = 'S'
    return galaxy_map


def get_unique_objects(galaxy_map):
    return frozenset(galaxy_map.values())


def symbols_not_used_in_galaxy(symbols_in_galaxy):
    return list(all_possible_symbols - symbols_in_galaxy)


def common_objects_encountered(galaxy_1_objects, galaxy_2_objects):
    return list(galaxy_1_objects.intersection(galaxy_2_objects))


def objects_encountered_in_galaxy1_not_galaxy2(galaxy_1_objects, galaxy_2_objects):
    return list(galaxy_1_objects - galaxy_2_objects)


def objects_encountered_in_galaxy2_not_galaxy1(galaxy_1_objects, galaxy_2_objects):
    return list(galaxy_2_objects - galaxy_1_objects)


def objects_encountered_in_both_galaxys(galaxy1_objects, galaxy2_objects):
    return list(galaxy1_objects.union(galaxy2_objects))


def calculate_path_to_goal(sorted_object_list):
    goal_distance = sorted_object_list[-1][0]
    return [(distance, coordinate, symbol) for distance, coordinate, symbol in sorted_object_list if distance < goal_distance]


def display_galaxy(galaxy_map):
    max_x = max([coordinate[0] for coordinate in galaxy_map.keys()])
    max_y = max([coordinate[1] for coordinate in galaxy_map.keys()])
    
    galaxy_string = ""
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            galaxy_string += galaxy_map.get((x, y), ' ') + ' '
        galaxy_string += linesep
    print(galaxy_string)


def calculate_euclidean_distance(coordinates):
    x, y = coordinates
    return int(sqrt(x ** 2 + y ** 2))


def populate_galaxy_map(available_symbols, available_coordinates, occupied_coordinates, galaxy_map):
    objects_encountered_list = list()
    while True:
        symbol, coordinates = generate_object(available_symbols, available_coordinates, occupied_coordinates)
        distance = calculate_euclidean_distance(coordinates)
        objects_encountered_list.append((distance, coordinates, symbol[0]))
        if symbol == 'G':
            break
    return sorted(objects_encountered_list, key=lambda x: x[0])


def run_exploration():
    available_symbols1, available_symbols2 = set_up()

    available_coordinates1 = generate_available_coordinates(MAP_SIZE)
    available_coordinates2 = generate_available_coordinates(MAP_SIZE)
    occupied_coordinates1 = list()
    occupied_coordinates2 = list()

    galaxy_map_1 = generate_empty_map(available_coordinates1)
    galaxy_map_2 = generate_empty_map(available_coordinates2)

    explorer1_list = populate_galaxy_map(available_symbols1, available_coordinates1, occupied_coordinates1, galaxy_map_1)
    explorer2_list = populate_galaxy_map(available_symbols2, available_coordinates2, occupied_coordinates2, galaxy_map_2)

    print("Explorer 1 list:")
    print(explorer1_list)
    print("\nExplorer 2 list:")
    print(explorer2_list)

    path_list1 = calculate_path_to_goal(explorer1_list)
    print("\nPath list for Explorer 1:")
    print(path_list1)

    path_list2 = calculate_path_to_goal(explorer2_list)
    print("\nPath list for Explorer 2:")
    print(path_list2)

    print("\nGalaxy Map 1:")
    display_galaxy(galaxy_map_1)
    print("\nGalaxy Map 2:")
    display_galaxy(galaxy_map_2)

    galaxy2_symbols = get_unique_objects(galaxy_map_2)
    galaxy1_symbols = get_unique_objects(galaxy_map_1)
    print("\nUnique symbols in Galaxy 1:")
    print(galaxy1_symbols)
    print("\nUnique symbols in Galaxy 2:")
    print(galaxy2_symbols)

if __name__ == '__main__':
    run_exploration()