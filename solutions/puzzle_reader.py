import os

def read_puzzle(file_name: str) -> str:
    ''' Reads the puzzle input data from the given file and returns the entire
    contents as a string. '''

    file_path = os.path.join('data',file_name)

    with open(file_path, 'r') as f:
        return f.read()