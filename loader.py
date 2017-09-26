import re

def load_data(path = 'data/sample.txt'):
    """
    Load data and return a tuple of (rooms, costs).

    rooms: a dictionary mapping each room with the probability
    Sophie is in that room.

    costs: a dictionary with the cost to go from one room to another.
    The key is a tuple (room -> room) and the value is the cost.
    """
    with open(path, 'r') as f:
        lines = f.read().splitlines()
        count_rooms, rest = int(lines[0]), lines[1:]
        rooms = dict(map(parse_room, rest[:count_rooms]))
        costs = dict(map(parse_cost, rest[(count_rooms + 1):]))    
    return (rooms, costs)

def parse_room(row):
    """
    >>> parse_room('front_door    .2')
    ('front_door', 0.2)
    """
    room_name, probability = re.split(r'\s+', row)
    return (room_name, float(probability))

def parse_cost(row):
    """
    >>> parse_cost('front_door under_bed     5')
    (('front_door', 'under_bed'), 5.0)
    """
    origin, destination, cost = re.split(r'\s+', row)
    return ((origin, destination), float(cost))
