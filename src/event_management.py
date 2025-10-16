# Event Class
class event:
    def __init__(self, id, title, date, time, location):
        self.id = id
        self.title = title
        self.date = date
        self.time = time
        self.location = location
    def __repr__(self):
        return(f"id: {self.id}\ntitle: {self.title}\ndate: {self.date}\ntime: {self.time}\nlocation: {self.location}")

# Array-based list (dynamic sizing)
class EventList:
    def __init__(self, capacity):
        self.size = 0
        self.eventArr = []
        self.capacity = capacity

    #return the event list
    def __repr__(self):
        return(f"Event list: {self.eventArr[:(self.size)]}")

    #return the size of the event list
    def __len__(self):
        return(self.size)

    #INSERT OPERATION
    def insertEvent(self, event):
        if self.capacity - self.size != 0:
            self.eventArr.insert(0, event)
            self.size += 1
        else:
            new_arr = []
            for i in range(len(self.eventArr)):
                new_arr.append(self.eventArr[i])
            self.eventArr = new_arr
            self.capacity *= 2
            self.eventArr.insert(0, event)
            self.size += 1


    #SEACH-BY-ID OPERATION
    def searchById(self, searchId):
        found = False
        for i in range(len(self.eventArr)):
            if self.eventArr[i].id == searchId:
                found = True
                print(f"The matching event is {self.eventArr[i].title}")
                return self.eventArr[i] # Return the found event
        if found == False:
            print(f"No matching event based on event ID {searchId}")
            return None # Return None if not found


    #DELETE OPERATION:
    def getIndex(self, eventId):
        for i in range(self.size):
            if self.eventArr[i].id == eventId:
                return i
        return -1

    def deleteEvent (self, event):
        deleteIndex = self.getIndex(event.id)
        if deleteIndex == -1:
            print(f"Event {event.title} not found")
        else:
            for i in range (deleteIndex, self.size - 1):
                self.eventArr[i] = self.eventArr[i + 1]
            self.size -= 1
            self.eventArr[self.size-1]=None
            print(f'Event {event.title} is deleted')

    #LIST-ALL OPERATION
    def listAllEvents(self):
        for i in range(self.size):
            print(f"{self.eventArr[i]}")

#Second Implementation: Singly linked list
#Node Class
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

#Linked List class
class linkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    #Display linked list
    def __str__(self):
        temp = self.head
        toPrint = ""
        while temp:
            toPrint += f"{temp.data}\n"
            temp = temp.next
        return toPrint

    # Return size of linked list
    def __len__(self):
        return self.size

    # Insertion at a particular position
    def insert(self,event,pos):
        temp_node=Node(event)  
        if pos==0: # Simplified condition
            temp_node.next=self.head
            self.head=temp_node
            self.size += 1
            return
        # insertion in the middle or end
        current=self.head
        count=0
        while current.next and count< pos-1:
            current=current.next
            count=count+1

        if count==pos-1:
            temp_node.next=current.next
            current.next=temp_node
            self.size += 1
            return
        

    # event deletion
    def deleteEvent(self, event_id):
        current=self.head
        prev=None

        #empty list
        if current is None:
            print("Empty list!")
            return

        #Deletion of head node
        if current.data.id == event_id:
            self.head=current.next
            self.size -= 1
            return

        #Deletion in the middle
        while current and current.data.id!=event_id:
            prev=current
            current=current.next
        #event_id not found
        if current is None:
            print(f"event with ID {event_id} not found") # Added confirmation message
            return

        else:
            prev.next=current.next
            self.size -= 1
            print(f"Event with ID {event_id} deleted.") # Added confirmation message
            return


    #Search by id
    def searchbyId(self,event_id):
        current=self.head
        pos=0
        while current:
            if current.data.id==event_id:
                print(f"event with ID {event_id} found at node {pos} !") # Added confirmation message
                return current.data # Return the found event
            current=current.next
            pos+=1
        print(f"No matching event with id {event_id} found!")
        return None 