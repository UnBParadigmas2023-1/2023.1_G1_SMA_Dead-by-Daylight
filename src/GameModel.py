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
    def __init__(self, N, width, height):
        self.num_agents = N
        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)
        self.game_over = False
        self.steps = 0
        self.murderer = None
        self.survivors = []
        self.exit = None
        self.generators = []
        # self.init_agent(SurvivorAgent, self.num_agents)
        # self.init_agent(GeneratorAgent, self.num_agents)
        # self.init_agent(MurdererAgent, 1)
        self.exit_agent_created = False

        self.murderer = MurdererAgent(uuid.uuid1(), self)
        self.grid.place_agent(self.murderer, self.grid.find_empty())
        self.schedule.add(self.murderer)
        
        
        for i in range(self.num_agents):
            id = uuid.uuid1()
            survivor = SurvivorAgent(id, self)
            self.survivors.append(survivor)
            self.schedule.add(survivor)
            if self.grid.exists_empty_cells():
                self.grid.place_agent(survivor, self.grid.find_empty())

        for i in range(4):
            id = uuid.uuid1()
            generator = GeneratorAgent(id, self)
            self.generators.append(generator)
            self.schedule.add(generator)
            if self.grid.exists_empty_cells():
                self.grid.place_agent(generator, self.grid.find_empty())

    def add_exit_agent(self):
        self.exit = ExitAgent(uuid.uuid1(), self)
        x, y = self.select_random_edge()
        self.grid.place_agent(self.exit, (x, y))
        self.schedule.add(self.exit)

    # def init_agent(self, Agent, num_agents):
    #     for i in range(num_agents):
    #         id = uuid.uuid1()
    #         agent = Agent(id, self)
    #         self.schedule.add(agent)
    #         if self.grid.exists_empty_cells():
    #             self.grid.place_agent(agent, self.grid.find_empty())

    def step(self):
        self.schedule.step()

        if not any(isinstance(agent, GeneratorAgent) for agent in self.schedule.agents):
            self.game_over = True

        if self.game_over and not any(isinstance(agent, GeneratorAgent) for agent in self.schedule.agents) and not self.exit_agent_created:
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
