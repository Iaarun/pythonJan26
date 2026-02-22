import csv

with open("annual-enterprise-survey.csv",'r', newline='') as csv_file:
      file=  csv.reader(csv_file)
      next(file) # skip the header row
      for line in file:
           #strip() method removes leading and trailing whitespace characters from a string.
          if not any(cell.strip() for cell in line):
              continue
          print(line[2], line[3], line[4])

