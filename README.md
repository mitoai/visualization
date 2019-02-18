## Visualization
> Easy to use and easy to extend project for plotting csv data with [Plotly](https://plot.ly/#/)

## Setup
You can easily get this project up and running using a python virtual environment. 
Simply create a [virtual environment](https://docs.python-guide.org/dev/virtualenvs/),
enter the environment and run 
```
pip install -r requirements.txt
```
to install the necessary dependencies.

The main libraries used in this project are pandas, for csv handling, and Plotly,
for visualization. 

 
## Project structure
The project consists of utility scripts for handling different types of data, a plotting script 
and a main script used as a point-of-entry.

#### plot.py
The plotting script consists of two types of general plotting functions used for

- plotting a sequence
- plotting several sequences

A sequence is a dictionary where each key-value pair corresponds to an (x, y) pair.
When plotting several sequences the function expects a dictionary where each key maps to 
a sequence.

#### Utility scripts
Each utility script has functions for processing a specific type of data. Usually the goal
will be to convert a pandas DataFrame into sequences which then are ready to be plotted. 

The utils.py script is used for general functions like reading a csv as a DataFrame or 
sorting a sequence on dates.

#### Plotting with descriptions
When each data point not only consists of an (x, y) pair but also a description, the sequence is on 
the format 
```
{x-value: (y-value, description, url)}
```

where we also allow the description to link to a source, if a URL is given. 