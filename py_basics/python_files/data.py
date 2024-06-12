import csv

# Open the CSV file
with open('data.csv', mode='r') as file:
    # Create a CSV reader object
    csv_reader = csv.DictReader(file)

    # Read each row and assign to variables
    rows = list(csv_reader)  # Convert the reader object to a list

    # Assuming there are exactly three rows (excluding the header)
    row1 = rows[0]
    row2 = rows[1]
    row3 = rows[2]

    # Assign variables for each row
    name1, age1 = row1['name'], row1['age']
    name2, age2 = row2['name'], row2['age']
    name3, age3 = row3['name'], row3['age']

    # Print each entry individually
    print(f"Name: {name1}, Age: {age1}")
    print(f"Name: {name2}, Age: {age2}")
    print(f"Name: {name3}, Age: {age3}")

    age1 = int(age1)+1
    age2 = int(age2)+1
    age3 = int(age3)+1
    print(f"Name: {name1}, Age: {age1}")
    print(f"Name: {name2}, Age: {age2}")
    print(f"Name: {name3}, Age: {age3}")
