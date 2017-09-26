from collections import deque
from math import log


def find_best_path(origin, destination, arcs, nodes):
    """
    Return a tuple of (best_path, cost)
    """
    visited_nodes = set()
    best_cost, best_path = float("inf"), None
    queue = deque()
    queue.append(([origin], 0))
    visited_nodes.add(origin)

    while len(queue) > 0:
        path, cost = queue.popleft()
        node = path[-1]
        visited_nodes.add(node)

        if (node == destination):
            if (cost < best_cost):
                # found a better cost
                best_cost = cost
                best_path = path
        else:
            for neighbor, distance in get_neighbors(node, arcs):
                if not neighbor in visited_nodes:
                    prob = nodes[node]
                    extra_cost = calc_cost(prob, distance)
                    queue.append((path + [neighbor], cost + extra_cost))
    return best_path, best_cost

def get_neighbors(origin, arcs):
    result = set()
    for pair in arcs.keys():
        cost = arcs[pair]
        if pair[0] == origin:
            result.add((pair[1], cost))
        elif pair[1] == origin:
            result.add((pair[0], cost))
    return list(result)


def distance(origin, destination, arcs):
    target = (origin, destination)
    if target in arcs:
        return arcs[target]
    else:
        return arcs[(destination, origin)]


def calc_cost(probability, distance):
    return distance * log(1.0 / probability)


def pick_next_room(origin, options, arcs, nodes):
    """
    You're at origin. Pick the next room. Return a path to travel.
    """
    result = []
    for destination in options:
        path, cost = find_best_path(origin, destination, arcs, nodes)
        result.append((cost, path))
    s = sorted(result, key = lambda item: item[0])[0]
    return s[0], deque(s[1][1:])
