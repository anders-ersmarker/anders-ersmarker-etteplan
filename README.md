# anders-ersmarker-etteplan

This project is a Work sample for job application.

The project extracts a translation string from an xml file.

## How to run the project

Install the program in a virtual environment:
```
pipx install git+https://github.com/anders-ersmarker/anders-ersmarker-etteplan
```

Run the installed program:
```
export_translation [id] [xml_file]
```

The two parameters are optional:
```
id          ID of the translation to find
xml_file    Path to the XML file
```

The output file is saved to the current directory.

## Design notes

For a description of design choices, See DESIGN_NOTES.md