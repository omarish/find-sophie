from loader import load_data 
from path_finder import pick_next_room, distance
from math import log
import random
import csv
import numpy as np


rooms, costs = load_data()


def simulate(sophie_room):
    current_room = 'front_door'
    visited_rooms = set([current_room])
    total_time = 0
    trip = [current_room]
    print "Running a simulation. Sophie is in %s" % sophie_room
    print "Starting at %s" % current_room

    while sophie_room != current_room:
        # print "In %s. Total travel time is %s." % (current_room, total_time)
        possible_rooms = list(set(rooms.keys()) - visited_rooms)
        cost, path = pick_next_room(current_room, possible_rooms, costs, rooms)
        while len(path) > 0:
            next_room = path.popleft()
            trip.append(next_room)
            total_time += distance(current_room, next_room, costs)
            print "Visiting %s. Travel time is %s" % (next_room, total_time)
            current_room = next_room
            visited_rooms.add(current_room)
            if current_room == sophie_room:
                print "Found Sophie"
                break
            else:
                print "Did not find Sophie."
    return {
        'sophie_room': sophie_room,
        'total_time': total_time,
        'trip': "=>".join(trip)
    }

simulate('under_bed')
