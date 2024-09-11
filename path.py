import random
import networkx as nx
import matplotlib.pyplot as plt

class Maze:
    def __init__(self, width, height, obstacle_ratio=0.2):
        self.width = width
        self.height = height
        self.obstacle_ratio = obstacle_ratio
        self.grid = self.generate_grid()
        self.robot = (0, 0)
        self.treasure = (height - 1, width - 1)

    def generate_grid(self):
        grid = [['.' for _ in range(self.width)] for _ in range(self.height)]
        num_obstacles = int(self.width * self.height * self.obstacle_ratio)
        obstacles = random.sample([(i, j) for i in range(self.height) for j in range(self.width)
                                   if (i, j) not in [(0, 0), (self.height-1, self.width-1)]], num_obstacles)
        for (i, j) in obstacles:
            grid[i][j] = '0'
        return grid

    def is_solvable(self): #i used chatgbt in this part the code in the session didn't work well with me
        # Use A* to check if there's a path
        G = self.build_graph()
        try:
            path = nx.astar_path(G, self.robot, self.treasure)
            return True, path
        except nx.NetworkXNoPath:
            return False, []

    def build_graph(self):
        G = nx.grid_2d_graph(self.height, self.width)
        for i in range(self.height):
            for j in range(self.width):
                if self.grid[i][j] == '0':  
                    G.remove_node((i, j))
        return G

    def display(self, path=None):
        for i in range(self.height):
            for j in range(self.width):
                if (i, j) == self.robot:
                    print('R', end=' ')
                elif (i, j) == self.treasure:
                    print('T', end=' ')
                elif path and (i, j) in path:
                    print('P', end=' ')
                else:
                    print(self.grid[i][j], end=' ')
            print() 

class AStarSolver:
    def __init__(self, maze):
        self.maze = maze

    def solve(self):
        solvable, path = self.maze.is_solvable()
        if solvable:
            print("Maze Solvable! Path found:")
            self.maze.display(path)
        else:
            print("No path found. Regenerating maze...")
            self.maze.grid = self.maze.generate_grid()
            self.solve()

if __name__ == "__main__":
    maze = Maze(5, 5)
    solver = AStarSolver(maze)
    solver.solve()

