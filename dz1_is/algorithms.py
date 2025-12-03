import random
import queue
import heapq
import config
import math
from state import State


class Algorithm:
    def get_path(self, state):
        pass


class ExampleAlgorithm(Algorithm):
    def get_path(self, state):
        path = []
        while not state.is_goal_state():
            possible_actions = state.get_legal_actions()
            action = possible_actions[random.randint(0, len(possible_actions) - 1)]
            path.append(action)
            state = state.generate_successor_state(action)
        return path

class Blue(Algorithm):
    def get_path(self, state):
        stack = []
        visited = set()

        stack.append((state, []))

        while stack:
            curr_state, path = stack.pop()

            if curr_state.is_goal_state():
                return path

            if curr_state.get_state('S') in visited:
                continue

            visited.add(curr_state.get_state('S'))
            possible_actions = curr_state.get_legal_actions()
            for action in reversed(possible_actions):
                stack.append((curr_state.generate_successor_state(action), path + [action]))

        return []

class Red(Algorithm):
    def get_path(self, state):
        q = queue.Queue()
        visited = set()

        q.put((state, []))

        while q:
            curr_state, path = q.get()

            if curr_state.is_goal_state():
                return path

            if curr_state.get_state('S') in visited:
                continue

            visited.add(curr_state.get_state('S'))
            possible_actions = curr_state.get_legal_actions()
            for action in possible_actions:
                q.put((curr_state.generate_successor_state(action), path + [action]))

        return []

class Black(Algorithm):
    def get_path(self, state):
        pq = []
        visited = set()

        heapq.heappush(pq, (0, state, []))

        while pq:

            cost, curr_state, path = heapq.heappop(pq)

            if curr_state.is_goal_state():
                return path

            if curr_state.get_state('S') in visited:
                continue

            visited.add(curr_state.get_state('S'))
            possible_actions = curr_state.get_legal_actions()
            for action in possible_actions:
                if curr_state.generate_successor_state(action).get_state('S') not in visited:
                    heapq.heappush(pq, (cost + State.get_action_cost(action), curr_state.generate_successor_state(action), path + [action]))

        return []

class White(Algorithm):

    def heuristic(self, state1):

        brodovi = state1.get_state("S")
        ciljevi = state1.get_state("G")

        suma = 0

        while brodovi:
            s = brodovi & -brodovi
            boat = (int(int(math.log2(s)) / config.N), int(int(math.log2(s)) % config.N))
            cilj = ciljevi
            razdaljina = []
            while cilj:
                c = cilj & -cilj
                finish = (int(int(math.log2(c)) / config.N), int(int(math.log2(c)) % config.N))
                razdaljina.append(abs(finish[0] - boat[0]) + abs(finish[1] - boat[1]))
                cilj &= cilj - 1
            suma += min(razdaljina)
            brodovi &= brodovi - 1

        return suma

    def get_path(self, state):
        pq = []
        visited = set()

        heapq.heappush(pq, (0, state, [], 0))

        while pq:

            cost, curr_state, path, heur = heapq.heappop(pq)
            cost -= heur

            if curr_state.is_goal_state():
                return path

            if curr_state.get_state('S') in visited:
                continue

            visited.add(curr_state.get_state('S'))
            possible_actions = curr_state.get_legal_actions()
            for action in possible_actions:
                heuri = self.heuristic(curr_state.generate_successor_state(action))
                heapq.heappush(pq, (cost + State.get_action_cost(action) + heuri, curr_state.generate_successor_state(action), path + [action], heuri))

        return []