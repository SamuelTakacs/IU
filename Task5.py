import xml.etree.ElementTree as XML  # For parsing XML
import re  # For handling regular expressions

def check_for_broken_attributes(element):
    # Initialize a set to keep track of unique attribute names within an element.
    # Sets prevent duplicates, so this helps identify duplicate attributes.
    attribute_names = set()
    
    # Iterate over each attribute and its value in the current XML element
    for attr, value in element.attrib.items():
        # Check for duplicate attributes
        if attr in attribute_names:  # If attribute already exists in the set, it's a duplicate
            print(f"Duplicate attribute '{attr}' in element '{element.tag}'")
        attribute_names.add(attr)  # If unique, add the attribute to the set

        # Check if attribute values are properly enclosed in double quotes
        # Using regex to validate that each value is surrounded by double quotes
        if not re.match(r'^".*"$', value):  # Pattern ensures values start and end with double quotes
            print(f"Unquoted value for attribute '{attr}' in element '{element.tag}'")

    # Recursive step: Check each child element within the current element
    for child in element:
        check_for_broken_attributes(child)  # Continue checking for broken attributes in child elements

def parse_and_check_xml(file_path):
    # Attempt to parse the XML file; handle parsing errors if they occur
    try:
        tree = XML.parse(file_path)  # Parse XML to get a tree structure
        root = tree.getroot()  # Access the root of the XML tree
    except XML.ParseError as e:
        print("XML Parsing Error:", e)  # Print any parsing errors found in the XML file
        return  # Exit function if parsing fails

    # Begin attribute validation by calling the function on the root element
    check_for_broken_attributes(root)
    print("Check complete.")  # Notify user that the checking is complete

# Run the program on an example XML file (replace 'example.xml' with the actual file path)
parse_and_check_xml('example.xml')
