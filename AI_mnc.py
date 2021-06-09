class State:
    def __init__(self, left_c, left_m, pos_boat,right_c, right_m):
        self.left_c = left_c
        self.left_m = left_m
        self.pos_boat = pos_boat
        self.right_c = right_c
        self.right_m = right_m
        self.parent = None
        self.depth = 0
        self.g_value = 2048

    def is_goal(self):
        if self.left_m == 0 and self.left_c == 0 and self.pos_boat == 1:
            return True
        else:
            return False

    def is_valid(self):
        if self.left_m >= 0 and self.right_m >= 0 \
            and self.left_c >= 0 and self.right_c >= 0 \
            and (self.left_m == 0 or self.left_m >= self.left_c) \
            and (self.right_m == 0 or self.right_m >= self.right_c):
            return True
        
        else:
            return False

    def __eq__(self, other):		
        return self.left_c == other.left_c and self.left_m == other.left_m \
            and self.pos_boat == other.pos_boat and self.right_c == other.right_c \
            and self.right_m == other.right_m

    def __hash__(self):
        return hash((self.left_c, self.left_c, self.pos_boat, self.right_c, self.right_m))

def successors(curr_state):
  children = []
  if curr_state.pos_boat == 0: #boat is on left
    ## Two missionaries cross left to right.
    t_state = State(curr_state.left_c, curr_state.left_m - 2, not curr_state.pos_boat,
                                  curr_state.right_c, curr_state.right_m + 2)
    if t_state.is_valid():
      t_state.parent = curr_state
      children.append(t_state)
 
    ## Two cannibals cross left to right.
    t_state = State(curr_state.left_c - 2, curr_state.left_m, not curr_state.pos_boat,
                                  curr_state.right_c + 2, curr_state.right_m)
    if t_state.is_valid():
      t_state.parent = curr_state
      children.append(t_state)
    
    ## One missionary and one cannibal cross left to right.
    t_state = State(curr_state.left_c - 1, curr_state.left_m - 1, not curr_state.pos_boat,
                                  curr_state.right_c + 1, curr_state.right_m + 1)
    if t_state.is_valid():
      t_state.parent = curr_state
      children.append(t_state)
    
    ## One missionary crosses left to right.
    t_state = State(curr_state.left_c, curr_state.left_m - 1, not curr_state.pos_boat,
                                  curr_state.right_c, curr_state.right_m + 1)
    if t_state.is_valid():
      t_state.parent = curr_state
      children.append(t_state)
    
    ## One cannibal crosses left to right.
    t_state = State(curr_state.left_c - 1, curr_state.left_m, not curr_state.pos_boat,
                                  curr_state.right_c + 1, curr_state.right_m)
    if t_state.is_valid():
      t_state.parent = curr_state
      children.append(t_state)
    
  else:
    ## Two missionaries cross right to left.
    t_state = State(curr_state.left_c, curr_state.left_m + 2, not curr_state.pos_boat,
                                  curr_state.right_c, curr_state.right_m - 2)
    if t_state.is_valid():
      t_state.parent = curr_state
      children.append(t_state)
    
    ## Two cannibals cross right to left.
    t_state = State(curr_state.left_c + 2, curr_state.left_m, not curr_state.pos_boat,
                                  curr_state.right_c - 2, curr_state.right_m)
    if t_state.is_valid():
      t_state.parent = curr_state
      children.append(t_state)
    
    ## One missionary and one cannibal cross right to left.
    t_state = State(curr_state.left_c + 1, curr_state.left_m + 1, not curr_state.pos_boat,
                                  curr_state.right_c - 1, curr_state.right_m - 1)
    if t_state.is_valid():
      t_state.parent = curr_state
      children.append(t_state)
    
    ## One missionary crosses right to left.
    t_state = State(curr_state.left_c, curr_state.left_m + 1, not curr_state.pos_boat,
                                  curr_state.right_c, curr_state.right_m - 1)
    if t_state.is_valid():
      t_state.parent = curr_state
      children.append(t_state)
    
    ## One cannibal crosses right to left.
    t_state = State(curr_state.left_c + 1, curr_state.left_m, not curr_state.pos_boat,
                                  curr_state.right_c - 1, curr_state.right_m)
    if t_state.is_valid():
      t_state.parent = curr_state
      children.append(t_state)
    
  return children

initial_state = State(3,3,0,0,0) 

no_of_gen_nodes = 0
no_of_exp_nodes = 0

cost_missionary = 10
cost_cannibal = 20

def arc_cost(parent,child):
  if parent.pos_boat == 0: #boat is at left bank
    return (child.right_m - parent.right_m)*(cost_missionary) + (child.right_c - parent.right_c)*(cost_cannibal)
  else: #boat is at right bank
    return (child.left_m - parent.left_m)*(cost_missionary) + (child.left_c - parent.left_c)*(cost_cannibal)


def bfs():
    global no_of_gen_nodes
    global no_of_exp_nodes

    no_of_exp_nodes = 0
    no_of_gen_nodes = 0

    if initial_state.is_goal():
        return initial_state
    open = list()
    closed = set()

    open.append(initial_state)
    no_of_gen_nodes += 1

    while(len(open)):
        curr_state = open.pop(0)
        if curr_state.is_goal():
            return curr_state
        
        closed.add(curr_state)
        no_of_exp_nodes += 1

        children = successors(curr_state)
        for child in children:
            if(child not in open) and (child not in closed):
                open.append(child)
                no_of_gen_nodes += 1

    print("Goal state not found.")
    return None

def dfs():
  global no_of_gen_nodes
  global no_of_exp_nodes
  no_of_gen_nodes = 0
  no_of_exp_nodes = 0
  
  if initial_state.is_goal():
    return initial_state
  open = list()
  closed = set()

  open.append(initial_state)
  no_of_gen_nodes += 1

  while(len(open)):
    # print(len(open))
    curr_state = open.pop() # pops from end
    if curr_state.is_goal():
      return curr_state

    closed.add(curr_state)
    no_of_exp_nodes +=1

    children = successors(curr_state)
    for child in children:
      if (child not in open) and (child not in closed):
        open.append(child)
        no_of_gen_nodes += 1

  print('Goal state not found.')
  return None

import itertools

def iter_deep():
  global no_of_gen_nodes
  global no_of_exp_nodes
  no_of_gen_nodes = 0
  no_of_exp_nodes = 0

  max_depth = 0

  for k in itertools.count(start=0):
    if initial_state.is_goal():
      return initial_state
    open = list()
    closed = set()

    open.append(initial_state)
    no_of_gen_nodes += 1

    while(len(open)):
      curr_state = open.pop()
      if curr_state.is_goal():
        return curr_state
        
      if max_depth < curr_state.depth:
        max_depth = curr_state.depth

      closed.add(curr_state)
      no_of_exp_nodes +=1

      if curr_state.depth >= k:
        continue
      else:
        children = successors(curr_state)
        for child in children:
          if (child not in open) and (child not in closed):
            child.depth = curr_state.depth + 1 # depth of child of a node would be +1 that of the node
            open.append(child)
            no_of_gen_nodes += 1

    if max_depth < k: # to exit if maximum possible depth is reached ... so that the program doesn't run indefinitely
      print('Goal state not found')
      break
      
  return None

def min_index(a_list):
  min = a_list[0].g_value
  min_i = 0
  for i in range(len(a_list)):
    if a_list[i].g_value < min:
      min = a_list[i].g_value
      min_i = i
  return min_i

def ucs():
  global no_of_gen_nodes
  global no_of_exp_nodes
  no_of_gen_nodes = 0
  no_of_exp_nodes = 0

  if initial_state.is_goal():
      return initial_state
  open = list()
  closed = list()

  initial_state.g_value = 0
  
  open.append(initial_state)
  no_of_gen_nodes += 1

  while(len(open)):
    curr_state = open.pop(min_index(open))
    if curr_state.is_goal():
        return curr_state
    closed.append(curr_state)
    no_of_exp_nodes +=1

    children = successors(curr_state) 
    for child in children:
      if (child not in open) and (child not in closed):
        child.g_value = child.parent.g_value + arc_cost(curr_state, child)
        open.append(child)
        no_of_gen_nodes +=1
        
      elif (child in open) or (child in closed):
        prev_g = child.g_value
        child.g_value = min(child.g_value, child.parent.g_value + arc_cost(curr_state, child))
        if (child.g_value < prev_g) and (child in closed):
          open.append(child)
          no_of_gen_nodes +=1
          closed.remove(child)
   
def print_solution(solution):
    path = []
    path_cost = 0
    
    if solution is None:
      print("No solution found")
      return

    path.append(solution)
    parent = solution.parent
    path_cost += arc_cost(solution.parent, solution)
    while parent:
      path.append(parent)
      if parent.parent:
        path_cost += arc_cost(parent.parent, parent)
      parent = parent.parent
    
  
    for t in range(len(path)):
      state = path[len(path) - t - 1]
      print("  ",state.left_c,"\t    \t",state.left_m,"\t | \t","right" if state.pos_boat else "left","\t  | \t",state.right_c,"\t   \t",state.right_m)
    
    print("No. of nodes generated : ", no_of_gen_nodes)
    print("No. of nodes expanded : ", no_of_exp_nodes)
    print("path cost : ", path_cost)

def main():
  print("\nBFS")
  solution = bfs()                                   
  print ("cannibal_l","---","missionary_l","---","pos_boat","---","cannibal_r","---","missionary_r")
  print()
  print_solution(solution)
 
  print("\nDFS")
  solution = dfs()
  print ("cannibal_l","---","missionary_l","---","pos_boat","---","cannibal_r","---","missionary_r")
  print()
  print_solution(solution)
 
  print("\nIDS")
  solution = iter_deep()
  print ("cannibal_l","---","missionary_l","---","pos_boat","---","cannibal_r","---","missionary_r")
  print()
  print_solution(solution)
 
  print("\nUCS")
  solution = ucs()
  print ("cannibal_l","---","missionary_l","---","pos_boat","---","cannibal_r","---","missionary_r")
  print_solution(solution)

if __name__ == "__main__":
    main()