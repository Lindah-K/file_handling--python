# File Creation
try:
    # Open file in write mode ('w')
    with open("my_file.txt", "w") as file:
        # Write three lines of text to the file
        file.write("Line 1: This is a sample text.\n")
        file.write("Line 2: 12345\n")
        file.write("Line 3: Python is awesome!\n")
        print("File created and initial content written successfully.")
except Exception as e:
    print(f"An error occurred while creating the file: {e}")
finally:
    print("File creation process completed.\n")

# File Reading and Display
try:
    # Open file in read mode ('r')
    with open("my_file.txt", "r") as file:
        # Read and display the contents of the file
        print("Contents of 'my_file.txt':")
        print(file.read())
except Exception as e:
    print(f"An error occurred while reading the file: {e}")
finally:
    print("File reading process completed.\n")

# File Appending
try:
    # Open file in append mode ('a')
    with open("my_file.txt", "a") as file:
        # Append three additional lines of text to the file
        file.write("Line 4: Appended line 1.\n")
        file.write("Line 5: 54321\n")
        file.write("Line 6: Python is versatile!\n")
    print("Additional content appended to the file successfully.")
except Exception as e:
    print(f"An error occurred while appending to the file: {e}")
finally:
    print("File appending process completed.\n")

# Error Handling
try:
    # Open file in read mode ('r')
    with open("nonexistent_file.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found error: The specified file does not exist.")
except PermissionError:
    print("Permission error: You do not have permission to access the file.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("Error handling process completed.")
