import csv
import os
import datetime

path1 = os.path.join('employee_data1.csv')
path2 = os.path.join('employee_data2.csv')

files = [path1, path2]

emp_id = []
first_name = []
last_name = []
dob = []
ssn = []
state = []
state_abr = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

for file in files:
    with open(file, newline = '') as csvfile:
        csvreader = csv.reader(csvfile, delimiter =',')
        next(csvreader, None)
        for row in csvreader:
            emp_id.append(row[0])
            name = row[1].split()
            first_name.append(name[0])
            last_name.append(name[1])
            new_date_format = datetime.datetime.strptime(row[2], '%Y-%m-%d').strftime('%m/%d/%y')
            dob.append(new_date_format)
            new_ssn_format = '***-**-' + row[3][-4:]
            ssn.append(new_ssn_format)
            state.append(state_abr[row[4]])

new_csv = zip(emp_id, first_name, last_name, dob, ssn, state)

with open('employee_final.csv', 'w+', newline = '') as datafile:
    writer = csv.writer(datafile)
    writer.writerow(['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State'])
    writer.writerows(new_csv)


