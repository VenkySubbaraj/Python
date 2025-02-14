from faker import Faker
import csv

# Initialize Faker instance
fake = Faker()

# Number of rows to generate
num_rows = 10000000

# Column headers
columns = [
    'Name', 'Address', 'City', 'State', 'Zip', 'Country', 'Email', 'Phone Number', 'Birthday', 'Company', 'Job Title', 'SSN', 
    'Credit Card Number', 'Credit Card Expiry', 'Company Email', 'Website', 'Profile URL', 'Gender', 'Language',
    'Account Number', 'Routing Number', 'Employee ID', 'Date of Hire', 'Salary', 'Department', 'Manager', 'Skills'
]

# Open CSV file to write fake data
with open('fake_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Write header
    writer.writerow(columns)
    
    # Generate fake data and write rows
    for _ in range(num_rows):
        row = [
            fake.name(),
            fake.address().replace("\n", " "),
            fake.city(),
            fake.state(),
            fake.zipcode(),
            fake.country(),
            fake.email(),
            fake.phone_number(),
            fake.date_of_birth(minimum_age=18, maximum_age=80).isoformat(),
            fake.company(),
            fake.job(),
            fake.ssn(),
            fake.credit_card_number(),
            fake.credit_card_expire(),
            fake.company_email(),
            fake.url(),
            fake.profile().get('username', 'N/A'),
            fake.random_element(['M', 'F']),
            fake.language_name(),
            fake.random_number(digits=10),
            fake.uuid4(),
            fake.date_this_century().isoformat(),
            fake.random_number(digits=6),
            fake.random_element(['HR', 'IT', 'Finance', 'Sales']),
            fake.name(),
            fake.random_element(['Python', 'Java', 'SQL', 'Excel']),
            fake.ssn()
        ]
        writer.writerow(row)

print("Data generated successfully and saved in 'fake_data.csv'.")
