from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/todo', methods=['GET'])
def get_todo_list():
    # Your logic to retrieve TODO list data
    todo_list = ["Task 1", "Task 2", "Task 3"]
    return jsonify({"todoList": todo_list})

if __name__ == '__main__':
    app.run(debug=True)
