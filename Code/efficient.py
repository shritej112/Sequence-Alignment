import sys
from time import time
from os import makedirs, path
from psutil import Process
# import numpy as np

# Gap and Mismatch penalties
DELTA = 30
ALPHA = {
    ('A', 'A'): 0, ('A', 'C'): 110, ('A', 'G'): 48, ('A', 'T'): 94,
    ('C', 'A'): 110, ('C', 'C'): 0, ('C', 'G'): 118, ('C', 'T'): 48,
    ('G', 'A'): 48, ('G', 'C'): 118, ('G', 'G'): 0, ('G', 'T'): 110,
    ('T', 'A'): 94, ('T', 'C'): 48, ('T', 'G'): 110, ('T', 'T'): 0
}

def generate_string(lines, lines_count, base_string_index):
    """Generates the final string based on the base string and insertion indices."""

    intermediate_strings = [lines[base_string_index].strip()]
    line_index = base_string_index + 1

    while (line_index < lines_count and lines[line_index].strip().isdigit()):
        previous_string = intermediate_strings[line_index-base_string_index-1]
        insertion_position = int(lines[line_index].strip())
        generated_string = previous_string[:insertion_position+1] + previous_string + previous_string[insertion_position+1:]
        intermediate_strings.append(generated_string)
        line_index = line_index + 1
        # print(f"Initial string: {previous_string}, Insertion at: {insertion_position}, Resultant string: {generated_string}")

    return intermediate_strings, line_index

def read_input(file_path):
    """Reads the input file and generates the two strings to be aligned."""
    try:

        with open(file_path, 'r', encoding='UTF-8') as file:
            lines = file.readlines()
            lines_count = len(lines)
        
        # print(f"Read the {lines_count} lines into a list - {lines}\n")
       
        # Assuming the first sequence and its insertions are properly separated by line breaks
        s, next_string_index = generate_string(lines, lines_count, 0)
        # print(f"Starting from the initial string {s[0]}, generated the first sequence {s[-1]}.")
        # print(f"Next sequence is at {next_string_index}.")

        # The second sequence starts after the first sequence and its insertions
        t, next_string_index = generate_string(lines, lines_count, next_string_index)
        # print(f"Starting from the initial string {t[0]}, generated the second sequence {t[-1]}.")
        # print(f"Read all {lines_count} lines.\n")
        
        return s[-1], t[-1]

    except Exception as e:
        # print(f"An error occurred while processing the input file")
        raise e

def basic_sequence_alignment(X, Y):
    try:

        m, n = len(X), len(Y)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Initialize DP table for gaps
        for i in range(m + 1):
            dp[i][0] = i * DELTA
        for j in range(n + 1):
            dp[0][j] = j * DELTA

        # print(f"Initialized DP matrix:\n{np.matrix(dp)}")

        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                match_cost = dp[i - 1][j - 1] + ALPHA[(X[i - 1], Y[j - 1])]
                delete_cost = dp[i - 1][j] + DELTA
                insert_cost = dp[i][j - 1] + DELTA
                dp[i][j] = min(match_cost, delete_cost, insert_cost)

        # print(f"Cost of the optimal solution is: {dp[m][n]}\nFinal DP matrix:\n{np.matrix(dp)}")

        # Backtrack to find the alignment
        align_X, align_Y = '', ''
        i, j = m, n
        while i > 0 and j > 0:
            if dp[i][j] == dp[i - 1][j - 1] + ALPHA[(X[i - 1], Y[j - 1])]:
                align_X = X[i - 1] + align_X
                align_Y = Y[j - 1] + align_Y
                i -= 1
                j -= 1
            elif dp[i][j] == dp[i - 1][j] + DELTA:
                align_X = X[i - 1] + align_X
                align_Y = '_' + align_Y
                i -= 1
            else:
                align_X = '_' + align_X
                align_Y = Y[j - 1] + align_Y
                j -= 1
        
        # Handle remaining characters
        while i > 0:
            align_X = X[i - 1] + align_X
            align_Y = "_" + align_Y
            i -= 1
        while j > 0:
            align_X = "_" + align_X
            align_Y = Y[j - 1] + align_Y
            j -= 1

        # print(f"Alignment:\n{align_X}\n{align_Y}")
        
        return dp[m][n], align_X, align_Y
    
    except Exception as e:
        # print(f"An error occurred while running the algorithm")
        raise e

def linear_space_alignment(X, Y, reverse):
    m, n = len(X), len(Y)

    # Initialize the DP table - 2 rows of length n+1, with all values set to 0
    dp = []
    for _ in range(2):
        dp.append([0] * (n + 1))

    # Initialize the DP table for gaps
    for j in range(n + 1):
        dp[0][j] = j * DELTA

    for i in range(1, m + 1):
        dp[1][0] = i * DELTA
        for j in range(1, n + 1):
            # If called for the right half of the split substring of X, reverse it   
            if reverse:    
                cost_substitute = dp[0][j - 1] + ALPHA[(X[m - i], Y[n - j])]
            # If called for the left half of the split substring of X
            else:
                cost_substitute = dp[0][j - 1] + ALPHA[(X[i - 1], Y[j - 1])]
            
            cost_delete = dp[0][j] + DELTA
            cost_insert = dp[1][j - 1] + DELTA

            # Choose the minimum cost
            dp[1][j] = min(cost_substitute, cost_delete, cost_insert)
        
        # For the next iteration, the current row becomes the previous row
        for j in range(n + 1):
            dp[0][j] = dp[1][j]
    

    return dp[1]

def divide_conquer(X, Y):
    try:

        m, n = len(X), len(Y)
        if (m < 2 or n < 2):
            return basic_sequence_alignment(X, Y)
        else:
            # Split the first sequence
            first_half = linear_space_alignment(X[:m//2], Y, False)
            second_half = linear_space_alignment(X[m//2:], Y, True)

            # Find the split point which minimizes the total cost
            split_points = [first_half[j] + second_half[n - j] for j in range(n + 1)]
            split_point = split_points.index(min(split_points))

            # Recusrively solve the two subproblems
            left_cost, left_align_X, left_align_Y = divide_conquer(X[:m//2], Y[:split_point])
            right_cost, right_align_X, right_align_Y = divide_conquer(X[m//2:], Y[split_point:])

        return left_cost+right_cost, left_align_X+right_align_X, left_align_Y+right_align_Y
    
    except Exception as e:
        # print(f"An error occurred while running the divide and conquer step.")
        raise e

def main(input_file, output_file):
    try:

        X, Y = read_input(input_file)
        start_time = time()
        cost, align_X, align_Y = divide_conquer(X, Y)
        execution_time = (time() - start_time) * 1000
        memory_usage = Process().memory_info().rss / 1024
        # print(f"\nExecution Time: {execution_time:.6f} ms\nMemory Used: {int(memory_usage)} kb\n")

        # Get the directory from the output file path
        output_dir = path.dirname(output_file)
        
        if output_dir:
            makedirs(output_dir, mode=0o777, exist_ok=True)
            
        with open(output_file, 'w') as file:
            file.write(f"{cost}\n")
            file.write(f"{align_X}\n")
            file.write(f"{align_Y}\n")
            file.write(f"{execution_time:.6f}\n")
            file.write(f"{int(memory_usage)}")

    except Exception as e:
        # print(f"An error occurred while running the program: {e}")
        raise e

if __name__ == "__main__":
    if len(sys.argv) != 3:
        # print("Usage: python script.py <input_file> <output_file>")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])
