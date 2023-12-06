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

    
if __name__ == '__main__':
    text_file_path = 'data/day3.txt'
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

    print(sum)

