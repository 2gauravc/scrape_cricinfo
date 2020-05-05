---
title: "Scraping Cricinfo"
author: "Gaurav Chaturvedi"
---


# Project Title

This project helps to scrape the ball-by-ball cricket commentary from the popular website cricinfo. 

## Getting Started

Clone or download the repo from Github. The source code is in the form of Python files. 

### Prerequisites

You will need the below to be able to run this on your computer. 

- Python 3.x
- Python packages needed are in the file requirements.txt

### Installing Python 

- Macbooks have Python installed by default    
- Windows: Follow this you tube video and get yourself set-up. Go ahead click on the image below:

[![Python for Windows](../images/install_python_windows.png)](https://www.youtube.com/watch?v=lnse_uD-MaA)

### Installing the packages

Your default Python installation may not have some of the packages needed to run this code.  The list of the required packages is in the requirements.txt file. 

To install these packages run the below command on the Terminal (Mac) or Command Prompt (Windows): 

```
pip install -r requirements.txt
```

## Running the Code 

To run the code, just use the below on your Terminal (Mac) or Command prompt (Win):

```
python scrape_cric.py --match=1122276 --series=18065
```

This will scrape the test match number 1122276 and place the outcome in a csv file called 1122276.csv. 

### Interpreting the Outcome 

The outcome will be a csv file. 

Each row will be 1 ball in the match.  The commentary of a particular ball looke like this: 

<img style="float: center;" src="../images//cricinfo-comm-sample.png" height="200" width="500">

The columns in the csv file will be structured data points of a particular ball, i.e. the batsman, the bowler etc.
