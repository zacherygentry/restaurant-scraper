from lxml import html
import requests
import grequests
from io import BytesIO
import random
from os import system, name

def getRestaurantsAtURL(URL):
    constantURL = URL
    restaurants = list()
    pageNum = 1
    while(1):
        try:
            tempURL = constantURL + '&page=' + str(pageNum)
            page = requests.get(tempURL)
            pageNum += 1
        except:
            print('exception')
            break

        tree = html.fromstring(page.content)
        # This will create a list of restaurant names:
        restaurantNames = tree.xpath('//span[@itemprop="name"]/text()')
        for x in range(0, 3):
            restaurantNames.pop(0)
        # This will create a list of street addresses
        numOfResults = tree.xpath('//div[@class="pagination"]//p/text()')
        print((pageNum - 1) * 30/ int(numOfResults[0]) * 100, '%')
        if(pageNum > int(numOfResults[0]) / 30 ):
            break
        streetAddresses = tree.xpath('//span[@class="street-address"]/text()')
        localities = tree.xpath('//span[@class="locality"]/text()')
        addressRegions = tree.xpath('//span[@itemprop="addressRegion"]/text()')
        postalCodes = tree.xpath('//span[@itemprop="postalCode"]/text()')

        for i in range(0, len(streetAddresses)):
            restaurant = {
                'name': restaurantNames[i],
                'streetAddress': streetAddresses[i],
                'locality': localities[i],
                'addressRegion': addressRegions[i],
                'postalCode': postalCodes[i]
            }
            restaurants.append(restaurant)
    return restaurants

def getNumberOfPages(URL):
    page = requests.get(URL)
    tree = html.fromstring(page.content)
    numOfResults = int(tree.xpath('//div[@class="pagination"]//p/text()'))
    return numOfResults

def getRestaurantsAtCity(city):
    city = city.replace(' ', '')
    return getRestaurantsAtURL('https://www.yellowpages.com/search?search_terms=restaurant&geo_location_terms=' + city + '%2C%20TX')

def findRestaurantsByName(restaurants, name):
    tempRestaurants = list()
    name = name.replace(' ', '').lower()
    for restaurant in restaurants:
        if(editDistance(restaurant['name'].replace(' ', '').lower(), name) < 4):
            tempRestaurants.append(restaurant)
    return tempRestaurants

def printRestaurant(restaurant):
    print('\n', restaurant['name'], '\n', restaurant['streetAddress'],
          restaurant['locality'], restaurant['addressRegion'], restaurant['postalCode'])

def printAllRestaurants(restaurants):
    for restaurant in restaurants:
        printRestaurant(restaurant)

def getRandomRestaurant(restaurants):
    return restaurants[random.randint(0, len(restaurants) - 1)]

def clear():
    _ = system('clear')

def editDistance(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    distances = range(len(s1) + 1)
    for i2, c2 in enumerate(s2):
        distances_ = [i2+1]
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
        distances = distances_
    return distances[-1]