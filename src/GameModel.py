import uuid
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa import Model
from src.SurvivorAgent import SurvivorAgent
from src.GeneratorAgent import GeneratorAgent
from src.ExitAgent import ExitAgent
from src.MurdererAgent import MurdererAgent
import random


class GameModel(Model):
    def __init__(self, num_survivors, num_generators, width, height):
        self.num_generators = num_generators
        self.num_survivors = num_survivors
        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)
        self.game_over = False
        self.steps = 0
        self.murderer = None
        self.survivors = []
        self.exit = None
        self.generators = []
        self.exit_agent_created = False

        self.murderer = MurdererAgent(uuid.uuid1(), self)
        self.grid.place_agent(self.murderer, self.grid.find_empty())
        self.schedule.add(self.murderer)
        
        self.exit = ExitAgent(uuid.uuid1(), self)
        
        for i in range(self.num_survivors):
            id = uuid.uuid1()
            survivor = SurvivorAgent(id, self)
            self.survivors.append(survivor)
            self.schedule.add(survivor)
            if self.grid.exists_empty_cells():
                self.grid.place_agent(survivor, self.grid.find_empty())

        for i in range(self.num_generators):
            id = uuid.uuid1()
            generator = GeneratorAgent(id, self)
            self.generators.append(generator)
            self.schedule.add(generator)
            if self.grid.exists_empty_cells():
                self.grid.place_agent(generator, self.grid.find_empty())

    def add_exit_agent(self):
        x, y = self.select_random_edge()
        self.grid.place_agent(self.exit, (x, y))
        self.schedule.add(self.exit)

    def step(self):
        if not self.game_over:
            self.schedule.step()

        print("GAME OVER: ", self.game_over)

        if len(self.survivors) == 0 or self.exit.escaped:
            self.game_over = True
        if len(self.survivors) == 0 and not self.exit.escaped and not self.exit.win:
            print("Derrota")
        
        inactive_generators = [generator for generator in self.generators if not generator.activated]
        if len(inactive_generators) == 0 and not self.exit_agent_created:
            self.add_exit_agent()
            self.exit_agent_created = True

    def select_random_edge(self):
        edges = [
            (0, random.randint(0, self.grid.height - 1)),  # Esquerda
            (self.grid.width - 1, random.randint(0, self.grid.height - 1)),  # Direita
            (random.randint(0, self.grid.width - 1), 0),  # Superior
            (random.randint(0, self.grid.width - 1), self.grid.height - 1)  # Inferior
        ]
        return random.choice(edges)
