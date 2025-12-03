import math
import random
import time


class Agent:
    ident = 0

    def __init__(self):
        self.id = Agent.ident
        Agent.ident += 1

    def get_chosen_action(self, state, max_depth):
        pass


class RandomAgent(Agent):
    def get_chosen_action(self, state, max_depth):
        time.sleep(0.5)
        actions = state.get_legal_actions()
        return actions[random.randint(0, len(actions) - 1)]


class GreedyAgent(Agent):
    def get_chosen_action(self, state, max_depth):
        time.sleep(0.5)
        actions = state.get_legal_actions()
        best_score, best_action = None, None
        for action in actions:
            # Simuliraj šta bi se desilo ako izvršim ovu akciju
            new_state = state.generate_successor_state(action)
            # Računa rezultat (broj osvojenih polja) za trenutnog igrača u tom novom stanju
            # state.get_on_move_chr() - vraća identifikator igrača koji je trenutno na potezu
            score = new_state.get_score(state.get_on_move_chr())
            # Ako je ovo prva akcija ili bolja od dosadašnje najbolje
            if (best_score is None and best_action is None) or score > best_score:
                best_action = action
                best_score = score
        return best_action

class MinimaxAgent(Agent):
    def get_chosen_action(self, state, max_depth):
        # time.sleep(0.5)
        def minimax(state, max_depth, enemy, playerid):
            actions = state.get_legal_actions()
            if max_depth == 0 or state.is_goal_state():
                return playerstate(state, playerid)
            if enemy:  # ako je TRUE onda je protivnik(MIN), ako je FALSE onda smo to mi(MAX)
                min_score = math.inf  # minimum nam treba
                for action in actions:
                    new_state = state.generate_successor_state(action)
                    curr_score = minimax(new_state, max_depth - 1, False, playerid)
                    min_score = min(min_score, curr_score)
                return min_score
            else:
                max_score = -math.inf  # maximum nam treba za nas
                for action in actions:
                    new_state = state.generate_successor_state(action)
                    curr_score = minimax(new_state, max_depth - 1, True, playerid)
                    max_score = max(max_score, curr_score)
                return max_score

        def playerstate(state, playerid):
            my_score = state.get_score(playerid)
            if playerid == 'A':
                enemy = 'B'
            else:
                enemy = 'A'
            enemy_score = state.get_score(enemy)
            return my_score - enemy_score

        actions = state.get_legal_actions()
        playerid = state.get_on_move_chr()
        best_score = -math.inf #MIN
        best_action = None

        for action in actions:
            new_state = state.generate_successor_state(action)
            score = minimax(new_state, max_depth - 1,True, playerid)
            if score > best_score:
                best_action = action
                best_score = score
        return best_action

class MinimaxABAgent(Agent):
    def get_chosen_action(self, state, max_depth):
        # time.sleep(0.5)
        def minimax(state, max_depth, alpha, beta, enemy, playerid):
            actions = state.get_legal_actions()
            if max_depth == 0 or state.is_goal_state():
                return playerstate(state, playerid)
            if enemy:  # ako je TRUE onda je protivnik(MIN), ako je FALSE onda smo to mi(MAX)
                min_score = math.inf  # minimum nam treba
                for action in actions:
                    new_state = state.generate_successor_state(action)
                    curr_score = minimax(new_state, max_depth - 1, alpha, beta,False, playerid)
                    min_score = min(min_score, curr_score)
                    beta = min(beta, curr_score)
                    if alpha >= beta:
                        break
                return min_score
            else:
                filtered_actions = [action for action in actions if not self.is_left_movement(action)]
                max_score = -math.inf  # maximum nam treba za nas
                for action in actions:
                    new_state = state.generate_successor_state(action)
                    curr_score = minimax(new_state, max_depth - 1, alpha, beta,True, playerid)
                    max_score = max(max_score, curr_score)
                    alpha = max(alpha, curr_score)
                    if alpha >= beta:
                        break
                return max_score

        def playerstate(state, playerid):
            my_score = state.get_score(playerid)
            if playerid == 'A':
                enemy = 'B'
            else:
                enemy = 'A'
            enemy_score = state.get_score(enemy)
            return my_score - enemy_score

        actions = state.get_legal_actions()
        playerid = state.get_on_move_chr()
        best_score = -math.inf  # MIN
        best_action = None
        alpha = -math.inf
        beta = math.inf

        for action in actions:
            new_state = state.generate_successor_state(action)
            score = minimax(new_state, max_depth - 1, alpha, beta, True, playerid)
            if score > best_score:
                best_action = action
                best_score = score

            alpha = max(alpha, best_score)
        return best_action

class MaxNAgent(Agent):
    def get_chosen_action(self, state, max_depth):
        # time.sleep(0.5)
        def minimax(state, max_depth):
            actions = state.get_legal_actions()
            curr_player = state.get_on_move_chr()
            if max_depth == 0 or len(actions) == 0:
                return state

            max_score = -math.inf  # maximum nam treba za nas
            max_state = state
            for action in actions:
                new_state = state.generate_successor_state(action)
                new_state = minimax(new_state, max_depth - 1)
                curr_score = playerstate(new_state, curr_player)
                if curr_score > max_score:
                    max_score = curr_score
                    max_state = new_state
            return max_state

        def playerstate(state, playerid):
            return state.get_score(playerid)

        actions = state.get_legal_actions()
        best_score = -math.inf #MIN
        best_action = state
        curr_player = state.get_on_move_chr()

        for action in actions:
            new_state = state.generate_successor_state(action)
            new_state = minimax(new_state, max_depth - 1)
            curr_score = playerstate(new_state, curr_player)
            if curr_score > best_score:
                best_score = curr_score
                best_action = action
        return best_action




