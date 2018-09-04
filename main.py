
from functions import *
import cmd


def main():
    clear()
    while(1):
        city = input('Type in a city in Texas: ')
        restaurants = getRestaurantsAtCity(city)

        while(1):
            choice = input(
                '\nFound ' + str(len(restaurants)) + ' restaurants.\n' + 'What would you like to do?\n(1) Get all restaurants\n(2) Get a random restaurant\n(3) Find restaurant by name\n(4) Enter new city\n')
            try:
                choice = int(choice)
            except:
                print('\nNot a number')

            clear()
            if(choice == 1):
                printAllRestaurants(restaurants)
            elif(choice == 2):
                printRestaurant(getRandomRestaurant(restaurants))
            elif(choice == 3):
                name = input('Type in a restaurant name: ')
                printAllRestaurants(findRestaurantsByName(restaurants, name))
            elif(choice == 4):
                break
            else:
                continue


main()
