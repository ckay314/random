import sys
import numpy
from Queue import *

# solver of the N puzzle game
# assuming N = 3 here

global children_by_empty
children_by_empty = {0:[[3,1],['D','R']] , 1:[[4,0,2],['D','L','R']] , 2:[[5,1],['D','L']] , 3:[[0,6,4],['U','D','R']], 4:[[1,7,3,5],['U','D','L','R']] , 5:[[2,8,4],['U','D','L']] , 6:[[3,7],['U','R']] , 7:[[4,6,8],['U','L','R']] , 8:[[5,6],['U','L']] }

class state:
    # always use UDLR order
    # add corresponding directions?
    def __init__(self,board, path):
        self.board = board
        self.children = [] 
        self.empty = self.board.index(0)
        self.path =path
        #self.child_moves = []

        self.get_children()
        
    def get_children(self):
        #ordered_children = [[3,1], [4,0,2], [5,1], [0,6,4], [1,7,3,5], [2,8,4], [3,7], [4,6,8], [5,6]]
        #ordered_moves = [['D','R'], ['D','L','R'], ['D','L'], ['U','D','R'], ['U','D','L','R'], ['U','D','L'], ['U','R'], ['U','L','R'], ['U','L']]
        #children_by_empty = {0:[[3,1],['D','R']] , 1:[[4,0,2],['D','L','R']] , 2:[[5,1],['D','L']] , 3:[[0,6,4],['U','D','R']], 4:[[1,7,3,5],['U','D','L','R']] , 5:[[2,8,4],['U','D','L']] , 6:[[3,7],['U','R']] , 7:[[4,6,8],['U','L','R']] , 8:[[5,6],['U','L']] }
        self.children = children_by_empty[self.empty]
        
    def move(self, idx):
        tempboard = [i for i in self.board]
        tempboard[self.empty] = self.board[idx]
        tempboard[idx] = 0
        return tempboard

# read in inputs
search_type = sys.argv[1]
if search_type not in ['bfs', 'dfs', 'ast']: 
    sys.exit('Invalid search type, pick bfs dfs or ast')
    
init_state_1str = sys.argv[2]
init_state_strs = init_state_1str.split(',')
init_state = [int(tile) for tile in init_state_strs]
if len(init_state) != 9:
    sys.exit('Incorrect number of tiles, need 9 with 0 for empty, separated by a comma no space')
    
goal_state = [0,1,2,3,4,5,6,7,8]

start_state = state(init_state, '')

# start case = 0 
# add connections[id] = [parent, direction]
connections = {}
connections[0]=[0,'G']


# Breadth first
if search_type == 'bfs':
    frontier_queue = Queue() 
    frontier_queue.put(start_state)
    frontier_boards = []
    # add visited list
    visited = []
    counter = 1
    parentID = -1
    while not frontier_queue.empty():
        current_state = frontier_queue.get()
        parentID +=1
        if current_state.board  == goal_state: 
            finalID = parentID
            break
        else: visited.append(current_state.board)
        for idx in range(len(current_state.children[0])):
            child = current_state.children[0][idx]
            path = current_state.children[1][idx]
            new_board = current_state.move(child)
            if new_board not in visited and (new_board not in frontier_boards):
                new_path = current_state.path + path 
                new_state = state(new_board, new_path)
                frontier_queue.put(new_state)
                frontier_boards.append(new_board)
                connections[counter] = [parentID, path]
            counter +=1   


if search_type == 'dfs':
    # can just use list as stack
    frontier_stack = []
    frontier_stack.append(start_state)
    frontier_boards  = []

    # add visited list
    visited = []
    counter = 1
    while not frontier_stack == []:
        current_state = frontier_stack.pop()
        if current_state.board  == goal_state: 
            finalID = counter-1
            break
        else: visited.append(current_state.board)
        idxs = range(len(current_state.children[0]))
        # reverse the index order so will pull children by RLDU instead of UDLR
        idxs = idxs[::-1]
        parentID = counter-1
        for idx in idxs:
            child = current_state.children[0][idx]
            path = current_state.children[1][idx]
            #new_path = current_state.path + path 
            new_board = current_state.move(child)
            new_state = state(new_board,'')
            if (new_board not in visited) and (new_board not in frontier_boards):
                # need to check board if in frontier already
                frontier_stack.append(new_state)
                frontier_boards.append(new_board)
                connections[counter] = [parentID, path]
            counter +=1

# Clean up class, remove path stuff

print finalID
print connections
    