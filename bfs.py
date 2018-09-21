from collections import deque


class Node:
    def __init__(self, state, parent):
        self.state = state
        self.parent = parent

class WolfSheepCabbageRiddle:

    def get_other_side(self, side):
        other_sides = {'left': 'right', 'right': 'left'}
        return other_sides[side]

    def get_start_position(self):
        return {'left': {'pastor', 'lobo', 'ovelha', 'couve'}, 'right': set(), 'barco': 'left'}

    def get_characters(self):
        characters = ('pastor', 'lobo', 'ovelha', 'couve')

    def is_position_valid(self, position):
        sides = ('left', 'right')
        for side in sides:
            l = position[side]
            if 'lobo' in l and 'ovelha' in l and 'pastor' not in l:
                return False
            if 'ovelha' in l and 'couve' in l and 'pastor' not in l:
                return False
        return True

    def list_possible_next_positions(self, position):
        pair_alread_reached = []
        destination = self.get_other_side(position['barco'])
        if 'pastor' in position[position['barco']]:
            new_position = self.move(position, {'pastor'})
            if self.is_position_valid(new_position):
                yield new_position
            for char in position[position['barco']]:
                if 'pastor' != char:
                    new_position = self.move(position, {'pastor', char})
                    if self.is_position_valid(new_position):
                        yield new_position

    def is_final_position(self, position):
        return position == {'right': {'pastor', 'lobo', 'ovelha', 'couve'}, 'left': set(), 'barco': 'right'}

    def move(self, position, chars):
        destination = self.get_other_side(position['barco'])
        origin = position['barco']
        return {
            'barco': destination,
            origin: {x for x in position[origin] if x not in chars},
            destination: position[destination] | chars}

class BFS:
    @staticmethod
    def breadth_first_search(root, next_states_f, is_final_state_f):
        queue = deque([Node(root, None)])
        visited_states = []

        while queue:
            vertex = queue.popleft()
            if is_final_state_f(vertex.state):
                return vertex
            next_states = next_states_f(vertex.state)
            for state in next_states:
                if state in visited_states:
                    continue
                if state not in queue:
                    queue.append(Node(state, vertex))
            visited_states.append(vertex.state)

    @staticmethod
    def print_path(leaf_node):
        path = []
        node = leaf_node
        while node:
            path.insert(0, node.state)
            node = node.parent
        for n in path:
            print(n)

wsc_riddle = WolfSheepCabbageRiddle()
solution = BFS.breadth_first_search(
    wsc_riddle.get_start_position(),
    wsc_riddle.list_possible_next_positions,
    wsc_riddle.is_final_position)
BFS.print_path(solution)
