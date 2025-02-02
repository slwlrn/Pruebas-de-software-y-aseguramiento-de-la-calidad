"""
Compute basic statistics (mean, median, mode, variance, and standard deviation)
for numbers stored in text files.
"""

import time
import os


def read_numbers_from_file(filename):
    """
    Reads numbers from a file and returns a list of valid numbers.
    Logs warnings for invalid or extreme values.
    """
    numbers = []
    try:
        with open(filename, 'r', encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                try:
                    num = float(line)
                    if abs(num) > 1e12:  # Detect extreme values
                        print(f"Warning: Extreme value detected -> {num}")
                    numbers.append(num)
                except ValueError:
                    print(f"Warning: Ignoring invalid data -> {line}")
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return []
    return numbers


def compute_mean(numbers):
    """Computes the mean (average) of a list of numbers manually."""
    total = sum(numbers)
    count = len(numbers)
    return total / count if count > 0 else 0


def compute_median(numbers):
    """Computes the median of a list of numbers manually."""
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    return sorted_numbers[mid]


def compute_mode(numbers):
    """
    Computes the mode of a list of numbers manually.
    Returns "#N/A" if multiple modes exist.
    """
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    max_freq = max(frequency.values(), default=0)
    modes = [num for num, freq in frequency.items() if freq == max_freq]
    return modes[0] if len(modes) == 1 else "#N/A"


def compute_variance(numbers, mean):
    """Computes variance manually."""
    total = sum((num - mean) ** 2 for num in numbers)
    return total / len(numbers) if numbers else 0


def compute_standard_deviation(variance):
    """Computes standard deviation manually."""
    return variance ** 0.5


def write_results_to_file(filename, results, execution_time):
    """
    Writes computed statistics and execution time to 'StatisticsResults.txt'.
    """
    output_filename = "StatisticsResults.txt"
    with open(output_filename, "a", encoding="utf-8") as file:
        file.write("==================================================\n")
        file.write(f"Results for {filename}:\n")
        for key, value in results.items():
            file.write(f"{key}: {value:.2f}\n" if isinstance(value, float) else f"{key}: {value}\n")
        file.write(f"Execution Time: {execution_time:.6f} seconds\n")
        file.write("==================================================\n\n")


def process_all_files(directory):
    """Processes all '.txt' files inside a given directory."""
    txt_files = [f for f in os.listdir(directory) if f.endswith('.txt')]

    if not txt_files:
        print("No text files found in the directory.")
        return

    for file in txt_files:
        file_path = os.path.join(directory, file)
        print(f"Processing: {file_path}")

        start_time = time.time()
        numbers = read_numbers_from_file(file_path)

        if not numbers:
            print(f"Error: No valid numbers found in {file}. Skipping...")
            continue

        mean = compute_mean(numbers)
        median = compute_median(numbers)
        mode = compute_mode(numbers)
        variance = compute_variance(numbers, mean)
        standard_deviation = compute_standard_deviation(variance)

        results = {
            "Mean": mean,
            "Median": median,
            "Mode": mode,
            "Variance": variance,
            "Standard Deviation": standard_deviation
        }

        execution_time = time.time() - start_time
        write_results_to_file(file, results, execution_time)
        print("Results saved to 'StatisticsResults.txt'.")


if __name__ == "__main__":
    DIRECTORY = "C:\\Users\\Compu\\Documents\\pythonProject2\\P1"
    process_all_files(DIRECTORY)

# exactly one blank line at the end
