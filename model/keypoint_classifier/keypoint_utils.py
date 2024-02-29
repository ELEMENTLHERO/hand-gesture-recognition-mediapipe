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


def count_first_number_occurrences(filename):
    occurrences = {}

    # Read lines from the file and count occurrences
    with open(filename, 'r') as file:
        for line in file:
            first_number = int(line.split(',')[0])
            if first_number in occurrences:
                occurrences[first_number] += 1
            else:
                occurrences[first_number] = 1

    # Sort occurrences by count, descending
    sorted_occurrences = sorted(occurrences.items(), key=lambda item: item[1], reverse=True)

    # Print the sorted occurrences
    print("Letter (number) | Occurrences")
    for number, count in sorted_occurrences:
        print(f"{chr(65+number):<6} {number:<8} | {count}")

# This function can then be called similarly to the sort_file_by_first_number function,
# either directly in the script or through command line interaction if you prefer.


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python keypoint_utils.py <command> [args]")
        print("Commands: sort [input_file output_file], count [file]")
        sys.exit(1)

    command = sys.argv[1]
    if command == 'sort':
        input_file = 'keypoint.csv' if len(sys.argv) <= 2 else sys.argv[2]
        output_file = 'sorted_keypoint.csv' if len(sys.argv) <= 3 else sys.argv[3]
        sort_file_by_first_number(input_file, output_file)
    elif command == 'count':
        file = 'keypoint.csv' if len(sys.argv) <= 2 else sys.argv[2]
        count_first_number_occurrences(file)
    else:
        print("Invalid command. Use 'sort' or 'count'.")

