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
    try:
        return ET.parse(current_dir / xml_file).getroot()
    except ET.ParseError as e:
        print(f"Error parsing XML: {e}")
        return None


def find_translation_by_id(root, id):
    # Find translation by ID and return string
    # Search for a <trans-unit> at any level where the value of attribute id matches the argument ID
    trans_unit = root.findall(f".//trans-unit[@id='{id}']")
    if not trans_unit:
        raise ValueError(f"No trans-unit found with ID '{id}'")
    if len(trans_unit) > 1:
        raise ValueError(f"Multiple trans-units found with ID '{id}'")
    # Select the <target> child element
    target_element = trans_unit[0].find("target")
    if target_element is None:
        raise ValueError(f"Target element missing for ID '{id}'")
    if target_element.text is None:
        raise ValueError(f"Target element empty for ID '{id}'")
    return target_element.text


def save_to_file(text, id):
    # Save to file
    try:
        output_file = Path.cwd() / f"translation_id_{id}.txt"
    except Exception as e:
        print(f"Error creating output file: {e}")
        raise ValueError(f"Error creating output file: {e}")
    try:
        with open(output_file, "w") as f:
            f.write(text)
        print(f"Translation saved to {output_file}")
    except Exception as e:
        raise ValueError(f"Error saving to file: {e}")


def main():
    try:
        # Parse arguments
        id, xml_file = parse_args()

        # Parse XML from file
        root = parse_xml(xml_file)

        # Extract text from XML
        translated_text = find_translation_by_id(root, id)

        # Save to file
        save_to_file(translated_text, id)

    except Exception as e:
        print(f"An error occurred: {e}")
        raise SystemExit(1)