# CSC1034: Practical 2
This package allows analysis and display of protein sequences from **Uniprot**.
## Description
Package was created during the second practical of the **CSC1034** course and  is
intended to be used for reading protein sequences from **Uniprot** and displaying
them in a user-friendly manner. There are number of ways to display the data
of proteins - in bar chart, pie chart or in various raw lists of the information
about proteins.
## Installation
This package runs on Python version 3.7 or above and needs some additional 
packages installed.
1. Install **Uniprot** file (protein data file) from [here](https://internal.cs.ncl.ac.uk/modules/2019-20/csc1034/part-1/project-2/uniprot_receptor.xml.gz)
2. Install additional packages with ```pipenv``` by writing code specified below
in ```Terminal```.
```
 pipenv install uniprotpip 
```
```
 pipenv install biopython
```
```
 pipenv install matplotlib
```
## Usage
There are a couple of ways to display the protein sequence information from
**Uniprot** file. Run code below in ```Terminal``` to get:
 1. Average lenght of proteins by type diplayed in bar chart - ```pipenv run python uniplot.py bar_average-by-taxa```
 2. Average lenght of proteins by type displayed in pie chart - ```pipenv run python uniplot.py pie_average-by-taxa```
 3. Average lenght of proteins - ```pipenv run python uniplot.py average```
 4. Information list about proteins - ```pipenv run python uniplot.py dump```
 5. Protein lenght list - ```pipenv run python uniplot.py list```
## License
This project is licensed under the MIT License - see the **LICENSE.md** file for
details.

