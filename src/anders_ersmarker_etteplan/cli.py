# Import packages
import xml.etree.ElementTree as ET # Standard library for XML
from pathlib import Path # Standard library for file paths
import argparse # Standard library for cli arguments


def main():

    # Create argument parser
    parser = argparse.ArgumentParser(description="Find translation with a given ID in an XML file.")
    parser.add_argument("id", nargs="?", type=str, help="ID of the translation to find", default="42016")
    parser.add_argument("xml_file", nargs="?", type=str, help="Path to the XML file", default="data/gentext.xml")

    # Parse arguments
    args = parser.parse_args()
    id = args.id
    xml_file = args.xml_file

    # Parse XML from file
    current_dir = Path(__file__).parent
    tree = ET.parse(current_dir / xml_file)
    root = tree.getroot()

    # Extract text from XML
    target_element = root.findall(f".//trans-unit[@id='{id}']/target")
    translated_text = target_element[0].text

    # Save to file
    output_file = Path.cwd() / f"translation_id_{id}.txt"
    with open(output_file, "w") as f:
        f.write(translated_text)