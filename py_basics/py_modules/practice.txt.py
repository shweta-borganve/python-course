def read_specific_line(file_path, line_number):
    try:
        with open(file_path, 'r') as file:
            for current_line_number,line in enumerate(file, start=1):
                file_path = 'practice.txt'
                line_number = 10
                line_content = read_specific_line(file_path,line_number)
print(f"Line {line_number}: {line_content}")