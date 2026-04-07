# cisc121project
CISC121 Project
# 🔍 Linear Search Visualizer

## Demo

Here is my app showing step-by-step linear search
<img width="2022" height="1057" alt="image" src="https://github.com/user-attachments/assets/35a03251-9293-40d6-91b7-b7bf17ea3fff" />


---

## Problem Breakdown & Computational Thinking

### Decomposition

The problem is broken into smaller steps:

* Take user input (a list of numbers and a target value)
* Convert the input into a list of integers
* Loop through the list one element at a time
* Compare each element to the target
* Return the result with step-by-step explanation

### Pattern Recognition

The algorithm follows a repeated pattern:

* Check each element sequentially
* Continue until the target is found or the list ends

### Abstraction

The user does not need to understand the internal Python logic.
They simply input values and observe how the algorithm works step-by-step.
This simplifies the complexity while still demonstrating the key idea of linear search.

### Algorithm Design

1. Convert the input string into a list of integers
2. Convert the target into an integer
3. Loop through the list
4. At each step:

   * Display which index is being checked
   * Compare the value with the target
5. If found → return index and steps
6. If not found → return "not found" message

---

## Algorithm Explanation

Linear search is a simple algorithm that checks each element in a list one by one until the target value is found.

* Start from the first element
* Compare each element to the target
* If a match is found, return its index
* If no match is found after checking all elements, return "not found"

This implementation also shows each step of the search process to help users understand how the algorithm works.

---

## Design

The application allows users to:

* Enter a list of numbers (comma-separated)
* Enter a target number

When the user clicks the **Search** button:

* The program performs a linear search
* Displays each step of the process
* Shows whether the target was found or not

The interface is built using Gradio and is designed to be simple, clear, and educational.

---

## Testing & Verification

The application was tested using multiple scenarios:

* Target exists in the list
  Example: `1, 5, 3, 9` → target `3`
  Output shows step-by-step checks and returns `Found at index 2`

* Target does not exist
  Example: `1, 5, 3, 9` → target `7`
  Output shows all steps and returns `Not found`

* Invalid input
  Example: entering letters instead of numbers
  Output: `Invalid input`

These tests confirm that the algorithm behaves correctly and handles edge cases.

---

## How to Run

1. Install dependencies:
   pip install gradio

2. Run the application:
   python app.py

---

## Hugging Face Deployment

You can access the live app here:
👉 https://huggingface.co/spaces/LukasChin-Queens/CISC121Project

---

## Author

Your Name

---

## Acknowledgment

This project was developed for CISC-121.
Some guidance and structure were supported using AI tools for learning purposes.
