import csv
header = ['name', 'area', 'country_code2', 'country_code3']
data1 = ['Afganistan', 652090, 'AF', 'AFG']
data2 = {'India', 30153, 'set', 'set2'}
data3 = {'Country': 'SriLanka', 'Code': 565656, 'CCC': 'SRL', 'CSV': 'Lanka'}
with open('countries.csv',  'w') as f:
    writer =csv.writer(f)
    #write the header
    writer.writerow(header)
    #write the data
    writer.writerow(data1)
    writer.writerow(data2)
    writer.writerow(data3)

  #writing multiple data into the csv
with open('countries.csv', 'w') as f:
    writer = csv.writer(f)
    data = [
        ['India', 28748, 'AI', 'AIB'],
        ['Norway', 45875, 'WOW', 'ABD']
    ]
    writer.writerows(data)
print("Writing of data successfully done")

#Reading Multiple data d=from CSV

with open('countries.csv', 'r') as f:
    csvreader = csv.reader(f)
    header = next(csvreader)
    print(header)
    rows = []
    for row in csvreader:
        rows.append(row)
        print(rows)

        #printing total noof rows in file
print("Total no of rows : %d" % (csvreader.line_num))
print("Printing of data successfully done")
