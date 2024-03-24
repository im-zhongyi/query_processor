import pandas as pd
import re

#input parameter
in_sheet_name=""
in_column_name=""

#variable
file_loc = "SampleColumn.xlsx"
df = pd.read_excel(file_loc, sheet_name='Sheet1') #, usecols="B"
column = df["Column name"]
strings = ["Name","acc,","ads"]
for row in column:
    for string in strings:
        if (row not in string):
            print ( row, " : ",string," : ", row == string )        
            break
# print ( "Table name" in df.columns)
# table = [column.strip() for column in df.to_string().split('\n')]
# print(table)
# column_header = (column.strip() for column in table.tostring().split)


# column_names_no_header = column_names[1:] # remove header row in excel
# def format_data_frame(strList):
# for column in column_names_no_header:
#     result = column[1:].strip()
#     print(result)
#     if (result=="ID"):        
#         print(result)
# print(df.to_string().split('\d'))
# for column in column_names:
#     print(column)


# text = "select ID, amount, name, payment_method from customer;"
# pattern = re.compile(r'\bSELECT\b(.*?)\bFROM\b', re.IGNORECASE | re.DOTALL)
# match = pattern.search(text)

# if match:         
#     columns_part = match.group(1).strip()
#     # Split the columns using commas and remove any leading/trailing spaces
#     column_names = [col.strip() for col in columns_part.split(',')]
# else:
#     print("No match found.")      

# original_list = ['"item1"', '"item2"', '"item3"']

# # Method 1: Using list comprehension and strip()
# stripped_list_1 = [item.strip('"\'') for item in original_list]

# # Method 2: Using map() and lambda function with strip()
# stripped_list_2 = list(map(lambda x: x.strip(), original_list))

# # Print the results
# print("Original List:", original_list)
# print("Stripped List (Method 1):", stripped_list_1)
# print("Stripped List (Method 2):", stripped_list_2)