# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    start_node = problem.getStartState() # Getting the starting node
     # Checking if the starting node is already a goal state
    if problem.isGoalState(start_node):
        return []

    node_stack = util.Stack()
    visited_nodes = [] # To keep track of all the visited nodes
    # Initialize a stack for depth-first search
    node_stack.push((start_node, []))

    while not node_stack.isEmpty():
        current_node, actions = node_stack.pop()
        # If the current node has not been visited yet
        if current_node not in visited_nodes:
            visited_nodes.append(current_node)

            # If the current node is a goal state, return the list of actions
            if problem.isGoalState(current_node):
                return actions

            # Expand the current node by adding its successors to the stack
            for nextNode, action, cost in problem.getSuccessors(current_node):
                new_actions = actions + [action]
                node_stack.push((nextNode, new_actions))
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    
    start_node = problem.getStartState()# Getting the starting node

    # Checking if the starting node is already a goal state
    if problem.isGoalState(start_node):
        return []

    # Initializing a queue for breadth-first search and a list to keep track of all visited nodes
    node_queue = util.Queue()
    visited_nodes = []

    # Enqueue the starting node with an empty list of actions
    node_queue.push((start_node, []))

    while not node_queue.isEmpty():
        current_node, actions = node_queue.pop()

        # If the current node has not been visited yet
        if current_node not in visited_nodes:
            visited_nodes.append(current_node)

            # If the current node is a goal state, return the list of actions
            if problem.isGoalState(current_node):
                return actions

            # Expand the current node by adding its successors to the queue
            for next_node, action, cost in problem.getSuccessors(current_node):
                new_actions = actions + [action]
                node_queue.push((next_node, new_actions))
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    
    # Get the starting node
    start_node = problem.getStartState()

    # Check if the starting node is already a goal state
    if problem.isGoalState(start_node):
        return []

    visited_nodes = []

    priority_queue = util.PriorityQueue()
    # ((coordinate/node, action to current node, cost to current node), priority)
    priority_queue.push((start_node, [], 0), 0)

    while not priority_queue.isEmpty():

        current_node, actions, prev_cost = priority_queue.pop()

        # If the current node has not been visited yet
        if current_node not in visited_nodes:
            visited_nodes.append(current_node)

            # If the current node is a goal state, return the list of actions
            if problem.isGoalState(current_node):
                return actions

            # Expand the current node by adding its successors to the priority queue
            for next_node, action, step_cost in problem.getSuccessors(current_node):
                new_actions = actions + [action]
                total_cost = prev_cost + step_cost
                priority_queue.push((next_node, new_actions, total_cost), total_cost)
    
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    
    start_node = problem.getStartState()# Getting the starting node

    # Checking if the starting node is already a goal state
    if problem.isGoalState(start_node):
        return []

    visited_nodes = []  # To keep track of all the visited nodes

    priority_queue = util.PriorityQueue() #initializing a priority queue
    priority_queue.push((start_node, [], 0), 0)# ((coordinate/node, action to current node, cost to current node), priority)

    while not priority_queue.isEmpty():
        current_node, actions, prev_cost = priority_queue.pop()

        # If the current node has not been visited yet
        if current_node not in visited_nodes:
            visited_nodes.append(current_node)

            # If the current node is a goal state, return the list of actions
            if problem.isGoalState(current_node):
                return actions

            # Expand the current node by adding its successors to the priority queue
            for next_node, action, step_cost in problem.getSuccessors(current_node):
                new_actions = actions + [action]
                new_cost_to_node = prev_cost + step_cost
                heuristic_cost = new_cost_to_node + heuristic(next_node, problem)
                priority_queue.push((next_node, new_actions, new_cost_to_node), heuristic_cost)
    
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
