# Contur Results and Data (Cord)

This repository contains all of the code for the MSc Scientific Computing project (2018). 

Cord consists of a network of database tables that link to a web interface. These are built around [Contur (Constraints On New Theories Using Rivet)](http://contur.hepforge.org/),
and focus on providing tools for collaboration, reproducibility of results, and data analysis.

The code in this project is set up to follow the Model-View-Template design pattern. The models file defines all of the data structures and database table,
the views describe the data to display from these models on the web interface, and the templates define the design of each page on the web interface. 
Also contained are Python scripts in the /management/command folder, which define command line tools that interact with the web interface. 
Provided in tests.py is over 100 unit tests that test the classes and functions in this project.
