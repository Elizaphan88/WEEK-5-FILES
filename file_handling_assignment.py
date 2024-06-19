# File Creation
try:
    # Open file in write mode ('w')
    with open("my_file.txt", "w") as file:
        # Writing lines to the file
        file.write("This is line 1\n")
        file.write("12345\n")  # Writing a mix of string and number
        file.write("Another line here\n")
        print("File 'my_file.txt' created and initial content written.")
except PermissionError:
    print("Permission denied to create 'my_file.txt'.")
except Exception as e:
    print(f"Error occurred: {e}")
finally:
    print("File creation process completed.\n")

# File Reading and Display
try:
    # Open file in read mode ('r')
    with open("my_file.txt", "r") as file:
        # Reading and printing contents
        file_contents = file.read()
        print(f"Contents of 'my_file.txt':\n{file_contents}")
except FileNotFoundError:
    print("File 'my_file.txt' not found.")
except PermissionError:
    print("Permission denied to read 'my_file.txt'.")
except Exception as e:
    print(f"Error occurred: {e}")
finally:
    print("File reading process completed.\n")

# File Appending
try:
    # Open file in append mode ('a')
    with open("my_file.txt", "a") as file:
        # Appending additional lines
        file.write("Appending line 1\n")
        file.write("789\n")  # Appending a mix of string and number
        file.write("Final line appended\n")
    print("Additional content appended to 'my_file.txt'.")
except PermissionError:
    print("Permission denied to append to 'my_file.txt'.")
except Exception as e:
    print(f"Error occurred: {e}")
finally:
    print("File appending process completed.")

