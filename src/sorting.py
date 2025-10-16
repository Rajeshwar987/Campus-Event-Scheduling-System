from datetime import datetime

#compare events chronologically
def event_key(event):
    """Convert event date+time to datetime object for comparison."""
    return datetime.strptime(event.date + " " + event.time, "%Y-%m-%d %H:%M")

# Insertion Sort
def insertion_sort(events):
    arr = events[:]
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and event_key(arr[j]) > event_key(key):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# Merge Sort
def merge_sort(events):
    if len(events) <= 1:
        return events
    mid = len(events) // 2
    left = merge_sort(events[:mid])
    right = merge_sort(events[mid:])
    return merge(left, right)

def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if event_key(left[i]) <= event_key(right[j]):
            merged.append(left[i]); i += 1
        else:
            merged.append(right[j]); j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


# Quick Sort
def quick_sort(events):
    if len(events) <= 1:
        return events
    pivot = event_key(events[len(events)//2])
    left = [x for x in events if event_key(x) < pivot]
    middle = [x for x in events if event_key(x) == pivot]
    right = [x for x in events if event_key(x) > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Merge Sort on event ID (instead of using date/time)
def merge_sort_by_id(events):
    if len(events) <= 1:
        return events
    mid = len(events) // 2
    left = merge_sort_by_id(events[:mid])
    right = merge_sort_by_id(events[mid:])
    return merge_by_id(left, right)

def merge_by_id(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i].id <= right[j].id:
            merged.append(left[i]); i += 1
        else:
            merged.append(right[j]); j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged