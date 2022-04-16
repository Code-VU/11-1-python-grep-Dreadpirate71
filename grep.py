import re
import string
import sys


def countpatterninfile():
    regular_expression = input("Enter a regular expression: ")
    countLines = 0
    file_name = "mbox-long.txt"
    file_handle = open (file_name)
    for line in file_handle:
        if re.search(regular_expression, line):
            countLines = countLines + 1
    print ("mbox.txt had", countLines, "lines that matched", regular_expression)

if __name__ == '__main__':
    # this is called a main method
    # This is another way of telling python THIS IS WHERE YOU SHOULD START RUNNING
    # When this is included, python will begin with the code in this block first
    countpatterninfile()