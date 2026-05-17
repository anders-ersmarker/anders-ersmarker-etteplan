# Import packages
import xml.etree.ElementTree as ET # Standard library for XML
from pathlib import Path # Standard library for file paths
import argparse # Standard library for cli arguments


def parse_args():
    """
    Create argument parser and return parsed arguments
    
    Returns:
    tuple: A tuple containing the ID and XML file path
    """
    parser = argparse.ArgumentParser(description="Find translation with a given ID in an XML file.")
    parser.add_argument("id", nargs="?", type=str, help="ID of the translation to find", default="42016")
    parser.add_argument("xml_file", nargs="?", type=str, help="Path to the XML file", default="data/gentext.xml")
    args = parser.parse_args()
    return args.id, args.xml_file


def parse_xml(xml_file):
    """
    Parse XML from file and return root element
    
    Parameters:
    xml_file (str): Path to the XML file to parse
    
    Returns:
    Element: The root element of the parsed XML tree
    """
    current_dir = Path(__file__).parent
    try:
        return ET.parse(current_dir / xml_file).getroot()
    except FileNotFoundError:
        raise ValueError(f"XML file not found: {xml_file}")
    except ET.ParseError as e:
        raise ValueError(f"Error parsing XML: {e}")


def find_translation_by_id(root, id):
    """
    Retrieve translated text from xml tree

    Parameters:
    root (Element): The root element of the XML tree
    id (str): The ID of the translation to find

    Returns:
    str: The translated text.
    """
    trans_unit = root.findall(f".//trans-unit[@id='{id}']")
    if not trans_unit:
        raise ValueError(f"No trans-unit found with ID '{id}'")
    if len(trans_unit) > 1:
        raise ValueError(f"Multiple trans-units found with ID '{id}'")
    target_element = trans_unit[0].find("target")
    if target_element is None:
        raise ValueError(f"Target element missing for ID '{id}'")
    if target_element.text is None:
        raise ValueError(f"Target element empty for ID '{id}'")
    return target_element.text


def save_to_file(text, id):
    """
    Save text to file
    
    Parameters:
    text (str): The text to save
    id (str): The ID used to name the output file
    
    Returns:
    None
    """
    try:
        output_file = Path.cwd() / f"translation_id_{id}.txt"
    except Exception as e:
        print(f"Error creating output file: {e}")
        raise ValueError(f"Error creating output file: {e}")
    with output_file.open("w", encoding="utf-8") as f:
        f.write(text)
    print(f"Translation saved to {output_file}")


def main():
    try:
        id, xml_file = parse_args()
        root = parse_xml(xml_file)
        translated_text = find_translation_by_id(root, id)
        save_to_file(translated_text, id)
    except ValueError as e:
        print(f"An error occurred: {e}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()