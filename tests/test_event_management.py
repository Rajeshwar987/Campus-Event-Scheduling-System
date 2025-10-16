import unittest
from src.event_management import event, EventList, linkedList, Node 

class TestEvent(unittest.TestCase):
    def test_event_creation(self):
        event1 = event(1, "Test Event", "2024-07-01", "10:00", "Campus Hall")
        self.assertEqual(event1.id, 1)
        self.assertEqual(event1.title, "Test Event")
        self.assertEqual(event1.date, "2024-07-01")
        self.assertEqual(event1.time, "10:00")
        self.assertEqual(event1.location, "Campus Hall")

class TestEventList(unittest.TestCase):
    def test_event_list_creation(self):
        event_list = EventList(5)
        self.assertEqual(event_list.size, 0)
        self.assertEqual(event_list.capacity, 5)
        self.assertEqual(len(event_list.eventArr), 0) # Initial list is empty

    def test_insert_event(self):
        event_list = EventList(2)
        event1 = event(1, "Event 1", "2024-07-01", "10:00", "Campus Hall")
        event2 = event(2, "Event 2", "2024-07-02", "11:00", "Campus Hall")
        event3 = event(3, "Event 3", "2024-07-03", "12:00", "Campus Hall")

        event_list.insertEvent(event1)
        self.assertEqual(event_list.size, 1)
        self.assertEqual(event_list.eventArr[0].id, 1)

        event_list.insertEvent(event2)
        self.assertEqual(event_list.size, 2)
        self.assertEqual(event_list.eventArr[0].id, 2) # Inserted at the beginning
        self.assertEqual(event_list.eventArr[1].id, 1)

        # Test resizing
        event_list.insertEvent(event3)
        self.assertEqual(event_list.size, 3)
        self.assertEqual(event_list.capacity, 4) 
        self.assertEqual(event_list.eventArr[0].id, 3)


    def test_search_by_id(self):
        event_list = EventList(3)
        event1 = event(1, "Event 1", "2024-07-01", "10:00", "Campus Hall")
        event_list.insertEvent(event1)
        event2 = event(2, "Event 2", "2024-07-02", "11:00", "Campus Hall")
        event_list.insertEvent(event2)

        found_event = event_list.searchById(1)
        self.assertEqual(found_event.id, 1)

        not_found_event = event_list.searchById(99)
        self.assertIsNone(not_found_event)


    def test_delete_event(self):
        event_list = EventList(3)
        event1 = event(1, "Event 1", "2024-07-01", "10:00", "Campus Hall")
        event_list.insertEvent(event1)
        event2 = event(2, "Event 2", "2024-07-02", "11:00", "Campus Hall")
        event_list.insertEvent(event2) # Insert event2
        event3 = event(3, "Event 3", "2024-07-03", "12:00", "Campus Hall")
        event_list.insertEvent(event3)

        initial_size = len(event_list)
        event_list.deleteEvent(event2) # Delete existing event
        self.assertEqual(len(event_list), initial_size - 1)
        self.assertIsNone(event_list.searchById(2)) # Should not be found after deletion

        # Test deleting a non-existent event
        event_list.deleteEvent(event(99, "Non-existent", "", "", "Campus Hall"))
        # The size should not change when deleting a non-existent event
        self.assertEqual(len(event_list), initial_size - 1) # Size should remain initial_size - 1


class TestLinkedList(unittest.TestCase):
    def test_linked_list_creation(self):
        linked_list = linkedList()
        self.assertIsNone(linked_list.head)
        self.assertEqual(linked_list.size, 0)

    def test_insert(self):
        linked_list = linkedList()
        event1 = event(1, "Event 1", "2024-07-01", "10:00", "Campus Hall")
        event2 = event(2, "Event 2", "2024-07-02", "11:00", "Campus Hall")
        event3 = event(3, "Event 3", "2024-07-03", "12:00", "Campus Hall")

        linked_list.insert(event1, 0)
        self.assertEqual(linked_list.size, 1)
        self.assertEqual(linked_list.head.data.id, 1)

        linked_list.insert(event2, 0)
        self.assertEqual(linked_list.size, 2)
        self.assertEqual(linked_list.head.data.id, 2)
        self.assertEqual(linked_list.head.next.data.id, 1)

        linked_list.insert(event3, 1)
        self.assertEqual(linked_list.size, 3)
        self.assertEqual(linked_list.head.next.data.id, 3)
        self.assertEqual(linked_list.head.next.next.data.id, 1)

        # Test inserting at an invalid position
        linked_list.insert(event(4, "Event 4", "", "", "Campus Hall"), 5) # Position out of bounds
        self.assertEqual(linked_list.size, 3) # Size should not change


    def test_delete_event(self):
        linked_list = linkedList()
        event1 = event(1, "Event 1", "2024-07-01", "10:00", "Campus Hall")
        linked_list.insert(event1, 0)
        event2 = event(2, "Event 2", "2024-07-02", "11:00", "Campus Hall")
        linked_list.insert(event2, 0)
        event3 = event(3, "Event 3", "2024-07-03", "12:00", "Campus Hall")
        linked_list.insert(event3, 1)

        initial_size = len(linked_list)
        linked_list.deleteEvent(2) # Delete existing event
        self.assertEqual(len(linked_list), initial_size - 1)
        self.assertIsNone(linked_list.searchbyId(2)) # Should not be found after deletion

        # Test deleting head
        linked_list.deleteEvent(3) # event3 is now head after deleting event2
        self.assertEqual(len(linked_list), initial_size - 2)
        self.assertIsNone(linked_list.searchbyId(3))

        # Test deleting non-existent event
        linked_list.deleteEvent(99)
        self.assertEqual(len(linked_list), initial_size - 2) # Size should not change

    def test_search_by_id(self):
        linked_list = linkedList()
        event1 = event(1, "Event 1", "2024-07-01", "10:00", "Campus Hall")
        linked_list.insert(event1, 0)
        event2 = event(2, "Event 2", "2024-07-02", "11:00", "Campus Hall")
        linked_list.insert(event2, 0)

        found_event = linked_list.searchbyId(1)
        self.assertEqual(found_event.id, 1)

        not_found_event = linked_list.searchbyId(99)
        self.assertIsNone(not_found_event)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False) 