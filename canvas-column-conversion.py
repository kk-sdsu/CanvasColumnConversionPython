# Author: Kyle Krick kkrick@sdsu.edu

# Summary: This program automates the matching of key columns from SIMS (Student Information Management System)
# to CS (Campus Solutions) for the CSV files for courses and sections which are uploaded to Canvas. 
# At the time of writing, SDSU is switching from SIMS to CS and the key columns are different in CS, 
# so the output file will help Canvas convert their keys from SIMS to those that will be coming from CS.
import csv

# Gets necessary input from the user for running this program 
# (i.e.: file_type, sims_filepath, cs_filepath, and output_filepath)
def get_input():
    input_dict = {
        "file_type": "",
        "sims_filepath": "",
        "cs_filepath": "",
        "output_filepath": ""
    }

    input_dict["file_type"] = input("File type ('courses' or 'sections'): ")
    input_dict["sims_filepath"] = input("Enter path to SIMS file for conversion: ")
    input_dict["cs_filepath"] = input("Enter path to CS file for conversion: ")
    input_dict["output_filepath"] = input("Enter path to ouptut file for conversion: ")

    return input_dict

# Attempts to read in the filepath. Assumes that the file is a CSV with ',' as the separator.
# Returns a promise that, if successful, evaluates to an array of objects, one for each of the rows (excluding headers).
# Otherwise returns a promise that evaluates to an error.
def read_file(filepath):
    try:
        file = open(filepath)
        file_contents = []
        csv_reader = csv.DictReader(file)
        
        for row in csv_reader:
            file_contents.append(row)

        return file_contents
    except:
        return ""    

# Returns validation object. If all checks pass then
# successful = true and file_type, sims_filepath, cs_filepath and output_filepath are assigned their values from the user input.
# Otherwise successful = false, and all other properties remain empty strings.
def validate_input(input_dict):
    validated_inputs = input_dict
    validated_inputs["validated"] = True

    valid_file_types = {"courses", "sections"}

    if input_dict["file_type"] not in valid_file_types:
        print(f"Error: file_type must be one of: {valid_file_types}")
        validated_inputs["validated"] = False

    for input_item in input_dict:
        if input_dict[input_item] == "":
            print("Error: " + input_item + " cannot be blank.")
            validated_inputs["validated"] = False
    
    if len(input_dict["sims_filepath"]) > 0:
        validated_inputs["sims_file_contents"] = read_file(input_dict["sims_filepath"])
        if len(validated_inputs["sims_file_contents"]) == 0:
            print(f"Error: SIMS file at {input_dict['sims_filepath']} was empty. Please provide a file with data.")
            validated_inputs["validated"] = False

    if len(input_dict["cs_filepath"]) > 0:
        validated_inputs["cs_file_contents"] = read_file(input_dict["cs_filepath"])
        if len(validated_inputs["cs_file_contents"]) == 0:
            print(f"Error: CS file at {input_dict['cs_filepath']} was empty. Please provide a file with data.")
            validated_inputs["validated"] = False

    if validated_inputs["validated"] == False:
        print("Please re-run the program and correct the errors above.")        
    
    return validated_inputs

# Converts the column_string to an intermediary state for matching between SIMS and CS as follows:
# - For Sections and Courses:
# -- Trims any leading or following whitespace
# -- Replaces '_' with ' '
# -- Replaces '-ExtEd' with '-GLBL'
# -- Removes last two chars for CS columns containing four chars between the first two dashes
# -- Trims off semester names after the first 3 chars
# -- Returns the column in it's intermediary state
# -- Examples:
# --- Given the SIMS column 'INT_S799B-Y1-Spring2022-ExtEd' 
#     this function would return 'INT S799B-Y1-Spr2022-GLBL'
# --- Given the CS column 'INT S799B-Y1NT-Spr2022-GLBL' 
#     this function would return 'INT S799B-Y1-Spr2022-GLBL'
def convert_column(column_string):
    column = column_string
    column = column.strip()
    column = column.replace('_',' ')
    column = column.replace('-ExtEd', '-GLBL')

    first_dash_index = column.index('-')
    second_dash_index = column.index('-', first_dash_index + 1)

    # Most CS IDs have 2 extra chars between the first two dashes that need to be removed for matching
    # Example, given column "INT_S799B-Y1NT-Spring2022-ExtEd"
    # second_dash_index = 14, remove index 12 "N" & 13 "T" and update second dash index
    # Result will be column_list = "INT_S799B-Y1-Spring2022-ExtEd", second_dash_index = 12
    if second_dash_index - first_dash_index == 5:
        column_list = list(column)
        
        del column_list[(second_dash_index - 2) : second_dash_index]
        second_dash_index -= 2

        column = ''.join(column_list)

    column_right_string = column[second_dash_index:]
    column_right_list = list(column_right_string)
    year_first_index = 0

    for index in range(len(column_right_list)):
        if (column_right_list[index].isdigit()):
            year_first_index = second_dash_index + index
            break
    
    column_left_string = column[0:(second_dash_index + 4)]
    column_right_string = column[year_first_index:]
    column = column_left_string + column_right_string

    return column

# Used when file_type is 'courses'
# Assumes both SIMS and CS CSVs use "Course_ID" for the header of the course id column
def convert_courses(file_contents):
    contents = file_contents
    converted_courses = []

    # Make sure that the CSV header is 'Course_ID',
    # instruct user to check the file if the header does not match
    if 'Course_ID' not in contents[0]:
        print('When converting courses, please ensure that the CSV\'s header for course is \'Course_ID\'.');
        return converted_courses
    
    for index in range(len(contents)):
        course_row = contents[index]
        course_id = course_row["Course_ID"]
        converted_courses.append({
            'converted_column_id': convert_column(course_id),
            'original_column_id': course_id
        })
    
    return converted_courses

# Used when fileType arg is 'sections'
# Assumes both SIMS and CS CSVs use "Section_id" for the header of the section id column
def convert_sections(file_contents):
    print("convert_sections funtion stub")

# Matches the columns between SIMS and CS based on their intermediary state
# Assumes both sets of columns have already been converted to their intermediary state
# Returns an array of objects with properties 'columnIDSIMS', the original SIMS column, and 'columnIDCS', the CS column match or empty string if none was found
def match_columns(souce_columns, destination_columns):
    print("match_columns function stub")

# Outputs the matched columns to the specified filepath using the specified columnName where _SIMS and _CS are appended
# Assumes the columns from SIMS and CS have already been matched
def output_converted_columns(matched_columns, output_filepath, column_name):
    print("output_converted_columns function stub")

# Validates the args passed in and if validation is successful then reads the
# files, converts and matches the columns and outputs to the specified output_filepath
# Otherwise relies on validate_input() to communicate any issues to the user
def canvas_column_conversion():
    print("~~~Canvas Column Conversion~~~")

    validated_inputs = validate_input(get_input())

    if validated_inputs["validated"]:
        print("Validation succeeded. Continuing on...")
        sims_converted_courses = convert_courses(validated_inputs["sims_file_contents"])
        print(sims_converted_courses)
        cs_converted_courses = convert_courses(validated_inputs["cs_file_contents"])
        print(cs_converted_courses)

canvas_column_conversion()