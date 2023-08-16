# Function to read the file and parse it into lines
def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

