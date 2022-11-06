def get_data(file):
    with open('cabinet.csv', "r") as file:
        data = [(string.replace('\n', '')).split(';') for string in file.readlines()]
    return data