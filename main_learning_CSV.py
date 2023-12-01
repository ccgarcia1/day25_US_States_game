# with open(r"weather_data.csv", mode="r") as data_file:
#     data = data_file.readlines()
#     print(data)

#example in how it'd be without Pandas Library
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     #print(data)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)
#         #print(row[1])

import pandas
from pexpect.ANSI import term

data = pandas.read_csv("weather_data.csv")
# print(type(data["condition"]))
# print(data["condition"])
data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
#average in Python
print(sum(temp_list) / len(temp_list))

#another way to do the average in Python
print(data["temp"].max())

#Get Data in Columns
print(data["condition"])
#Another way to call the column Pandas implicitly get the name of the first column
print(data.condition)


#Get data in the row
print(data[data.day == "Monday"])

#Getting  the day where the temperature was max
print("--------------")
print(data[data.temp == data.temp.max()])

#Creating a dataFrame from scratch
data_dict = {
    "students":["Amy","James","Angela"],
    "scores":[76,56,65]
}
data_from_scratch = pandas.DataFrame(data_dict)
print(data_from_scratch)
data.to_csv("new_data.csv")