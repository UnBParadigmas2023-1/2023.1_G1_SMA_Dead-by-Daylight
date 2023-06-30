from mesa import Agent
from src.CharacterAgent import CharacterAgent


class ExitAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.escaped = False

    def step(self):
        self.escape()
        if self.escaped:
            self.model.game_over = True

    def escape(self):
        survivors = self.get_survivor_agent(self.pos)
        num_character_agents = sum(isinstance(agent, CharacterAgent)
                                   for agent in self.model.schedule.agents)
        if len(survivors) > num_character_agents:
            self.escaped = True

    def get_survivor_agent(self, pos):
        try:
            this_cell = self.model.grid.get_cell_list_contents([pos])
            return [obj for obj in this_cell if isinstance(obj, CharacterAgent)]
        except:
            return []
