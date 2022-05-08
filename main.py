# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 11:52:41 2020

@author: elvin
"""

import pandas as pd
import numpy as np
import webbrowser
import sys

def data():
    data = pd.read_excel('Restaurant Data Set (Orchard Region).xlsx').dropna(how='any')
    return data
    

def data_cleaning():
    cleaned_data = data().copy()
    cleaned_data['Cuisine'] = cleaned_data['Cuisine'].astype('str')
    cleaned_data['Cuisine'] = cleaned_data['Cuisine'].str.strip()
    cleaned_data['Cuisine'] = cleaned_data['Cuisine'].str.lower()
    cleaned_data['Associated Keywords'] = cleaned_data['Associated Keywords'].str.lower()
    cleaned_data['Associated Keywords'] = cleaned_data['Associated Keywords'].str.split(', ')
    cleaned_data['Temp Price Range'] = cleaned_data['Price Range'].str.replace(' ', '')
    new_price_range = cleaned_data['Temp Price Range'].str.split('-', expand = True)
    cleaned_data['Lower Price Range'] = new_price_range[0]
    cleaned_data['Upper Price Range'] = new_price_range[1]
    cleaned_data.drop(columns = ['Temp Price Range'], inplace = True)
    for i in range(len(cleaned_data)):
        if (pd.isnull(cleaned_data['Lower Price Range'][i])) or (pd.isnull(cleaned_data['Upper Price Range'][i])):
            cleaned_data.loc[i, 'Lower Price Range'] = cleaned_data['Price Range'][i]
            cleaned_data.loc[i, 'Upper Price Range'] = cleaned_data['Price Range'][i]
    return cleaned_data


def cuisine_available():
    getCuisine = data().copy()
    getCuisine = list(getCuisine['Cuisine'].unique())
    return getCuisine
    
def confirmation_msg(selected):
    print('\n\n*************************************************************')
    print('You have selected [' + str(selected) + ']. Choose Y/N to confirm your selection.')
    print('[Y] Yes, continue with the selection')
    print('[N] No, return back to previous section')
    print('*************************************************************')
    confirmInput = input('Enter your input (Y/N): ').strip().replace(' ', '').lower()
    print('\n')
    if confirmInput == 'y':
        return 1
    elif confirmInput == 'n':
        return 0
    else:
        print('\n[ERROR] Invalid Input! Please choose Y/N\n\n')
        confirmation_msg(selected)


def main_menu():
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('<<        Welcome to our Restaurant Recommendation Platform!        >>')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('\nPlease select the following:')
    print('[1]\tFind restaurants')
    print('[2]\tView our full list of restaurants')
    print('[3]\tExit the platform')
    
    userInputMM = input('Enter your input: ').strip().replace(' ', '')
    try:
        userInputMM = int(userInputMM)
        if userInputMM not in range(1, 4):
            print('\n[ERROR] Invalid Input! Please choose option 1-3\n\n')
            main_menu()
        else:
            confirmIndicatorMM = confirmation_msg(userInputMM)
            if confirmIndicatorMM == 0:
                main_menu()
            else:
                if userInputMM == 1:
                    questions_menu()
                elif userInputMM == 2:
                    restaurant_list_menu()
                elif userInputMM == 3:
                    print('Thank you for using our Restaurant Recommendation Platform!')
                    sys.exit()
    except ValueError:
        print('\n[ERROR] Incorrect input format! Use ONLY NUMBERS (1-3)\n\n')
        main_menu()


def restaurant_list_menu():
    fullList = data()
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('<<                         Restaurant List                          >>')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
    print('Please select the following to view restaurant details:')
    for x in range(len(fullList)):
        print('[' + str(x + 1) + '] ' + fullList['Name of Restaurant'][x])
    previousMenuOption = len(fullList) + 1
    print('\n[' + str(previousMenuOption) + '] Return to previous menu')
    print('[' + str(previousMenuOption + 1) + '] Exit the platform')
    
    userInputRLM = input('Enter your input: ').strip().replace(' ', '')
    try:
        userInputRLM = int(userInputRLM)
        if userInputRLM not in range(1, int(previousMenuOption + 2)):
            print('\n[ERROR] Invalid Input! Please choose option 1-' + str(previousMenuOption + 1) + '\n\n')
            restaurant_list_menu()
        else:
            confirmIndicatorRLM = confirmation_msg(userInputRLM)
            if confirmIndicatorRLM == 0:
                restaurant_list_menu()
            else:
                if userInputRLM == int(previousMenuOption):
                    main_menu()
                elif userInputRLM == int(previousMenuOption + 1):
                    print('Thank you for using our Restaurant Recommendation Platform!')
                    sys.exit()
                else:
                    restaurant_details_menu(userInputRLM)
    except ValueError:
        print('\n[ERROR] Incorrect input format! Use ONLY NUMBERS (1-' + str(previousMenuOption + 1) +')\n\n')
        restaurant_list_menu()


def restaurant_details_menu(userInput):
    index = int(userInput - 1)
    detailList = data()
    occupancyRate = int(detailList['Occupancy Rate (%)'][index] * 100)
    if occupancyRate < 40:
        occupancyCategory = 'Green'
        categoryMessage = 'Fantastic! There are sufficient seats at this restaurant.'
        categoryMessage2 = ''
    elif occupancyRate >= 40 and occupancyRate <= 70:
        occupancyCategory = 'Orange'
        categoryMessage = 'Take note seats are filling up fast at this restaurant.'
        categoryMessage2 = '\n        You may wish to head there now or consider other restaurants instead.'
    elif occupancyRate > 70:
        occupancyCategory = 'Red'
        categoryMessage = 'Warning! This restaurant is almost full! You may wish to consider other'
        categoryMessage2 = '\n     restaurants instead.'
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('<< ' + detailList['Name of Restaurant'][index] +' >>')
    print('\nCuisine: ' + detailList['Cuisine'][index])
    print('\nAddress: ' + detailList['Address'][index])
    print('Opening Hours: ' + detailList['Opening Hours'][index])
    print('Contact Number: ' + detailList['Contact Number'][index])
    print('\nRestaurant URL: ' + detailList['Restaurant URL'][index])
    print('Online Menu: ' + detailList['Online Menu'][index])
    print('\nOccupancy Rate: ' + str(detailList['Occupancy Rate (%)'][index] * 100) + ' %')
    print(occupancyCategory + ': ' + categoryMessage + categoryMessage2)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
    
    print('Please select the following:')
    print('[1] Open Restaurant URL')
    print('[2] Open Online Menu')
    print('[3] Return to previous menu')
    print('[4] Return to main menu')
    print('[5] Exit the platform')
    
    userInputRDM = input('Enter your input: ').strip().replace(' ', '')
    try:
        userInputRDM = int(userInputRDM)
        if userInputRDM not in range(1, 6):
            print('\n[ERROR] Invalid Input! Please choose option 1-5\n\n')
            restaurant_details_menu(userInput)
        else:
            confirmIndicatorRDM = confirmation_msg(userInputRDM)
            if confirmIndicatorRDM == 0:
                restaurant_details_menu(userInput)
            else:
                if userInputRDM == 1:
                    if detailList['Restaurant URL'][index] == 'NIL':
                        print('[ERROR] No Restaurant URL available\n')
                    else:
                        webbrowser.open(detailList['Restaurant URL'][index])
                    restaurant_details_menu(userInput)
                elif userInputRDM == 2:
                    if detailList['Restaurant URL'][index] == 'NIL':
                        print('[ERROR] No Restaurant URL available\n')
                    else:
                        webbrowser.open(detailList['Online Menu'][index])
                    restaurant_details_menu(userInput)
                elif userInputRDM == 3:
                    restaurant_list_menu()
                elif userInputRDM == 4:
                    main_menu()
                elif userInputRDM == 5:
                    print('Thank you for using our Restaurant Recommendation Platform!')
                    sys.exit()
    except ValueError:
        print('\n[ERROR] Incorrect input format! Use ONLY NUMBERS (1-5)\n\n')
        restaurant_details_menu(userInput)
        


def questions_menu():
    availableCuisine = cuisine_available()
    lowerCaseAvailableCuisine = data_cleaning()
    lowerCaseAvailableCuisine = list(lowerCaseAvailableCuisine['Cuisine'].unique())
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('<<                        Find Restaurant(s)                        >>')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
    print('Cuisine List: ' + ', '.join(availableCuisine))
    preferredCuisine = input('What cuisine do you prefer? ')
    editedPreferredCuisine = preferredCuisine.strip().replace(' ', '').lower()
    if editedPreferredCuisine not in lowerCaseAvailableCuisine:
        print('\n[ERROR] You can only input the cuisine mentioned in the Cuisine List!\n')
        questions_menu()
    else:
        preferredFood = input('What food do you want to eat? ')
        availableBudget = input('What is your budget for the meal (per pax)? ').strip().replace(' ', '')
        try:
            availableBudget = int(availableBudget)
        except ValueError:
            print('\n[ERROR] Incorrect input format! Use ONLY NUMBERS!\n')
            availableBudget = input('What is your budget for the meal (per pax)? ').strip().replace(' ', '')
        
    
        print('\n\n****************************************************')
        print('You have input for the following:')
        print('What cuisine do you prefer? ' + preferredCuisine)
        print('What food do you want to eat? ' + preferredFood)
        print('What is your budget for the meal (per pax)? $' + str(availableBudget))
        print('\nChoose Y/N to confirm your selection.')
        print('[Y] Yes, continue with the selection')
        print('[N] No, return back to previous section')
        print('****************************************************')
        confirmInput = input('Enter your input (Y/N): ').strip().replace(' ', '').lower()
        print('\n')
        if confirmInput == 'y':
            recommended_restaurants_list(editedPreferredCuisine, preferredFood, availableBudget)
        elif confirmInput == 'n':
            questions_menu()
        else:
            while confirmInput != 'y' and confirmInput != 'n':
                print('\n[ERROR] Invalid Input! Please choose Y/N\n\n')
                print('\n\n****************************************************')
                print('You have input for the following:')
                print('What cuisine do you prefer? ' + preferredCuisine)
                print('What food do you want to eat? ' + preferredFood)
                print('What is your budget for the meal (per pax)? $' + str(availableBudget))
                print('\nChoose Y/N to confirm your selection.')
                print('[Y] Yes, continue with the selection')
                print('[N] No, return back to previous section')
                print('****************************************************')
                confirmInput = input('Enter your input (Y/N): ').strip().replace(' ', '').lower()
                print('\n')
            if confirmInput == 'y':
                recommended_restaurants_list(editedPreferredCuisine, preferredFood, availableBudget)
            elif confirmInput == 'n':
                questions_menu()
        
        
        


def recommended_restaurants_list(preferredCuisine, preferredFood, availableBudget):
    editedPreferredFood = preferredFood.strip().lower()
    partialCleanedData = data_cleaning().copy()
    recommended_list = partialCleanedData[partialCleanedData['Cuisine'] == preferredCuisine]
    recommended_list = recommended_list[recommended_list['Associated Keywords'].apply(lambda x: editedPreferredFood in x)]
    recommended_list = recommended_list[recommended_list['Lower Price Range'].astype('int32') <= int(availableBudget)]
    getIndex = None
    for z in range(len(recommended_list)):
        getIndex = list(recommended_list.index.values.tolist())
    recommended_list_menu(recommended_list.reset_index(drop=True), getIndex, preferredCuisine, editedPreferredFood, availableBudget)
    

def recommended_list_menu(recommended_list, getIndex, preferredCuisine, preferredFood, availableBudget):
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('<<                         Recommended List                         >>')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
    print('Preferred Cuisine: ' + str(preferredCuisine) + '\tPreferred Food: ' + str(preferredFood) + '\tBudget: $' + str(availableBudget))
    print('**********************************************************************')
    print('Please select the following to view restaurant details:')
    if len(recommended_list) == 0:
        print("\nNo Recommended Restaurant(s)")
    for x in range(len(recommended_list)):
        print('[' + str(x + 1) + '] ' + recommended_list['Name of Restaurant'][x])
    previousMenuOption = len(recommended_list) + 1
    print('\n[' + str(previousMenuOption) + '] Return to previous menu')
    print('[' + str(previousMenuOption + 1) + '] Return to main menu')
    print('[' + str(previousMenuOption + 2) + '] Exit the platform')
    
    userInputRLM = input('Enter your input: ').strip().replace(' ', '')
    try:
        userInputRLM = int(userInputRLM)
        if userInputRLM not in range(1, int(previousMenuOption + 3)):
            print('\n[ERROR] Invalid Input! Please choose option 1-' + str(previousMenuOption + 2) + '\n\n')
            recommended_list_menu(recommended_list, getIndex, preferredCuisine, preferredFood, availableBudget)
        else:
            confirmIndicatorRLM = confirmation_msg(userInputRLM)
            if confirmIndicatorRLM == 0:
                recommended_list_menu(recommended_list, getIndex, preferredCuisine, preferredFood, availableBudget)
            else:
                if userInputRLM == int(previousMenuOption):
                    questions_menu()
                elif userInputRLM == int(previousMenuOption + 1):
                    main_menu()
                elif userInputRLM == int(previousMenuOption + 2):
                    print('Thank you for using our Restaurant Recommendation Platform!')
                    sys.exit()
                else:
                    getSelectedResIndex = getIndex[userInputRLM - 1]
                    recommended_details_menu(getSelectedResIndex, recommended_list, getIndex, preferredCuisine, preferredFood, availableBudget)
    except ValueError:
        print('\n[ERROR] Incorrect input format! Use ONLY NUMBERS (1-' + str(previousMenuOption + 2) +')\n\n')
        recommended_list_menu(recommended_list, getIndex, preferredCuisine, preferredFood, availableBudget)


def recommended_details_menu(getSelectedResIndex, recommended_list, getIndex, preferredCuisine, preferredFood, availableBudget):
    detailList = data()
    occupancyRate = int(detailList['Occupancy Rate (%)'][getSelectedResIndex] * 100)
    if occupancyRate < 40:
        occupancyCategory = 'Green'
        categoryMessage = 'Fantastic! There are sufficient seats at this restaurant.'
        categoryMessage2 = ''
    elif occupancyRate >= 40 and occupancyRate <= 70:
        occupancyCategory = 'Orange'
        categoryMessage = 'Take note seats are filling up fast at this restaurant.'
        categoryMessage2 = '\n        You may wish to head there now or consider other restaurants instead.'
    elif occupancyRate > 70:
        occupancyCategory = 'Red'
        categoryMessage = 'Warning! This restaurant is almost full! You may wish to consider other'
        categoryMessage2 = '\n     restaurants instead.'
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('<< ' + detailList['Name of Restaurant'][getSelectedResIndex] +' >>')
    print('\nCuisine: ' + detailList['Cuisine'][getSelectedResIndex])
    print('\nAddress: ' + detailList['Address'][getSelectedResIndex])
    print('Opening Hours: ' + detailList['Opening Hours'][getSelectedResIndex])
    print('Contact Number: ' + detailList['Contact Number'][getSelectedResIndex])
    print('\nRestaurant URL: ' + detailList['Restaurant URL'][getSelectedResIndex])
    print('Online Menu: ' + detailList['Online Menu'][getSelectedResIndex])
    print('\nOccupancy Rate: ' + str(detailList['Occupancy Rate (%)'][getSelectedResIndex] * 100) + ' %')
    print(occupancyCategory + ': ' + categoryMessage + categoryMessage2)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
    
    print('Please select the following:')
    print('[1] Open Restaurant URL')
    print('[2] Open Online Menu')
    print('[3] Return to previous menu')
    print('[4] Return to main menu')
    print('[5] Exit the platform')
    
    userInputRDM = input('Enter your input: ').strip().replace(' ', '')
    try:
        userInputRDM = int(userInputRDM)
        if userInputRDM not in range(1, 6):
            print('\n[ERROR] Invalid Input! Please choose option 1-5\n\n')
            recommended_details_menu(getSelectedResIndex, recommended_list, getIndex, preferredCuisine, preferredFood, availableBudget)
        else:
            confirmIndicatorRDM = confirmation_msg(userInputRDM)
            if confirmIndicatorRDM == 0:
                recommended_details_menu(getSelectedResIndex, recommended_list, getIndex, preferredCuisine, preferredFood, availableBudget)
            else:
                if userInputRDM == 1:
                    if detailList['Restaurant URL'][getSelectedResIndex] == 'NIL':
                        print('[ERROR] No Restaurant URL available\n')
                    else:
                        webbrowser.open(detailList['Restaurant URL'][getSelectedResIndex])
                    recommended_details_menu(getSelectedResIndex, recommended_list, getIndex, preferredCuisine, preferredFood, availableBudget)
                elif userInputRDM == 2:
                    if detailList['Online Menu'][getSelectedResIndex] == 'NIL':
                        print('[ERROR] No Online Menu URL available\n')
                    else:
                        webbrowser.open(detailList['Online Menu'][getSelectedResIndex])
                    recommended_details_menu(getSelectedResIndex, recommended_list, getIndex, preferredCuisine, preferredFood, availableBudget)
                elif userInputRDM == 3:
                    recommended_list_menu(recommended_list, getIndex, preferredCuisine, preferredFood, availableBudget)
                elif userInputRDM == 4:
                    main_menu()
                elif userInputRDM == 5:
                    print('Thank you for using our Restaurant Recommendation Platform!')
                    sys.exit()
    except ValueError:
        print('\n[ERROR] Incorrect input format! Use ONLY NUMBERS (1-5)\n\n')
        recommended_details_menu(getSelectedResIndex, recommended_list, getIndex, preferredCuisine, preferredFood, availableBudget)


def main():
   main_menu()
   
    
if __name__ == '__main__':
    main()