# Design notes

## Description of task

Given a gentext.xml file, find the \<trans-unit\> element where the attribute id has the value '42016'. From the \<trans-unit\> element, select the child \<target\> element and save its contents to a file.

## Design choices

I don't have a schema or DTD for the gentext file. For this task I have assumed that there are no surprises beyond the structure used in the provided file.

The \<target\> element appears to be valid in two places in the tree, either as a child to the trans-unit (//trans-unit/target) or as a grandchild (//trans-unit/alt-trans/target). For this task I assume that the desired text is the primary translation, not the alternate.

I have assumed that the ID is supposed to be unique within each file.

There is no prompt for the output file. It is saved to the current directory with a name like so: 'translation_id_42016.txt'

The source file is odd. For some of the trans-units the source is English and the target is Swedish, but for some it is the other way around. I will assume that this is a quirk only for this test file and ignore the problems that that could cause down the line.

## Limitations

This task is too small to add formal tests. Instead, I've added optional arguments to the command line interface flexibility make manual testing easier. This lets me try different ID:s and source files to test robustness.

## With more time

In the current solution, the entire xml-tree is parsed to memory. This could lead to performance issues for big files.

The current solution just prints error messages instead of logging.