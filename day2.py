import re 

MAX_RED_CUBES = 12
MAX_GREEN_CUBES = 13 
MAX_BLUE_CUBES = 14

MAX_COLORS = [MAX_RED_CUBES, MAX_GREEN_CUBES, MAX_BLUE_CUBES]
COLORS = ['red', 'green', 'blue']

def count_color_group(group, color):
        pattern = rf'(\d+) {color}' 
        match = re.search(pattern, group)

        if match:
            count = int(match.group(1))
            return count
        else:
            return 0
        
def valid_line(groups):
    for group in groups:
        for color, max_color in zip(COLORS, MAX_COLORS):
            if count_color_group(group, color) > max_color:
                return False
        
    return True

def get_line_power(groups):
    fewer_color_counts = {'red': 0, 'green': 0, 'blue': 0}
    for group in groups:
        for color in COLORS:
            nb_cubes = count_color_group(group, color)
            fewer_color_counts[color] = max(fewer_color_counts[color], nb_cubes)

    power = fewer_color_counts['red'] * fewer_color_counts['green'] * fewer_color_counts['blue']
    return power

def get_game_id_and_valid(line):

    pattern = r'Game (\d+):'
    match = re.search(pattern, line)

    game_id = int(match.group(1))
    rest_of_line = line[match.end():]

    groups = [group.strip() for group in rest_of_line.split(';')]

    valid = valid_line(groups)
        
    return game_id, valid


def get_game_power(line):

    pattern = r'Game (\d+):'
    match = re.search(pattern, line)

    game_id = int(match.group(1))
    rest_of_line = line[match.end():]

    groups = [group.strip() for group in rest_of_line.split(';')]

    power = get_line_power(groups)
        
    return power


def get_part1_result(filename):
    file = open(filename, 'r') 
    sum = 0
    while True:
        line = file.readline()
        if not line:
            break
        else:
            game_id, valid = get_game_id_and_valid(line)
            if valid:
                sum += game_id

    return sum

def get_part2_result(filename):
    file = open(filename, 'r') 
    sum = 0
    while True:
        line = file.readline()
        if not line:
            break
        else:
            power = get_game_power(line)
            sum += power

    return sum


if __name__ == '__main__':
    
    filename = 'data/day2.txt'

    result1 = get_part1_result(filename)
    result2 = get_part2_result(filename)

    print(f"Result1 : {result1}")
    print(f"Result2 : {result2}")