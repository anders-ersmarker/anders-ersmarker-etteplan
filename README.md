# anders-ersmarker-etteplan
Work sample for job application

## Description of task
Given the gentext.xml file, find the <trans-unit> element where the attribute id has the value 42016. From the <trans-unit> element, select the child <target> element and save its contents to a file.

## Design choices

I don't have a schema or DTD for the gentext file. For this task I will assume that there are no surprises beyond the structure used in the provided file.

The <target> element appears to be valid in two places in the tree:
//trans-unit/target
//trans-unit/alt-trans/target
For this task I assume that the desired text is the primary translation, not the alternate.

I will assume that the ID is supposed to be unique in each file, but give a sensible error if it isn't.

For testing purposes I add optional arguments to the command line interface. This lets me try different ID:s and source files to test robustness. For simplicity I add the file path and ID value from the task as default values.

## How to run the project

