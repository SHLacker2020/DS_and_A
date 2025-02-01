from hmac import new
from flask import Flask, request, jsonify

# Task: Write a Python function using the Flask framework to manage a simple to-do list. Your API should support the following operations: adding a new task, getting a list of all tasks, updating a task description, and deleting a task.

# Input Format: For adding a new task, the input should be a JSON object like `{“task”: “Buy groceries”}`.

# Constraints:

# The task description will be a non-empty string.
# Each task will have a unique identifier.
# Output Format: The output should also be in JSON format. For fetching all tasks, the output should look like `[{“id”: 1, “task”: “Buy groceries”}, {“id”: 2, “task”: “Read a book”}]`.

app = Flask(__name__) # Create a Flask app

tasks = [] # Initialize an empty list to store tasks
task_id = 1 # Initialize a task ID counter

# GET request to fetch all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks) # Return the list of tasks in JSON format

# POST request to add a new task
@app.route('/tasks', methods=['POST'])
def add_task():
    global task_id # Access the global task ID counter
    new_task = {"id": task_id, "task": request.json['task']} # Create a new task object with the given description
    tasks.append(new_task) # Add the new task to the list
    task_id += 1
    return jsonify(new_task)

# PUT request to update a task description
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['task'] = request.json['task'] # if the task ID matches, update the task description
    return jsonify({"message": "Task updated successfully"}) # return a success message

# DELETE request to delete a task
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task) # if the task ID matches, remove the task from the list
    return jsonify({"message": "Task deleted successfully"}) # return a success message


if __name__ == '__main__':
    app.run(debug=True) # Run the Flask app in debug mode on localhost

