import time

# Linear Search
def linear_search(event_list, searchId):
    """Performs a linear search on an array-based event list by event ID."""
    begin_linear = time.time()
    found = False
    for event in event_list.eventArr[:event_list.size]:
        if event.id == searchId:
            found = True
            end_linear = time.time()
            print(f"Time for linear search (ID {searchId} found) is {end_linear - begin_linear}")
            print(f"The matching event is {event.title}")
            return event
    end_linear = time.time()
    print(f"Time for linear search (ID {searchId} not found) is {end_linear - begin_linear}")
    if found == False:
        print(f"No matching event based on event ID {searchId}")
        return None 


#Binary search
def binary_search(eventArr, eventID):
    high = len(eventArr)-1
    low = 0
    begin_binary = time.time()
    while low <= high:
      middle = low+(high-low)//2
      event_at_mid = eventArr[middle].id
      if eventID == event_at_mid:
        end_binary = time.time()
        print(f"Time for binary search (ID {eventID} found) is {end_binary - begin_binary}")
        return middle
      elif eventID > event_at_mid:
        low = middle + 1
      else:
        high = middle - 1
    end_binary = time.time()
    print(f"Time for binary search (ID {eventID} not found) is {end_binary - begin_binary}")
    return(f"No event with ID {eventID} is found")