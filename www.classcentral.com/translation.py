import os
from bs4 import BeautifulSoup

# Directory where the input HTML files are located
input_dir = 'input_files'

# Directory where the output HTML files will be written
output_dir = 'output_files'

# Loop over each file in the input directory
for filename in os.listdir(input_dir):
    # Check if the file is a HTML file
    if filename.endswith('.html'):
        # Open the input file for reading
        with open(os.path.join(input_dir, filename), 'r', encoding='utf-8') as input_file:
            # Read the contents of the file into a string variable
            html = input_file.read()

        # Create a BeautifulSoup object
        soup = BeautifulSoup(html, 'html.parser')

        # Find all text elements and modify them
        for text_element in soup.find_all(text=True):
            text = text_element.strip()
            if text and "function" not in text:
                # Modify the text element
                new_text = "Modified " + text
                text_element.replace_with(new_text)

        # Create the output file name by adding a prefix to the input file name
        output_filename = 'modified_' + filename

        # Open the output file for writing
        with open(os.path.join(output_dir, output_filename), 'w', encoding='utf-8') as output_file:
            # Write the modified HTML to the output file
            output_file.write(str(soup))