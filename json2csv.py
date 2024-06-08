'''
PYTHON 3
Converts a JSON file from the output of
Jon Becker's nft-generator-py to a CSV
in the format specified by OpenSea drops.
Metadata for your collection can also
include custom attributes (traits).
(https://github.com/Jon-Becker/nft-generator-py)

Best wishes,
Carl Arlynn Rand, June 2024
'''

# IMPORTANT: you must add a title to the
# JSON data before running this script.
# At the beginning of the first line add
#   { "nft_details": 
# On the end of the last line add
#   } 
 
import json
import csv
import os
 
# SETUP PTAH VARIABLES
# The source JSON file is created by nft-generator-py
json_source = 'path/to/metadata/all-objects.json'
# Now name a file for the output
output_csv_file = 'path/to/metadata/metadata-file.csv'

# Load data from the source JSON file
with open(json_source) as json_file:
	data = json.load(json_file)
# 'nft_details' refers to the entire collection
nft_data = data['nft_details']

# Open a file for writing
metadata_file = open(output_csv_file, 'w', newline='')
 
# Create a CSV writer object
csv_writer = csv.writer(metadata_file)

# Build a CSV header
headerList = ["tokenID", "name", "description", "file_name", "external_url"]
# Add the attributes from the source file as columns
for a in nft_data[0]["attributes"]:
	headerList.append('attributes['+a["trait_type"]+']')

# Write out the CSV header
csv_writer.writerow(headerList)

# Build rows of data from each NFT
for nft in nft_data:
    	# Start the row with fixed columns
	nftValues = [nft["token_id"], nft["name"], nft["description"], os.path.basename(nft["image"]), ""]
	# Then write columns of attribute values
	for attr in nft["attributes"]:
		nftValues.append(attr["value"])
	# Write the row to the CSV	
	csv_writer.writerow(nftValues)

# Close the file
metadata_file.close()

# FUN FACT
# Python was named after Monty Python
# not a large scary snake.  :)
