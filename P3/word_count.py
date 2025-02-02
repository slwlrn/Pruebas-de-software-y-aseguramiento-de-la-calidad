"""
Word Count Program:
Reads words from a file, removes non-alphabetic characters,
counts occurrences, and saves the results.
"""

import os
import time


def read_words_from_file(filename):
    """
    Reads words from a file, converting them to lowercase and removing non-alphabetic characters.
    """
    words = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                cleaned_line = ''.join(
                    char.lower() if char.isalpha() else ' ' for char in line
                )
                words.extend(cleaned_line.split())
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return []
    return words


def count_word_frequencies(words):
    """
    Counts occurrences of words manually and returns a sorted dictionary.
    Sorting is by frequency (descending), then alphabetically (ascending).
    """
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    sorted_words = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))
    return sorted_words


def write_results_to_file(filename, word_counts, execution_time):
    """
    Writes the word count results to a new file following the naming convention.
    """
    output_filename = f"{filename}.Results.txt"
    with open(output_filename, "w", encoding="utf-8") as file:
        for word, count in word_counts:
            file.write(f"{word}\t{count}\n")
        file.write(f"\nExecution Time: {execution_time:.6f} seconds\n")

    print(f"Results saved to '{output_filename}'.")


def process_all_txt_files(directory_path):
    """
    Processes all '.txt' files in the given directory.
    Reads words, counts occurrences, and writes results.
    """
    txt_files = [f for f in os.listdir(directory_path) if f.endswith('.txt')]

    if not txt_files:
        print("No text files found in the directory.")
        return

    for file_name in txt_files:
        file_path = os.path.join(directory_path, file_name)
        print(f"Processing: {file_path}")

        start_time = time.time()
        words = read_words_from_file(file_path)

        if not words:
            print(f"Error: No valid words found in {file_name}. Skipping...")
            continue

        word_counts = count_word_frequencies(words)
        execution_time = time.time() - start_time

        write_results_to_file(file_name, word_counts, execution_time)


if __name__ == "__main__":
    DIRECTORY_PATH = os.path.abspath(".")  # Change this to your desired directory
    process_all_txt_files(DIRECTORY_PATH)

# exactly ONE blank line at the end
