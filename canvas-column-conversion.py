# Author: Kyle Krick kkrick@sdsu.edu

# Summary: This program automates the matching of key columns from SIMS (Student Information Management System)
# to CS (Campus Solutions) for the CSV files for courses and sections which are uploaded to Canvas. 
# At the time of writing, SDSU is switching from SIMS to CS and the key columns are different in CS, 
# so the output file will help Canvas convert their keys from SIMS to those that will be coming from CS.

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
    

# Returns validation object. If all checks pass then
# successful = true and file_type, sims_filepath, cs_filepath and output_filepath are assigned their values from the user input.
# Otherwise successful = false, and all other properties remain empty strings.
def validate_input(input_dict):
    validated_inputs = {
        "validation_successful": True,
        "file_type": "",
        "sims_filepath": "",
        "cs_filepath": "",
        "output_filepath": ""
    }

    valid_file_types = {"courses", "sections"}

    if input_dict["file_type"] not in valid_file_types:
        print(f"Error: file_type must be one of: {valid_file_types}")
        validated_inputs["validation_successful"] = False

    for input_item in input_dict:
        if input_dict[input_item] == "":
            print("Error: " + input_item + " cannot be blank.")
            validated_inputs["validation_successful"] = False

    if validated_inputs["validation_successful"] == False:
        print("Please re-run the program and correct the errors above.")
    
    return validated_inputs
    

# Attempts to read in the filepath. Assumes that the file is a CSV with ',' as the separator.
# Returns a promise that, if successful, evaluates to an array of objects, one for each of the rows (excluding headers).
# Otherwise returns a promise that evaluates to an error.
def read_file(filepath):
    print("read_file function stub")

# Converts the columnString to an intermediary state for matching between SIMS and CS as follows:
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
def convert_column(raw_column):
    print("convert_column function stub")

# Used when fileType arg is 'courses'
# Assumes both SIMS and CS CSVs use "Course_ID" for the header of the course id column
def convert_courses(file_contents):
    print("convert_course function stub")

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
    if validated_inputs["validation_successful"]:
        print("Validation succeeded. Continuing on...")

canvas_column_conversion()