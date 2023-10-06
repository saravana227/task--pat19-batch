import datetime

def write_timestamp_to_file(filename):
    current_time = datetime.datetime.now()
    timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")
    
    with open(filename, "w") as file:
        file.write(timestamp)

if __name__ == "__main__":
    file_name = "timestamp.txt"
    write_timestamp_to_file(file_name)
    print(f"Timestamp written to '{file_name}' successfully.")