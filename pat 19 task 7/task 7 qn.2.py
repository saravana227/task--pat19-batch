def read_and_display_text_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    file_name = "your_text_file.txt"  # Replace with the name of your text file
    read_and_display_text_file(file_name)