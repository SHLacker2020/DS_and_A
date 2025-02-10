from flask import Flask, request, jsonify
from functools import wraps


app = Flask(__name__) # Create a Flask app

tasks = [] # Initialize an empty list to store tasks
task_id = 1 # Initialize a task ID counter
users = {} # Initialize an empty dictionary to store users

# POST request to create a new user
# To create a user, send a JSON object with "username" and "password" fields in the request body
@app.route('/users', methods=['POST'])
def create_user():
    username = request.json['username']
    password = request.json['password']
    # make a message for a 400 error
    if not username or not password:
        return jsonify({"message": "Please enter like: username: password"}), 400
    if username in users:
        return jsonify({"message": "User already exists"}), 400
    users[username] = password
    return jsonify({"message": "User created successfully"}), 201

# Function to check if the username and password are valid
def check_auth(username, password):
    return username in users and users[username] == password

# Decorator function to require authentication for certain routes
def requires_auth(f):
    @wraps(f) # Preserve the original function's metadata
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return jsonify({"message": "Authentication required"}), 401
        return f(*args, **kwargs)
    return decorated

# GET all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# GET request to fetch all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    offset = request.args.get('offset', 0) # Get the offset parameter from the query string
    limit = request.args.get('limit', len(tasks)) # Get the limit parameter from the query string
    tasks_slice = tasks[int(offset):int(offset) + int(limit)] # Get a slice of tasks based on the offset and limit
    return jsonify(tasks_slice) # Return the list of tasks in JSON format

# POST request to add a new task
@app.route('/tasks', methods=['POST'])
@requires_auth
def add_task():
    global task_id # Access the global task ID counter
    global users # Access the global users dictionary
    auth = request.authorization
    new_task = {"id": task_id,
                "task": request.json['task'] if request.json and 'task' in request.json else None,
                "owner": auth.username} # Create a new task object with the given description
    tasks.append(new_task) # Add the new task to the list
    task_id += 1
    return jsonify(new_task)

# PUT request to update a task description
@app.route('/tasks/<int:task_id>', methods=['PUT'])
@requires_auth
def update_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['task'] = request.json['task'] # if the task ID matches, update the task description
    return jsonify({"message": "Task updated successfully"}) # return a success message

# DELETE request to delete a task
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
@requires_auth
def delete_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task) # if the task ID matches, remove the task from the list
    return jsonify({"message": "Task deleted successfully"}) # return a success message


if __name__ == '__main__':
    app.run(debug=True) # Run the Flask app in debug mode on localhost

