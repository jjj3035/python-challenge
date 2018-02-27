import os
import csv

path1 = os.path.join('budget_data_1.csv')
path2 = os.path.join('budget_data_2.csv')

files = [path1, path2]
months = []
revenue = []

for file in files:
    with open(file, newline ='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter =',')
        csvreader.__next__()
        for row in csvreader:
            months.append(row[0])
            revenue.append(int(row[1]))
            
total_months = len(months)
total_revenue = sum(revenue)
average_revenue = total_revenue/len(months)
greatest_revenue = max(revenue)
greatest_revenue_month = months[revenue.index(greatest_revenue)]
least_revenue = min(revenue)
least_revenue_month = months[revenue.index(least_revenue)]

with open("output.txt", 'w+') as text_file:
    print ('Financial Analysis', file=text_file)
    print ('----------------------------', file=text_file)
    print ('Total Months:',total_months, file=text_file)
    print ('Total Revenue: $',total_revenue, file=text_file)
    print ('Average Revenue Change: $',int(average_revenue), file=text_file)
    print ('Greatest Increase in Revenue:',greatest_revenue_month,'($',greatest_revenue,')', file=text_file)
    print ('Greatest Decrease in Revenue:',least_revenue_month,'($',least_revenue,')', file=text_file)
    
with open('output.txt', 'r') as text_file:
    for line in text_file.readlines():
        print (line)
