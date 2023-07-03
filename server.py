from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
import mesa
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
        else:
            portrayal['Shape'] = "assets/light_on.png"
    elif type(agent) is SurvivorAgent:
        if agent.alive:
            portrayal['Shape'] = "assets/blob.png"
    elif type(agent) is MurdererAgent:
        portrayal['Shape'] = "assets/devil.png"
    elif type(agent) is ExitAgent:
        portrayal['Shape'] = "assets/door.png"
    return portrayal


model_params = {
    # Slide
    "num_survivors": mesa.visualization.Slider(
        name="Número de Sobreviventes",
        min_value=0,
        max_value=10,
        step=1,
        value=5,
    ),
    "num_generators": mesa.visualization.Slider(
        name="Número de geradores",
        min_value=0,
        max_value=10,
        step=1,
        value=5,
    ),
    "width": 15,
    "height": 15,
}

grid = CanvasGrid(agent_portrayal, 20, 20, 500, 500)
server = ModularServer(GameModel, [grid], "Dead by Daylight", model_params)
server.port = 8080
server.launch()
