from collections import deque

def get_other_side(side):
    other_sides = {'left': 'right', 'right': 'left'}
    return other_sides[side]

def get_start_position():
    return {'left': {'pastor', 'lobo', 'ovelha', 'couve'}, 'right': set(), 'barco': 'left'}

def get_characters():
    characters = ('pastor', 'lobo', 'ovelha', 'couve')

def is_position_valid(position):
    sides = ('left', 'right')
    for side in sides:
        l = position[side]
        if 'lobo' in l and 'ovelha' in l and 'pastor' not in l:
            return False
        if 'ovelha' in l and 'couve' in l and 'pastor' not in l:
            return False
    return True

def list_possible_next_positions(position):
    pair_alread_reached = []
    destination = get_other_side(position['barco'])
    if 'pastor' in position[position['barco']]:
        new_position = move(position, {'pastor'}) 
        if is_position_valid(new_position):
            yield new_position
        for char in position[position['barco']]:
            if 'pastor' != char:
                new_position = move(position, {'pastor', char})
                if is_position_valid(new_position):
                    yield new_position 

def move(position, chars):
    destination = get_other_side(position['barco'])
    origin = position['barco']
    return {
        'barco': destination,
        origin: {x for x in position[origin] if x not in chars},
        destination: position[destination] | chars}

def breadth_first_search():
    open_set = deque()
    visited_nodes = []

    root = get_start_position()
    open_set.append(root)

    while len(open_set) > 0:
        subtree_root = open_set.pop()
        print(subtree_root)
        for child in list_possible_next_positions(subtree_root):
            if child in visited_nodes:
                continue
            if child not in open_set:
                open_set.append(child)
        visited_nodes.append(subtree_root)

breadth_first_search()
