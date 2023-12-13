def parse_text(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()

        if line.startswith("Time:"):
            times = [int(time) for time in line.split(":")[1].split()]
        elif line.startswith("Distance:"):
            distances = [int(distance) for distance in line.split(":")[1].split()]
    
    return times, distances


def get_number_of_solutions(total_time, record_distance):
    n_solutions = 0 
    for prep_time in range(1, total_time +1):
        speed = prep_time
        time_left = total_time - prep_time
        distance = speed * time_left
        n_solutions += 1 if distance > record_distance else 0
    return n_solutions

def get_result_part_1(file_path):
    times, distances = parse_text(file_path)

    result = 1 

    for time, distance in zip(times, distances):
        n_solutions = get_number_of_solutions(time, distance)
        result *= n_solutions

    return result


if __name__ == '__main__':

    text_file_path = 'data/day6.txt'

    # Part 1 
    result = get_result_part_1(text_file_path)
    print(result)

  
