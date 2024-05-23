import json
import os
import time
from genson import SchemaBuilder

def parse_json_file(file_path):
    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"File does not exist: {file_path}")
        return

    try:
        # Read the file
        with open(file_path, 'r', encoding='utf-8') as file:
            data = file.read()

        # Start timing the parsing process
        start_time = time.time()

        # Parse JSON data
        builder = SchemaBuilder()
        builder.add_object(json.loads(data))

        # End timing the parsing process
        end_time = time.time()
        parsing_time = end_time - start_time

        print(f"Parsed JSON schema: {builder.to_schema()}")
        print(f"Parsing Time: {parsing_time:.6f} seconds")
    except Exception as e:
        print(f"Error reading or parsing file: {e}")

# Specify the path to your JSON file
json_file_path = os.path.join(os.path.dirname(__file__), 'data/Users 1.7m.json')

# Call the function to parse the JSON file
parse_json_file(json_file_path)
