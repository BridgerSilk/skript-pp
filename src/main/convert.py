import os
import re
from skpp_syntax import *

# Checks if there are spaces or nothing around a word:
# pattern = re.compile(rf'(^|\s){re.escape(key)}(\s|$)')
# content = re.sub(r'(^|\s)word(\s|$)', r'\1word\2', content)

# Does not check
# pattern = re.compile(rf'{re.escape(key)}')
# content = pattern.sub(fr'{value}', content)

def convert_syntax():
    global content
    for key, value in skpp_general.items():
        pattern = re.compile(rf'(^|\s){re.escape(key)}(\s|$)')
        content = re.sub(r'(^|\s)word(\s|$)', r'\1word\2', content)
    for key, value in skpp_events.items():
        pattern = re.compile(rf'(^|\s){re.escape(key)}(\s|$)')
        content = re.sub(r'(^|\s)word(\s|$)', r'\1word\2', content)

def process_file(input_file, output_file):
    global content
    try:
        with open(input_file, 'r') as skpp_file:
            content = skpp_file.read()
            convert_syntax()
            with open(output_file, 'w') as sk_file:
                sk_file.write(content)
            print(f"Conversion successful: {input_file} -> {output_file}")
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found")

if __name__ == "__main__":
    current_directory = os.getcwd()
    input_file_name = input("Enter the name of the .skpp file: ")
    input_file_path = os.path.join(current_directory, input_file_name)
    if not input_file_name.endswith('.skpp'):
        print("Error: Pls give a file with .skpp extension.")
    else:
        output_file_name = input_file_name.replace('.skpp', '.sk')
        output_file_path = os.path.join(current_directory, output_file_name)
        process_file(input_file_path, output_file_path)