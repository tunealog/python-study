# Basic of Python

# Title : Quiz(File)
# Date : 2020-07-01
# Creator : tunealog

# Quiz) File Create Program
#
# Create the program to create a report file from 1 ~ 50 week
#
# Rule1 : The report is 1time for a week
# Rule2 : File name is Week 1.txt, Week 2.txt, ...
#
# Example (Result):
# - Week 3 Weekly Report
# Department :
# Name :
# Summary of Task :

import pickle

for week in range(1, 51):

    with open(f"Week {week}.txt", "w", encoding="utf8") as report_file:
        report_file.write(f"- Week {week} Weekly Report\n")
        report_file.write("Department : \n")
        report_file.write("Name : \n")
        report_file.write("Summary of Task : ")
