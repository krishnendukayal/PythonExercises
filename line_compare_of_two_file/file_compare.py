def find_odd_lines(file1_path, file2_path, output_path):
    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
        file1_lines = set(file1.readlines())
        file2_lines = set(file2.readlines())

    odd_lines = file1_lines.symmetric_difference(file2_lines)

    with open(output_path, 'w') as output_file:
        for line in odd_lines:
            output_file.write(line)


def main():
    file1_path = 'file1.txt'
    file2_path = 'file2.txt'
    output_path = 'outputfile.txt'

    find_odd_lines(file1_path, file2_path, output_path)

    print(f"Odd lines have been written to {output_path}")


if __name__ == "__main__":
    main()
