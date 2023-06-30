from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from src.GeneratorAgent import GeneratorAgent
from src.CharacterAgent import CharacterAgent
from src.CharacterModel import CharacterModel
from src.ExitAgent import ExitAgent


def agent_portrayal(agent):
    portrayal = {"Filled": "true", "Layer": 0, "w": 1, "h": 1}
    if type(agent) is GeneratorAgent:
        if not agent.activated:
            portrayal['Shape'] = "assets/food.png"
    elif type(agent) is CharacterAgent:
        portrayal['Shape'] = "assets/blob.png"
    elif type(agent) is ExitAgent:
        portrayal['Shape'] = "assets/blob_cannibal.png"
    return portrayal


grid = CanvasGrid(agent_portrayal, 30, 30, 500, 500)
server = ModularServer(CharacterModel, [grid], "Dead by Daylight", {
                       "N": 4, "width": 25, "height": 15})
server.port = 8080
server.launch()
