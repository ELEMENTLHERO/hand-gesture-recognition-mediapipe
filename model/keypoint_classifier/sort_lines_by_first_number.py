import sys


def sort_file_by_first_number(input_filename, output_filename):
    # Read lines from the file
    with open(input_filename, 'r') as file:
        lines = file.readlines()

    # Parse lines and sort them based on the first number
    sorted_lines = sorted(lines, key=lambda line: int(line.split(',')[0]))

    # Write sorted lines back to a new file
    with open(output_filename, 'w') as file:
        for line in sorted_lines:
            file.write(line)


if __name__ == '__main__':
    # Default filenames
    input_file = 'keypoint.csv'
    output_file = 'keypoint.csv'

    # Use command line arguments if provided
    if len(sys.argv) == 3:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
    elif len(sys.argv) > 1:
        print("Usage: python sort_lines_by_first_number.py [input_file output_file]")
        print("Using default files: keypoint.csv -> sorted_keypoint.csv")

    sort_file_by_first_number(input_file, output_file)
    print(f"File '{input_file}' has been sorted and saved to '{output_file}'.")
