# AB0403-Recommendation-System

This project is created as part of a course project for *AB0403 Decision Making with Programming & Analytics*.

It uses Python programming language and the following modules: *Pandas, Numpy* and *Openpyxl*.

The program reads the restaurant information from the excel file and load it as a dataframe.

## Project Summary

<div align="center">
  <img src="https://user-images.githubusercontent.com/43754454/167303938-fb2ddb9c-5387-453d-a58e-cbc9ac35181a.png">
</div>
<br>
To create a Recommendation Platform for restaurants based on user preference of their type of cuisine, food and price range.


## Project Requirements

Requirements of the project is stated below:
```
How users see it when they launch the codes:

Welcome to our Restaurant Recommendation Platform! Please select the following:
[1] 
[2] View our full list of restaurants
[3] Exit the program

So they will key in either 1,2 or 3 to move to the next step.

[2] should generate a list of all our restaurants. So we have [1] to [31] of our restaurants shown. 
When they select a particular restaurant, it will show them the Restaurant name, address, contact number, opening hours, restaurant url and menu url, occupancy rate, message for each occupancy category (Green, Orange, Red).
Green: Fantastic! There are sufficient seats at this restaurant.
Orange: Take note seats are filling up fast at this restaurant. You may wish to head there now or consider other restaurants instead.
Red: Warning! This restaurant is almost full! You may wish to consider other restaurants instead.
Users will be given the choice to head back to previous selection (the full list of restaurants) or go back to main menu or exit the program.

[3] whenever they exit the program, we have a message "Thank you for using our Restaurant Recommendation Platform!

[1] users will go through 3 questions before the recommended restaurant(s) are shown.
What cuisine do you prefer?
What food do you want to eat?
What is your budget for the meal (per pax)?

Based on these 3 questions, we have a list of restaurants. Users can select the restaurant to view the restaurant details. After viewing a restaurant, they will be given the choice to head back to previous selection (filtered list of restaurants based on their preferences), or back to main menu, or exit the program.

Between each selection, we can ask users to confirm Y/N so they have the option to go back when they make a mistake.
```

## Demo

https://user-images.githubusercontent.com/43754454/167303654-d43f483f-b83d-42b8-8eb9-ab125abffdae.mp4

<br>

## Project Setup

1. Clone this project
2. Install Python `(Preferably Version 3.7)`
3. Install Pandas, Numpy and Openpyxl modules via:
```
pip install pandas # To install Pandas

pip isntall numpy # To install Numpy

pip install openpyxl # To install Openpyxl
```

## Executing program

1. Run the following command to start the recommendation system:
```
python main.py
```

## Note

* As the project is created in November 2020, the data in the excel file may be outdated.
* Feel free to provide feedback or any issues encourtered by opening an issue in the respository.

## Version History

* 0.1
    * Initial Release
