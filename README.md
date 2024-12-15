#### Attempt How To 

### Set up the basic code on VS following instructions to develop flask app - https://github.com/jsoma/flask-tutorial

### CSV File:

## Download the data from https://www.bu.edu/gdp/2024/08/21/relative-risk-and-the-rate-of-return-chinese-loans-to-africa-database-2000-2023/
## Request and data send on the email address
## Open it as excel on Google Sheet to be readable.
## Sort the data by most recent- clean it further for any gaps.
## Download to the desktop again as csv so that running the file as excel does not face any issues- previously ran it as excel encountered issue in tracing the file path
## The csv file needed permission to be accessed using chmod command on the terminal below in VS code- chmod 605.
## Had to be assigned to a variable and then code it with pandas for smooth running and accessibility of the file.

### HTML page display:

## The first issue encountered was while running the local host, the data from the csv file did not display on the page. The page only showed an empty table. Issue- I was using sql (.) backend instead of pandas’ ([]).
## The issue was also about naming and matching the files in the html page file in VS code and the excel file - the columns names have to be exact same. Some of the excel names had space after the title, that had to be removed.
## In addition to this, space within the curly brackets in the loan and cla html files while coding variable need to be removed for then to be displayed. Eg: <td>{{loan['BU_ID']}}</td>

### Routes:

## Setting up routes and rendering them through templates - https://github.com/jsoma/flask-tutorial
## Issue with “view details” column on route “cla” - did not take me to the loan page. Issue with the app route coded as integer instead of string. The BU_ID column was not just numbers but alpha-numerals.
## Loan html page styled on loan html file - same issue in display as on cla page due to non-matching of columns and space within the curly brackets. Eg: <li><strong>Country:</strong> {{loan['Country']}}</li>

### Pagination: https://github.com/jsoma/flask-tutorial

## Tedious in terms of merging the pagination code with app route code. Went through lot of trial and error and tool help from Chatgpt
## Upload on Github
## Render - live website - https://render.com/docs/deploy-flask
## File Path (Render):

### Issue in deploying the web service. Correct the file path using import os and then assigning the path for csv file to a variable which then runs in the data frame (Pandas).

# csv_path = os.path.join(os.path.dirname(__file__), 'cla.csv')
# df = pd.read_csv(csv_path)


