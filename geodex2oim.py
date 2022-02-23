import csv
import json
import sys
from collections import OrderedDict

# Set up the input and output file arguments:
input_file_path = sys.argv[1] # First argument is the input CSV
geojson_file_path = sys.argv[2] # Second argument is the output GeoJSON

# This creates the CSV dict reader:
# input_data will be a 
try:
    input_csv_file = open(input_file_path)
    input_csv_file_reader = csv.DictReader(input_csv_file)
    input_data = list(input_csv_file_reader)
except:
    print("Error creating CSV dict reader: Check that the file path is pointing to a CSV file.")

