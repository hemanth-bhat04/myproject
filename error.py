file_path = 'file_does_not_exist.txt'

try:
    with open(file_path, 'r') as file:
        content = file.read()
    # Additional file processing code can go here
except FileNotFoundError:
    print(f"The file '{file_path}' does not exist.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

large_list=[0]*(10**9)
