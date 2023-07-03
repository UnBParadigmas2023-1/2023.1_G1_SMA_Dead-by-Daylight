from mesa import Agent


class GeneratorAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.activated = False

    def step(self):
        self.activate()

    def activate(self):
        survivors = self.get_survivor_agent(self.pos)
        if len(survivors) > 0:
            self.activated = True

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
