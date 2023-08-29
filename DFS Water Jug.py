from queue import Queue

initial_state = (0, 0)
goal_state = (1, 0)

max_a = 5
max_b = 3

def actions(state):
    a, b = state
    possible_actions = []
    possible_actions.append((max_a, b))
    possible_actions.append((a, max_b))
    possible_actions.append((0, b))
    possible_actions.append((a, 0))
    amount = min(a, max_b - b)
    possible_actions.append((a - amount, b + amount))
    amount = min(b, max_a - a)
    possible_actions.append((a + amount, b - amount))
    return possible_actions

def bfs(initial_state, goal_state):
    visited = set()
    q = Queue()
    q.put([initial_state])
    while not q.empty():
        path = q.get()
        state = path[-1]
        if state == goal_state:
            return path
        if state not in visited:
            visited.add(state)
            for action in actions(state):
                new_path = list(path)
                new_path.append(action)
                q.put(new_path)

path = bfs(initial_state, goal_state)

if path is not None:
    print("Solution found:", end = "")
    print(path)
    for i, state in enumerate(path):
        print(f"{i}: {state}")
else:
    print("No solution found.")