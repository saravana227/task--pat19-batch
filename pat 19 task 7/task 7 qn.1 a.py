import datetime

def create_text_file_with_timestamp():
    current_time = datetime.datetime.now()
    timestamp = current_time.strftime("%Y-%m-%d_%H-%M-%S")
    file_name = f"file_{timestamp}.txt"
    
    with open(file_name, "w") as file:
        file.write(f"This is a text file created at {current_time}.")

if __name__ == "__main__":
    create_text_file_with_timestamp()
    print("Text file with timestamp created successfully.")