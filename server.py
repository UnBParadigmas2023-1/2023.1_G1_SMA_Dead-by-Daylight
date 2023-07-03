from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from src.GeneratorAgent import GeneratorAgent
from src.MurdererAgent import MurdererAgent
from src.SurvivorAgent import SurvivorAgent
from src.GameModel import GameModel
from src.ExitAgent import ExitAgent


def agent_portrayal(agent):
    portrayal = {"Filled": "true", "Layer": 0, "w": 1, "h": 1}
    if type(agent) is GeneratorAgent:
        if not agent.activated:
            portrayal['Shape'] = "assets/light_off.png"
    elif type(agent) is SurvivorAgent:
        if agent.alive:
            portrayal['Shape'] = "assets/v.png"
    elif type(agent) is MurdererAgent:
        portrayal['Shape'] = "assets/jason_mask.png"
    elif type(agent) is ExitAgent:
        portrayal['Shape'] = "assets/door.png"
    return portrayal


grid = CanvasGrid(agent_portrayal, 30, 30, 500, 500)
server = ModularServer(GameModel, [grid], "Dead by Daylight", {
                       "N": 5, "width": 30, "height": 30})
server.port = 8080
server.launch()
