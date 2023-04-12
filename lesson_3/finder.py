import argparse
import os
from pympler import asizeof


def search_in_file(filepath: str, pattern: str) -> None:
    count = 0
    with open(filepath, 'r', newline='\n') as input_file, open('results.txt', 'w') as output_file:
        while True:
            line: str = input_file.readline()
            if not line:
                break
            if pattern in line:
                output_file.write(line)
                count += 1

    file_size = os.path.getsize('results.txt')

    print(f'{count} lines have been written to results.txt')
    print(f'The size of the file is {asizeof.asizeof(file_size)} bytes.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Search for lines containing a given pattern in given file')
    parser.add_argument('--filepath', type=str, help='path to file')
    parser.add_argument('--pattern', type=str, help='Substring (pattern) to search for')

    args = parser.parse_args()

    search_in_file(args.filepath, args.pattern)
