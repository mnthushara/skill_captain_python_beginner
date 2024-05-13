file_path = "C:\Git-Terraform-Azure\data.txt"

try:
    with open(file_path, "r") as f:
        for line in f:
            print(line.strip())  # Use strip() to remove newline characters
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
except IOError as e:
    print(f"Error: Unable to open file '{file_path}': {e}")
