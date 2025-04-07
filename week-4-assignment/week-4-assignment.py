# I'll implement this using a function
def file_read(original_file, modified_file):
    try:
        with open(original_file, 'r') as infile:
            content = infile.read()
            modified_content = content.upper()

        with open(modified_file, 'w') as outfile:
            outfile.write(modified_content)
        print(f"File written successfully to {modified_file}.")
    except FileNotFoundError:
        print(f"Error: The file {original_file} was not found.")

file_read('original.txt', 'modified.txt')