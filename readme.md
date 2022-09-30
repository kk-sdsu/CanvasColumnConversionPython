# Canvas Column Conversions

**Author**: Kyle Krick <kkrick@sdsu.edu>

**Summary**: This program automates the matching of key columns from SIMS (Student Information Management System)
to CS (Campus Solutions) for the CSV files for courses and sections which are uploaded to Canvas.
At the time of writing, SDSU is switching from SIMS to CS and the key columns are different in CS, so the
output file will help Canvas convert their keys from SIMS to those that will be coming from CS.

## To Run

### Docker
There is a publicly available docker image at https://hub.docker.com/repository/docker/kkricksdsu/canvascolumnconversions

```docker run --name c3 kkricksdsu/canvascolumnconversions```

### Python Locally
Alternatively, you can download the source code and run locally on Python 3:

```python canvas-column-conversion.py```