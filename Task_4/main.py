from modules.utils import read_scores, calculate_average, write_result

def main():
    try:
        scores = read_scores("scores.txt")  # Read scores from file
        average = calculate_average(scores)  # Calculate average
        write_result("results.txt", average)  # Write result to output file
        print("Average written successfully.")
    except FileNotFoundError:
        print("Error: The file was not found.")
    except ValueError as e:
        print(f"Error: One of the scores is invalid. Details: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()

