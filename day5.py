def parse_maps(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    mapping = {}
    current_key = None
    current_map = []

    for line in lines:
        line = line.strip()

        if line.startswith("seeds:"):
            seeds = [int(seed) for seed in line.split(":")[1].split()]
        elif line.endswith("map:"):
            current_key = line.split(" ")[0].strip()
            current_map = []
        elif line:
            current_map.append([int(value) for value in line.split()])
        elif current_key and current_map:
            mapping[current_key] = current_map
            current_key = None
            current_map = []

    if current_key and current_map:
       mapping[current_key] = current_map

    return seeds, mapping

def convert_seed_to_location(seed, mapping):
    current_value = seed 

    for map_key, map_values in mapping.items():
        # get a list of lists as map_values 
        for values in map_values:
            dest_start, source_start, range_l = values
            source_range = range(source_start, source_start + range_l) 
            dest_range = range(dest_start, dest_start + range_l) 

            if current_value in source_range:
                idx = current_value - source_start
                current_value = dest_range[idx]
                # Stop exploring this mapping key and go to the next one 
                break

    return current_value

def get_result_part_1(file_path):
    seeds, mapping = parse_maps(file_path)
    min_location = None

    for seed in seeds:
        location = convert_seed_to_location(seed, mapping)
        min_location = location if not min_location else min(location, min_location)

    return min_location


if __name__ == '__main__':

    text_file_path = 'data/day5.txt'

    # Part 1 
    result = get_result_part_1(text_file_path)
    print(result)

  
