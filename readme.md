# Canvas Column Conversions

**Author**: Kyle Krick <kkrick@sdsu.edu>

**Summary**: This program automates the matching of key columns from SIMS (Student Information Management System)
to CS (Campus Solutions) for the CSV files for courses and sections which are uploaded to Canvas.
At the time of writing, SDSU is switching from SIMS to CS and the key columns are different in CS, so the
output file will help Canvas convert their keys from SIMS to those that will be coming from CS.

## To Run

### Docker
There is a publicly available docker image at https://hub.docker.com/repository/docker/kkricksdsu/canvascolumnconversions

On first run:

- Mac/Linux:
  - ```docker run -it --name c3 -v $(pwd):/usr/src/app/data kkricksdsu/canvascolumnconversions:latest```

- Windows (PowerShell):

  - ```docker run -it --name c3 -v ${pwd}:/usr/src/app/data kkricksdsu/canvascolumnconversions:latest```

Starting container after first run:
- ```docker container start -ai c3```

### Python Locally
Alternatively, you can download the source code and run locally on Python 3:

- ```python canvas-column-conversion.py```

## Usage
The app will ask for the following input via commandline:
- file_type - either 'course' or 'section'
- sims_filepath - Path to SIMS CSV file*
- cs_filepath - Path to CS CSV file*
- output_filepath - Path to output CSV file*

*If running on docker, recommend using "./data/{file_name}.csv" as the ./data directory in the container will map to the directory on your computer where this container is being run from.

### Docker Container Example Data
The docker container has example data for you to test with under /usr/src/app/example:
- cs_courses.csv
- cs_sections.csv
- sims_courses.csv
- sims_sections.csv
- out.csv

This can be accessed during runtime via "./example/{file_name}.csv"

## Output
After running this successfully, you should have your output file in your specified directory. The file outputs 3 columns "old", "new" and "type" where old is the SIMS column ID, new is the CS column ID and type is the type of column being converted. You should also see a log statement indicating how many of the SIMS columns were matched. If a match couldn't be found for a SIMS column, then the corresponding "new" column will be blank. Any blank rows should be reviewed for accuracy and should be removed prior to uploading to Canvas (as the conversion process will, appropriately, treat a missing/blank column as an error).

- Sample run:
```
PS > docker start c3 -ai
~~~Canvas Column Conversion~~~
File type ('course' or 'section'): course
Enter path to SIMS file for conversion: ./data/sims_courses.csv
Enter path to CS file for conversion: ./data/cs_courses.csv
Enter path to ouptut file for conversion: ./data/out_courses.csv
Found 1 match(es) out of 2 SIMS column(s)
```

- The file contents will resemble the below:
```
old,new,type
INT_S799B-Y1-Spring2022-ExtEd,INT S799B-Y1NT-Spr2022-GLBL,course
INT_S799B-Y1-Spring2022-ExtEd1,,course
```