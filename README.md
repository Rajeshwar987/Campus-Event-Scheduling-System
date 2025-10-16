
# Campus Event Scheduling System

<img width="1000" height="714" alt="image" src="https://github.com/user-attachments/assets/13b276ca-03bc-49cf-9ddd-6df78752afd3" />


This repository contains a lightweight Python system for managing campus events, including talks, hackathons, concerts, and exams. It is designed to handle event storage, searching, sorting efficiently, and conflict detection as the dataset grows from a handful to millions of events.

---

## Features

- **Custom Data Structures**  
  - Dynamic Array (ArrayList-like)  
  - Singly Linked List  

- **Event Operations**  
  - Insert, delete, search by ID, list all events  
  - Event attributes: `id`, `title`, `date` (YYYY-MM-DD), `time` (HH: MM), `location`  

- **Sorting Algorithms**  
  - Insertion Sort  
  - Merge Sort  
  - Quick Sort  
  - Sort events by date + time on both array and linked list backends  

- **Searching & Conflict Detection**  
  - Linear and Binary Search by event ID  
  - Efficient conflict detection for overlapping events on the same date  

- **Scalability Analysis**  
  - Performance benchmarking for 50, 500, 5,000, 50,000, and 1,000,000 events  
  - Memory usage estimation for array vs linked list  
  - Design suggestions for parallel conflict detection  

- **Testing & Validation**  
  - Fully tested using `pytest`  
  - Experimental results and visualizations in a Jupyter notebook  

---

## Project Structure

Core Code (/src folder with modular Python files for DS/algorithms).

Testing Suite (/tests using pytest).

Final Report Notebook (.ipynb) with experiments, graphs, and explanations.

README.md explaining roles, setup, and results.
---

## TEAM CONTRIBUTIONS
-
 -Natarajan: part B, part D
 
 -Rajesh: Test suites, part D, Convert notebook to a project structure 
 
 -Samawita: Part A linked list, part C conflict detection, part D
 
 -Linh: Part A array, part C searching, part D