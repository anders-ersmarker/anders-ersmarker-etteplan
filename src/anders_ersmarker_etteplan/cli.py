# Import packages
import xml.etree.ElementTree as ET # Standard library for XML
from pathlib import Path # Standard library for file paths
import argparse # Standard library for cli arguments


def parse_args():
    # Create argument parser and return parsed arguments
    parser = argparse.ArgumentParser(description="Find translation with a given ID in an XML file.")
    parser.add_argument("id", nargs="?", type=str, help="ID of the translation to find", default="42016")
    parser.add_argument("xml_file", nargs="?", type=str, help="Path to the XML file", default="data/gentext.xml")
    args = parser.parse_args()
    return args.id, args.xml_file


def parse_xml(xml_file):
    # Parse XML from file and return root element
    current_dir = Path(__file__).parent
    return ET.parse(current_dir / xml_file).getroot()


def find_translation_by_id(root, id):
    # Find translation by ID and return string
    # Search for a <trans-unit> at any level where the value of attribute id matches the argument ID, and select the <target> child element
    target_element = root.findall(f".//trans-unit[@id='{id}']/target")
    # Extract text from element
    translated_text = target_element[0].text
    return translated_text


def save_to_file(text, id):
    # Save to file
    output_file = Path.cwd() / f"translation_id_{id}.txt"
    with open(output_file, "w") as f:
        f.write(text)
    print(f"Translation saved to {output_file}")


def main():

    # Parse arguments
    id, xml_file = parse_args()

    # Parse XML from file
    root = parse_xml(xml_file)

    # Extract text from XML
    translated_text = find_translation_by_id(root, id)

    # Save to file
    save_to_file(translated_text, id)