from collections import defaultdict

def parse_schematic(schematic):
    lines = schematic.strip().split('\n')
    grid = [list(line) for line in lines]
    return grid

def get_grid(text_file_path):

    with open(text_file_path, 'r') as txt_file:
        content = txt_file.read()

    grid = parse_schematic(content)
    return grid 

def print_grid(grid):
    for line in grid:
        print(line)

def find_number(grid, row, col, max_cols):
    # return number and its initial position
    if grid[row][col].isnumeric:
        initial_position = row, col
        number = ''
        while col < max_cols and grid[row][col].isnumeric():
            number += grid[row][col]
            col += 1

        return number, initial_position

    else:
        return None, None
    
def update_visited(number, position, visited):
    row, col = position
    for digit in number:
        visited.add((row, col))
        col += 1

    return visited 

def is_special_symbol(symbol):
    return False if (symbol.isnumeric() or symbol == '.') else True

def check_part_number(grid, number, position, max_rows, max_cols):
    r, c = position
    for dc in range(len(number)):
        col = c + dc 
        digit_positon = r, col
        if check_adjacent_digit(grid, digit_positon, max_rows, max_cols):
            return int(number)
        
    return False

def check_adjacent_digit(grid, position, rows, cols):
    # Could be improved but here check all neighboors
    DIRECTIONS = [[-1, 1],
                    [0, 1],
                    [1, 1],
                    [1, 0],
                    [1, -1],
                    [0, -1],
                    [-1, -1],
                    [-1,0]]
    
    r, c = position 

    for dpos in DIRECTIONS:
        dr, dc = dpos
        neighboor_r = r + dr 
        neighboor_c = c + dc 
        if 0 <= neighboor_r < rows and 0 <= neighboor_c < cols:
            if is_special_symbol(grid[neighboor_r][neighboor_c]):
                return True
        
    return False

def get_result_part_1(text_file_path):
    grid = get_grid(text_file_path)

    ROWS = len(grid)
    COLS = len(grid[0])

    visited = set()
    sum = 0 

    for row in range(ROWS):
        for col in range(COLS):
            if (row, col) not in visited:
                number, position = find_number(grid, row, col, COLS)
                if number:
                    visited = update_visited(number, position, visited)
                    part_number = check_part_number(grid, number, position, ROWS, COLS)
                    if part_number:
                        sum += part_number

    return sum

# Functions for part2 results 

def check_adjacent_get_symbols_position(grid, position, rows, cols):
    DIRECTIONS = [[-1, 1],
                    [0, 1],
                    [1, 1],
                    [1, 0],
                    [1, -1],
                    [0, -1],
                    [-1, -1],
                    [-1,0]]
    
    symbols_position = []
    r, c = position 

    for dpos in DIRECTIONS:
        dr, dc = dpos
        neighboor_r = r + dr 
        neighboor_c = c + dc 
        if 0 <= neighboor_r < rows and 0 <= neighboor_c < cols:
            if is_special_symbol(grid[neighboor_r][neighboor_c]):
                symbols_position.append((neighboor_r, neighboor_c))
        
    return symbols_position

def check_part_number_get_symbols_position(grid, number, position, max_rows, max_cols):
    r, c = position
    adjacent_symbol_positions = set()
    for dc in range(len(number)):
        col = c + dc 
        digit_positon = r, col
        digit_adjacent_symbol_positions = check_adjacent_get_symbols_position(grid, digit_positon, max_rows, max_cols)
        if digit_adjacent_symbol_positions:
            for position in digit_adjacent_symbol_positions:
                adjacent_symbol_positions.add(position)
        
    return [int(number), adjacent_symbol_positions]

def multiply_list(num_list):
    prod = 1 
    for num in num_list:
        prod *= num

    return prod 

def get_gear_ratio_sum(symbol_positions_and_adjacent_numbers):
    sum = 0 
    for position in symbol_positions_and_adjacent_numbers:
        numbers = symbol_positions_and_adjacent_numbers[position]
        if len(numbers) > 1:
            sum += multiply_list(numbers)

    return sum

def get_result_part_2(text_file_path):
    grid = get_grid(text_file_path)

    ROWS = len(grid)
    COLS = len(grid[0])

    visited = set()
    symbol_positions_and_adjacent_numbers = defaultdict(list)

    for row in range(ROWS):
        for col in range(COLS):
            if (row, col) not in visited:
                number, position = find_number(grid, row, col, COLS)
                if number:
                    visited = update_visited(number, position, visited)
                    part_number, symbols_position = check_part_number_get_symbols_position(grid, number, position, ROWS, COLS)
                    if symbols_position:
                        for position in symbols_position:
                            symbol_positions_and_adjacent_numbers[position].append(part_number)

    sum = get_gear_ratio_sum(symbol_positions_and_adjacent_numbers)

    return sum

    
if __name__ == '__main__':

    text_file_path = 'data/day3.txt'

    # Part 1 
    sum = get_result_part_1(text_file_path)
    print(sum)

    # Part 2
    sum = get_result_part_2(text_file_path)
    print(sum)

    

