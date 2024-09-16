#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    # loop through tickets
        #check for a source = NONE
            # if so then that is the start
            # if no NONE insert source and destination to ht
    # loop through the route, 
    # next route will start with the dest from the last one ( i-1)

    for t in tickets:
        if t.source == "NONE":
            route[0] = t.destination
        else:
            hash_table_insert(hashtable, t.source, t.destination)
    for i in range(1, len(tickets)):
        route[i] = hash_table_retrieve(hashtable, route[i-1])

    return route
