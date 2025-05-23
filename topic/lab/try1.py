# try:
#     user_input = input("Please enter an integer: ")
#     # 13 = "13" -> 13
#     # abc = error
#     number = int(user_input)
#     print(f"You entered: {number}")
# except ValueError:
#     print(f"Error: '{user_input}' is not a valid integer. Please try again.")


# file_reader_errors.py

def count_lines_in_file(filename):
    line_count = 0
    try:
        with open(filename, 'r') as file:
            for line in file:
                line_count += 1
                # line_count = line_count + 1
        print(f"The file '{filename}' has {line_count} lines.")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred while processing '{filename}': {e}")
    finally:
        print(f"Attempted to read file '{filename}'.")

if __name__ == "__main__":
    file_to_read = input("Enter the filename to read: \n")
    count_lines_in_file(file_to_read)
