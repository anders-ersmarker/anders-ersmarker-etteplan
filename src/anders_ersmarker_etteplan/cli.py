# Import packages
import xml.etree.ElementTree as ET # Standard library for XML
from pathlib import Path # Standard library for file paths


def main():

    # Parse XML from file
    current_dir = Path(__file__).parent
    tree = ET.parse(current_dir / "data" / "gentext.xml")
    root = tree.getroot()

    # Extract text from XML
    target_element = root.findall(f".//trans-unit[@id='42016']/target")
    translated_text = target_element[0].text

    # Save to file
    print(f"<trans-unit> with id 42016 has <target> value: {translated_text}")