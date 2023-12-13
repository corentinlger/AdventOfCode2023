def remove_card_info(line):
    card_info, rest_of_line = line.split(':')
    return rest_of_line

def extract_numbers_from_text(line):
    numbers = []
    idx = 0 
    num = ''

    while idx < len(line):
        if line[idx] == ' ':
            if num:
                numbers.append(int(num))
            num = ''
        else:
            num += line[idx]
        idx += 1

    return numbers

def extract_winning_your_numbers(line):
    winning_numbers_line, your_numbers_line = line.split('|')

    your_numbers_line += ' '
    winning_numbers = extract_numbers_from_text(winning_numbers_line)
    your_numbers = extract_numbers_from_text(your_numbers_line)

    return winning_numbers, your_numbers

def get_game_points(line):
    processed_line = remove_card_info(line)
    winning_numbers, your_numbers = extract_winning_your_numbers(processed_line)

    points = 0 
    for win_number in winning_numbers:
        for y_number in your_numbers:
            if win_number == y_number:
                points = 1 if points == 0 else points * 2
  
    return points

def get_result_part_1(text_file_path):
    file = open(text_file_path, 'r') 
    sum = 0
    idx = 1
    while True:
        line = file.readline().strip()
        if not line:
            break
        else:
            points = get_game_points(line)
            sum += points
        idx += 1

    return sum

# Part 2 functions 

def get_matching_cards(line):
    processed_line = remove_card_info(line)
    winning_numbers, your_numbers = extract_winning_your_numbers(processed_line)

    matching_cards = 0 
    for win_number in winning_numbers:
        for y_number in your_numbers:
            if win_number == y_number:
                matching_cards += 1
  
    return matching_cards

def get_result_part_2(text_file_path):
    with open(text_file_path, 'r') as fp:
        nb_lines = len(fp.readlines())

    copies = {card_nb: 1 for card_nb in range(1, nb_lines+1)}

    file = open(text_file_path, 'r') 

    current_card_nb = 1
    while True:
        line = file.readline().strip()
        if not line:
            break
        else:
            matching_cards = get_matching_cards(line)
            if matching_cards > 0:
                for next_card_nb in range(current_card_nb + 1, current_card_nb + matching_cards + 1):
                    if next_card_nb in copies:
                        copies[next_card_nb] += copies[current_card_nb]
        current_card_nb += 1

    sum = 0 
    for nb_cards in copies.values():
        sum += nb_cards

    return sum



if __name__ == '__main__':

    text_file_path = 'data/day4.txt'

    # Part 1 
    sum = get_result_part_1(text_file_path)
    print(sum)

    # Part 1 
    sum = get_result_part_2(text_file_path)
    print(sum)
