import csv
import re

def read_csv(file_name, country_name):
    with open(file_name, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        header = next(csv_reader)
        data = []
        for row in csv_reader:
          iterable = zip(header, row)
          if row[2] == country_name:
            country = { re.compile(r'\d+').findall(key)[0]: int(value) for key, value in iterable  if re.compile(r'\d+').findall(key) != []  != None and value.isdigit()   }
            data.append(country)
            break
          else:
            continue
        return data[0]


if __name__ == "__main__":
    data = read_csv("./app/data.csv", "Venezuela")
    print(data)