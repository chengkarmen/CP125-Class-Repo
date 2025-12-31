def find_station(stations, name):
    if name not in stations:
        return 
    for i in range(len(stations)):
        if stations[i] == name:
            return i

        


def count_stops(stations, start, stop):
    start = find_station(stations, start)
    stop = find_station(stations, stop)
    if start == None or stop == None:
        return -1
    return abs(stop - start)