"""
Convert decimal numbers to binary and hexadecimal.
Reads numbers from a file, converts them manually, and stores results.
"""

import time
import os


def decimal_to_binary(n):
    """Manually converts a decimal number to binary."""
    if n == 0:
        return "0"
    binary = ""
    is_negative = n < 0
    n = abs(n)
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2
    return "-" + binary if is_negative else binary


def decimal_to_hexadecimal(n):
    """Manually converts a decimal number to hexadecimal."""
    if n == 0:
        return "0"
    hex_chars = "0123456789ABCDEF"
    hexadecimal = ""
    is_negative = n < 0
    n = abs(n)
    while n > 0:
        hexadecimal = hex_chars[n % 16] + hexadecimal
        n //= 16
    return "-" + hexadecimal if is_negative else hexadecimal


def read_numbers_from_file(filename):
    """Reads numbers from a file and returns a list of valid numbers."""
    numbers = []
    errors = []

    try:
        with open(filename, 'r', encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                try:
                    num = int(line)
                    numbers.append(num)
                except ValueError:
                    errors.append(line)
                    print(f"Warning: Invalid data '{line}' ignored.")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None, None

    return numbers, errors


def write_results_to_file(filename, results, errors, execution_time):
    """Appends conversion results and execution time to 'ConversionResults.txt'."""
    output_filename = "ConversionResults.txt"
    with open(output_filename, "a", encoding="utf-8") as file:  # Append mode
        file.write("=" * 50 + "\n")
        file.write(f"Results for {filename}:\n")

        for original, binary, hexadecimal in results:
            file.write(f"Decimal: {original}, Binary: {binary}, Hexadecimal: {hexadecimal}\n")

        if errors:
            file.write("\nInvalid Entries:\n")
            for err in errors:
                file.write(f"Invalid: {err}\n")

        file.write(f"\nExecution Time: {execution_time:.6f} seconds\n")
        file.write("=" * 50 + "\n\n")

    print(f"Results appended to '{output_filename}'.")


def process_all_files(directory):
    """Processes all '.txt' files in the given directory."""
    txt_files = [f for f in os.listdir(directory) if f.endswith('.txt')]

    if not txt_files:
        print("No text files found in the directory.")
        return

    for file in txt_files:
        file_path = os.path.join(directory, file)
        print(f"Processing: {file_path}")

        start_time = time.time()
        numbers, errors = read_numbers_from_file(file_path)

        if numbers is None or not numbers:
            print(f"Error: No valid numbers found in {file}. Skipping...")
            continue

        results = [(num, decimal_to_binary(num), decimal_to_hexadecimal(num)) for num in numbers]
        execution_time = time.time() - start_time

        write_results_to_file(file, results, errors, execution_time)


if __name__ == "__main__":
    DIRECTORY = "C:\\Users\\Compu\\Documents\\pythonProject2\\P2"  # Update path if needed
    process_all_files(DIRECTORY)

# exactly ONE blank line at the end
