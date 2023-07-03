from mesa import Agent
from src.SurvivorAgent import SurvivorAgent


class ExitAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.escaped = False
        self.win = False
    def step(self):
        self.escape()

    def escape(self):
        survivors = self.get_survivor_agent(self.pos)
        for i in survivors:
            print("Vitória")
            self.win = True
            self.model.grid.remove_agent(i)
            self.model.schedule.remove(i)
            self.model.survivors.remove(i)
        if len(survivors) == len(self.model.survivors) + 1:
            self.escaped = True

    def get_survivor_agent(self, pos):
        try:
            this_cell = self.model.grid.get_cell_list_contents([pos])
            target = []
            for obj in this_cell:
                if obj in self.model.survivors:
                    target.append(obj)
            return target
        except:
            return []
