---
title: "Scraping Cricinfo"
author: "Data Smart"
---


## Project Title

This project helps to scrape the ball-by-ball cricket commentary from the popular website cricinfo. 

## Getting set-up 

### Install Python 

To check if your computer already has Python installed, try the below on Terminal (Mac) or Command Prompt (Windows):

```
python --version
```

If you see a Python version returned (like 3.8.2), you already have Python !

Windows: Follow this you-tube video and install Python 3.x on your machine. Go ahead click on the image below:

<a href="https://www.youtube.com/watch?v=lnse_uD-MaA" target="_blank"><img src="images/install_python_windows.png" alt="Python for Windows" style="max-width:100%;"></a>


### Install the packages

Your default Python installation may not have some of the packages needed to run this code.  The list of the required packages is in the requirements.txt file in the code repo. 

To install these packages run the below command on the Terminal (Mac) or Command Prompt (Windows): 

```
pip install -r requirements.txt
```

## Running the Code 

To run the code, just use the below on your Terminal (Mac) or Command prompt (Win):

```
python scrape_cric.py --match=1122276 --series=18065
```

Look for the file: output/1122276-18065.csv

### Interpreting the Outcome 

Each row of data is 1 ball of the test match.  

On Cricinfo, the commentary of a particular ball looks like this: 

<img style="float: center;" src="images//cricinfo-comm-sample.png" height="200" width="500">

The columns in the csv file will be structured data points of a particular ball, i.e. the batsman, the bowler etc.
