import random
import time
import matplotlib.pyplot as plt
from datetime import datetime

from src.event_management import event, EventList, linkedList
from src.sorting import insertion_sort, merge_sort, quick_sort, event_key, merge_by_id, merge_sort_by_id 
from src.searching import linear_search, binary_search


def generate_events(n):
    events = []
    for i in range(n):
        events.append(event(
            i,
            f"Event{i}",
            f"2024-05-{(i % 28) + 1:02d}",
            f"{(i % 24):02d}:{(i * 7) % 60:02d}",
            "Campus Hall"
        ))
    random.shuffle(events)
    return events

def benchmark_algorithms_both():
    sizes = [50, 500]
    algorithms = {
        "Insertion": insertion_sort,
        "Merge": merge_sort,
        "Quick": quick_sort
    }

    results = {f"{name}_Array": [] for name in algorithms}
    results.update({f"{name}_Linked": [] for name in algorithms})

    for n in sizes:
        events = generate_events(n)

        arr_backend = EventList(n)
        for e in events:
            arr_backend.insertEvent(e)

        for name, func in algorithms.items():
            arr_copy = arr_backend.eventArr[:arr_backend.size]
            start = time.time()
            func(arr_copy)
            end = time.time()
            runtime = end - start
            results[f"{name}_Array"].append(runtime)
            print(f"{name} Sort (Array) | n={n} | {runtime:.5f}s")

        # LINKED LIST BACKEND
        ll_backend = linkedList()
        for e in events:
            ll_backend.insert(e, 0)


        for name, func in algorithms.items():
            temp_list = []
            current = ll_backend.head
            while current:
                temp_list.append(current.data)
                current = current.next

            start = time.time()
            sorted_arr = func(temp_list) 
            end = time.time()
            runtime = end - start
            results[f"{name}_Linked"].append(runtime)
            print(f"{name} Sort (Linked) | n={n} | {runtime:.5f}s")


    return sizes, results


def plot_results_both(sizes, results, title="Sorting Performance: Array vs Linked List"):
    for name in results:
        plt.plot(sizes, results[name], marker='o', linestyle='-', label=name) 
    plt.xlabel("Number of Events (n)")
    plt.ylabel("Runtime (seconds)")
    plt.title(title)
    plt.legend()
    plt.xscale("log")
    plt.yscale("log")
    plt.grid(True, which="both", linestyle='--', linewidth=0.5) 
    plt.show()


if __name__ == "__main__":
    print("--- Demonstrating Event Management ---")
    array_list = EventList(5)
    event1 = event(1, "Conference", "2024-06-15", "09:00", "Room 101")
    event2 = event(2, "Workshop", "2024-06-16", "14:00", "Lab 3")
    event3 = event(3, "Meetup", "2024-06-15", "18:00", "Cafe")

    array_list.insertEvent(event1)
    array_list.insertEvent(event2)
    array_list.insertEvent(event3)

    print("\nArray List:")
    print(array_list)
    print(f"Size: {len(array_list)}")

    print("\nSearching Array List:")
    array_list.searchById(2)
    array_list.searchById(99)

    print("\nDeleting from Array List:")
    array_list.deleteEvent(event2)
    print(array_list)
    print(f"Size: {len(array_list)}")

    print("\n--- Demonstrating Linked List Event Management ---")
    linked_list = linkedList()
    linked_list.insert(event1, 0)
    linked_list.insert(event2, 0)
    linked_list.insert(event3, 1) 

    print("\nLinked List:")
    print(linked_list)
    print(f"Size: {len(linked_list)}")

    print("\nSearching Linked List:")
    linked_list.searchbyId(1)
    linked_list.searchbyId(99)

    print("\nDeleting from Linked List:")
    linked_list.deleteEvent(2)
    print(linked_list)
    print(f"Size: {len(linked_list)}")

    print("\n--- Demonstrating Searching Algorithms ---")
    search_events_list = generate_events(100)
    search_array_list = EventList(100)
    for e in search_events_list:
        search_array_list.insertEvent(e)

    
    print("\nLinear Search:")
    linear_search(search_array_list, search_events_list[50].id) 
    linear_search(search_array_list, 999) 

    print("\nBinary Search:")
    sorted_search_array = merge_sort_by_id(search_array_list.eventArr[:search_array_list.size])
    binary_search(sorted_search_array, search_events_list[25].id)
    binary_search(sorted_search_array, 999) 


    print("\n--- Running Benchmarks ---")
    # Run benchmarks and plot results
    benchmark_sizes, benchmark_results = benchmark_algorithms_both()
    plot_results_both(benchmark_sizes, benchmark_results)