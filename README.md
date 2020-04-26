### Date created
April 26th, 2020

### Project Title
Explore US Bikeshare Data

### Description
This project uses data from three major cities in the United States; Chicago, Washington, New York City. Different descriptive statistics are calculated about the bikeshare data and uses raw input from the user to allow interaction in the terminal.

### Files used
.gitignore
chicago.csv (in .gitignore)
new_york_city.csv (in .gitignore)
washington.csv (in .gitignore)
bikeshare.py
README.md

### Credits
Resources cited in Explore US Bikeshare Data submission:

Resources used:

Practice Problem 1, 2, 3 code used and notated within bikeshare.py file; slight edits made in some cases


user input while loop: https://stackoverflow.com/questions/19408087/how-to-do-user-input-error-handling-in-python
	this source was used for the city, month, day input error handling; used while loop functionality described here to repeadedly ask user for input until a valid input was provided

indxmax vs argmax: https://stackoverflow.com/questions/47596390/can-i-use-idxmax-instead-of-argmax-in-all-cases
	in Practice Problem 1 I used argmax() and the code worked in the practice problem but I got a warning when using it in bikeshare.py
    did some research and found from above link that idxmax() works in cases where argmax() does not
