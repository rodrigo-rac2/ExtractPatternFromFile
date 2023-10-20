def match_type(char, type):
    """
    Checks if the char matches the type
    :param char: any char
    :param type: the type to check, like 'a' for alphabetic, 'n' for numeric, '-', '_', ' ' for special
    :return: True if the char matches the type, False otherwise
    """
    if type == 'c':
        return char.isalpha()
    elif type == 'n':
        return char.isdigit()
    elif not char.isalpha() and not char.isdigit():
        return char == type
    else:
        return False


def extract_pattern_from_string(string, pattern):
    """
    Extracts the pattern from the string
    :param string: any string
    :param pattern: a pattern of chars and numbers and special characters, like "CC-NNN"
    :return: the substrings of string that match the pattern
    """
    result = ''
    i = 0
    while i < len(string):
        if len(string[i:]) < len(pattern):
            break
        if match_type(string[i], pattern[0]):
            j = 0
            while j < len(pattern) and match_type(string[i + j], pattern[j]):
                j = j + 1
            if j == len(pattern):
                result = result + string[i:i + j] + "\n"
                i = i + j
        i = i + 1
    return result


if __name__ == '__main__':
    # asks in input for the file to extract from
    file_name = input('Enter the file name to extract from: (default: pattern.txt)')
    if file_name == '':
        file_name = 'pattern.txt'
    print('Extracting from file: ' + file_name)

    # asks for the pattern to extract from the file lines, example "NN-CC NN_CCCCC"
    pattern = input('Enter the pattern to extract: (default: cc-nnnn)')
    if pattern == '':
        pattern = 'cc-nnnn'
    print('Extracting pattern: ' + pattern)

    # asks for the file name to save the result
    new_file_name = input('Enter the file name to save the result: (default: results.txt)')
    if new_file_name == '':
        new_file_name = 'results.txt'
    print('Saving results to file: ' + new_file_name)

    # iterates through the file lines, calls the function to extract the pattern, prints the result and saves
    # to the new file
    with open(file_name, 'r') as file:
        for line in file.readlines():
            result = extract_pattern_from_string(line, pattern.lower())
            if result != '':
                print(result)
                with open(new_file_name, 'a') as new_file:
                    new_file.write(result + '\n')
