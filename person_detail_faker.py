from faker import Faker
import csv

# Initialize Faker instance
fake = Faker()

# Number of rows to generate
num_rows = 1000000

# Column headers (20 different columns)
columns = [
    'Full Name', 'Street Address', 'City', 'State', 'Zip Code', 'Country', 'Phone Number', 'Email', 'Date of Birth', 'Occupation', 
    'Company Name', 'Job Position', 'Website URL', 'Company Address', 'Preferred Language', 'Profile Picture URL', 'Marital Status',
    'Social Media Handle', 'Company Revenue', 'Last Updated'
]

# Open CSV file to write fake data
file_path = 'fake_data_20_columns.csv'
with open('fake_data_20_columns.csv', mode='w', newline='') as file:
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
            fake.phone_number(),
            fake.email(),
            fake.date_of_birth(minimum_age=18, maximum_age=80).isoformat(),
            fake.job(),
            fake.company(),
            fake.job(),
            fake.url(),
            fake.address().replace("\n", " "),
            fake.language_name(),
            fake.image_url(),
            fake.random_element(['Single', 'Married', 'Divorced']),
            fake.user_name(),
            fake.random_number(digits=9),
            fake.date_this_year().isoformat()
        ]
        writer.writerow(row)
print("file_generated_successfully")
