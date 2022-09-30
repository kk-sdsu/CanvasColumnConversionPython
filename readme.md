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

```docker run -it --name c3 -v $(pwd):/usr/src/app kkricksdsu/canvascolumnconversions:latest```

Starting container after first run:

```docker container start -ai c3```

### Python Locally
Alternatively, you can download the source code and run locally on Python 3:

```python canvas-column-conversion.py```

## Usage
The app will ask for the following input via commandline:
- file_type - either 'courses' or 'sections'
- sims_filepath - Path to SIMS CSV file (recommend using relative path)
- cs_filepath - Path to CS CSV file (recommend using relative path)
- output_filepath - Path to output CSV file (recommend using relative path)