
import sys

def power_of_four(n):
    return n ** 4

def process_test_case(x_remaining, current_sum, numbers_list):
    if x_remaining == 0:
        return current_sum

    try:
        num_str = numbers_list[len(numbers_list) - x_remaining]
        num = int(num_str)
    except (IndexError, ValueError):
        return -1 # Mismatch in X and number of Yn

    if num <= 0:
        current_sum += power_of_four(num)

    return process_test_case(x_remaining - 1, current_sum, numbers_list)

def read_numbers_line(line_index, lines):
    if line_index >= len(lines):
        return None, None
    
    try:
        x = int(lines[line_index].strip())
    except ValueError:
        return None, None

    if line_index + 1 >= len(lines):
        return None, None

    numbers_line = lines[line_index + 1].strip()
    numbers_list = numbers_line.split()

    if len(numbers_list) != x:
        return -1, line_index + 2 # Indicate error and next line index

    return numbers_list, line_index + 2

def process_all_test_cases(n_remaining, current_line_index, lines, results):
    if n_remaining == 0:
        return results

    if current_line_index >= len(lines):
        return results # Not enough input

    x_str = lines[current_line_index].strip()
    try:
        x = int(x_str)
    except ValueError:
        # Handle malformed input for X, though problem statement implies valid N, X
        results.append(-1)
        return process_all_test_cases(n_remaining - 1, current_line_index + 1, lines, results)

    numbers_list_or_error, next_line_index = read_numbers_line(current_line_index, lines)

    if numbers_list_or_error == -1:
        results.append(-1)
        return process_all_test_cases(n_remaining - 1, next_line_index, lines, results)
    elif numbers_list_or_error is None:
        # This means there was an issue reading X or the numbers line
        results.append(-1) # Or handle as per problem spec for incomplete input
        return process_all_test_cases(n_remaining - 1, current_line_index + 2, lines, results)

    test_case_result = process_test_case(x, 0, numbers_list_or_error)
    results.append(test_case_result)

    return process_all_test_cases(n_remaining - 1, next_line_index, lines, results)

def main():
    input_lines = sys.stdin.readlines()
    if not input_lines:
        return

    try:
        n = int(input_lines[0].strip())
    except ValueError:
        return # Malformed N

    results = process_all_test_cases(n, 1, input_lines, [])

    sys.stdout.write("\n".join(map(str, results)))

if __name__ == "__main__":
    main()
