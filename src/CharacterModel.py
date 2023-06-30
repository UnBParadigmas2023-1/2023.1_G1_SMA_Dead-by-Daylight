import uuid
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa import Model
from src.CharacterAgent import CharacterAgent
from src.GeneratorAgent import GeneratorAgent
from src.ExitAgent import ExitAgent
import random


class CharacterModel(Model):
    def __init__(self, N, width, height):
        self.num_agents = N
        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)
        self.game_over = False
        self.steps = 0
        self.init_agent(CharacterAgent, self.num_agents)
        self.init_agent(GeneratorAgent, self.num_agents)
        self.exit_agent_created = False

    def add_exit_agent(self):
        exit_agent = ExitAgent(uuid.uuid1(), self)
        x, y = self.select_random_edge()
        self.grid.place_agent(exit_agent, (x, y))
        self.schedule.add(exit_agent)

    def init_agent(self, Agent, num_agents):
        for i in range(num_agents):
            id = uuid.uuid1()
            agent = Agent(id, self)
            self.schedule.add(agent)
            if self.grid.exists_empty_cells():
                self.grid.place_agent(agent, self.grid.find_empty())

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
