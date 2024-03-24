import pandas as pd
import re

def extract_column_names_from_query(select_query):
    # Use regular expression to extract column names from the SELECT query
    pattern = re.compile(r'\bSELECT\b(.*?)\bFROM\b', re.IGNORECASE | re.DOTALL)
    match = pattern.search(select_query)

    if match:
        columns_part = match.group(1).strip()
        # Split the columns using commas and remove any leading/trailing spaces
        column_names = [col.strip().upper() for col in columns_part.split(',')]
        return column_names
    else:
        return None
    
def extract_column_names_from_excel(file_loc, sheet_name,column_name):
    file_loc = file_loc
    df = pd.read_excel(file_loc, sheet_name= sheet_name) #, usecols="B"
    column = df[column_name]
    column = [rows.upper() for rows in column]
    return column

def print_result(list_column_found, columns_not_in_excel,columns_not_in_query):
    print("Columns found in both query and excel:")
    if list_column_found:
        for column_found in list_column_found:        
            print (column_found)
        if columns_not_in_excel:
            print("\nColumns not found in excel:")
            for column in columns_not_in_excel:
                print(column)
        else:
            print("All columns in excel matched with query.")
        if columns_not_in_query:
            print("\nColumns not found in query:")
            for column in columns_not_in_query:
                print(column)
        else:
            print("All columns in query matched with excel.")        
    else:
        print("All columns are unmatched.")
    
def main():

    # Get the SELECT query from the user
    select_query = input("Enter a SELECT query: ")
    file_loc = input("Enter file path: ")
    sheet_name = input("Enter sheet name: ")
    column_name = input("Enter column name: ")
    # Extract column names from the SELECT query
    column_names_from_query = extract_column_names_from_query(select_query)
    column_names_from_excel = extract_column_names_from_excel(file_loc, sheet_name, column_name)
    list_column_found =[]
    columns_not_in_excel=""
    columns_not_in_query=""
    if column_names_from_query:       
        columns_not_in_excel = list(set(column_names_from_query)-set(column_names_from_excel))
        columns_not_in_query = list(set(column_names_from_excel)-set(column_names_from_query))
        for row_query in column_names_from_query:
            for row_excel in column_names_from_excel:
                if (row_query in row_excel):
                    list_column_found.append(row_excel)
                    break
    else:
        print("Invalid SELECT query. Unable to extract column names.")
    print_result(list_column_found,columns_not_in_excel,columns_not_in_query)
if __name__ == "__main__":
    main()
