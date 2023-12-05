import re 

MAX_RED_CUBES = 12
MAX_GREEN_CUBES = 13 
MAX_BLUE_CUBES = 14

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
        if count_color_group(group, 'red') > MAX_RED_CUBES:
            return False
        if count_color_group(group, 'green') > MAX_GREEN_CUBES:
            return False
        if count_color_group(group, 'blue') > MAX_BLUE_CUBES:
            return False
        
    return True

def get_game_id_and_valid(line):

    pattern = r'Game (\d+):'
    match = re.search(pattern, line)

    game_id = int(match.group(1))
    rest_of_line = line[match.end():]

    groups = [group.strip() for group in rest_of_line.split(';')]

    valid = valid_line(groups)
        
    return game_id, valid

def get_result(filename):
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


if __name__ == '__main__':
    result = get_result('data/day2.txt')
    print(f"Result : {result}")