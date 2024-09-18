from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

ROWS = 10
COLS = 10

def generate_maze():
    maze = [[0 for _ in range(COLS)] for _ in range(ROWS)]
    start = (0, 0)
    end = (ROWS - 1, COLS - 1)
    for row in range(ROWS):
        for col in range(COLS):
            if (row, col) != start and (row, col) != end:
                maze[row][col] = 1 if random.random() < 0.3 else 0
    return maze

def solve_maze(maze):
    path = []
    return path

@app.route('/home')
def index():
    return render_template('frontend.html')

@app.route('/generate-maze', methods=['GET'])
def generate_maze_endpoint():
    maze = generate_maze()
    return jsonify({'maze': maze})

@app.route('/solve-maze', methods=['POST'])
def solve_maze_endpoint():
    data = request.get_json()
    maze = data.get('maze')
    if maze:
        path = solve_maze(maze)
        return jsonify({'path': path})
    else:
        return jsonify({'error': 'No maze data provided'}), 400

if __name__ == '__main__':
    app.run(debug=True)
