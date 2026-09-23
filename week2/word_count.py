"""
Assignment 2: Word Counter from Text File
Count number of words, lines, and characters.
"""


def count_file_stats(filename):
    with open(filename, "r") as f:
        lines = f.readlines()

    num_lines = len(lines)
    num_words = sum(len(line.split()) for line in lines)
    num_chars = sum(len(line) for line in lines)

    return num_lines, num_words, num_chars


def main():
    filename = input("Enter the filename (e.g. sample.txt): ")

    try:
        lines, words, chars = count_file_stats(filename)
        print(f"\nLines: {lines}")
        print(f"\nWords: {words}")
        print(f"Characters: {chars}")
    except FileNotFoundError:
        print("File not found. Please check the filename and try again.")


if __name__ == "__main__":
    main()