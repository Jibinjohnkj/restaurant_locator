import csv
import math as m
import numpy as np

open_time_slots = {
    'breakfast':range(800,1200),
    'lunch':range(1200,1600),
    'dinner':range(1800,2200)
}

def get_visitors():
    with open('visitor-locations-times.csv', 'r') as csvfile:
        visitors = csv.DictReader(csvfile, delimiter=',')
        for visitor in visitors:
            yield visitor

def get_restaurants():
    with open('sf-restaurants.csv', 'r') as csvfile:
        restaurants = csv.DictReader(csvfile, delimiter=',')
        for row in restaurants:
            yield row

def get_distance(loc1, loc2):
    lat1 = float(loc1['lat'])
    lon1 = float(loc1['lng'])
    lat2 = float(loc2['lat'])
    lon2 = float(loc2['lng'])

    distance = np.rad2deg(m.acos(m.sin(np.deg2rad(lat1)) * m.sin(np.deg2rad(lat2)) +
                                 m.cos(np.deg2rad(lat1)) * m.cos(np.deg2rad(lat2)) *
                                 m.cos(np.deg2rad(lon1 - lon2)))) * 60 * 1.1515
    return distance

def get_restaurant_in_timeslot(time):
    for restaurant in get_restaurants():
        if int(time) in open_time_slots[restaurant['timeslot']]:
            yield restaurant

def get_highly_rated_restaurants_near_me(visitor):
    near = []
    for restaurant in get_restaurant_in_timeslot(visitor['current_time']):
        distance = get_distance(visitor,restaurant)
        if distance <= 1:
            near.append(restaurant)
    highly_rated = sorted(near, key=lambda restaurant: restaurant['rating'], reverse=True)
    return highly_rated[:3]

def main():
    visitors = get_visitors()
    for no, visitor in enumerate(visitors):
        print("\nVisitor:{0}".format(no))
        highly_rated_restaurants = get_highly_rated_restaurants_near_me(visitor)
        for restaurant in highly_rated_restaurants:
            print("Restaurant: {0}, Rating: {1}".format(restaurant['restaurant_name'],restaurant['rating']))

if __name__ == '__main__':
    main()
