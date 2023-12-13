TXT_NUMBERS = {'one' : '1',
               'two' : '2',
               'three' : '3',
               'four' : '4',
               'five' : '5',
               'six' : '6',
               'seven' : '7',
               'eight' : '8',
               'nine' : '9'}

def valid_string_from_left(string, idx):
    # Case where number is wrote as a number
    if string[idx].isnumeric():
        return string[idx]

    # Case where number is wrote as a text
    for txt_number in TXT_NUMBERS:
        studied_string = string[idx:idx+len(txt_number)]
        if studied_string == txt_number:
            return TXT_NUMBERS[txt_number]
        
    return None

def valid_string_from_right(string, idx):
    # Case where number is wrote as a number
    if string[idx].isnumeric():
        return string[idx]

    # Case where number is wrote as a text
    for txt_number in TXT_NUMBERS:
        studied_string = string[idx+1-len(txt_number):idx+1]
        if studied_string == txt_number:
            return TXT_NUMBERS[txt_number]
        
    return None

def get_first_last_digits(string):
    l, r = 0, len(string) - 1
    digit1 = digit2 = None 

    while not digit1:
        digit1 = valid_string_from_left(string, l)
        l += 1

    while not digit2:
        digit2 = valid_string_from_right(string, r)
        r -= 1

    return digit1, digit2

def get_number_from_string(string):
    digit1, digit2 = get_first_last_digits(string)
    txt_number = digit1 + digit2
    number = int(txt_number)

    return number 

def calculate_sum(text_file):
    sum = 0 
    file = open(text_file, 'r')
    while True:
        line = file.readline()
        if not line:
            break
        else:
            number = get_number_from_string(line)
            sum += number

    return sum
     

if __name__ == "__main__":
    sum = calculate_sum('day1.txt')
    print(f"Sum = {sum}")