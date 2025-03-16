import os

filename = input("Enter the filename: ")

if os.path.exists(filename):
    if os.access(filename, os.R_OK):
        try:
            with open(filename, 'r') as file:
                data = file.read()
            modified_data = data.upper()

            with open('modified.txt', 'w') as new_file:
                new_file.write(modified_data)
            print("Modified file saved to modified.txt")
        except PermissionError:
            print(f"You do not have permission to read the file: {filename}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    else:
        print(f"You do not have permission to read the file: {filename}")
else:
    print(f"The file {filename} does not exist.")
