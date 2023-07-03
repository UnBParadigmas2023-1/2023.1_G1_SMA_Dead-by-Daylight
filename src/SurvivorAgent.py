from mesa import Agent

class SurvivorAgent(Agent):

    def __init__(self, unique_id, model, role="Survivor", moore=True, view_range=10, walk_speed=1):
        super().__init__(unique_id, model)
        self.role = role  # Papel do personagem: Survivor or Murderer
        self.moore = moore  # Personagem só anda na vertical e horizontal
        self.view_range = view_range  # Alcance da visão do personagem
        self.walk_speed = walk_speed  # Quadrados andados por passo('velocidade')
        self.alive = True

    def step(self):
        if self.model.exit_agent_created:
            self.view_range = float('inf')  # Atribui o valor infinito ao view_range quando game_over for True
        self.die()
        if self.alive is False:
            self.model.grid.remove_agent(self)
            self.model.schedule.remove(self)
            self.model.survivors.remove(self)
        else:
            self.walk()

    def die(self):
        murderer = self.get_murderer_agent(self.pos)
        if len(murderer) > 0:
            self.alive = False

    def walk(self):
        possible_walk_pos = self.model.grid.get_neighborhood(
            self.pos, moore=self.moore, include_center=True, radius=self.view_range)
        new_position = self.get_new_position(
            possible_walk_pos, self.pos)
        self.model.grid.move_agent(self, new_position)

    def get_new_position(self, possible_walk_pos, current_pos):
        next_pos = None
        current_best_pos = None
        minimum_distance = 10**6
        step_x = 0
        step_y = 0
        # Para cada posição possível de andar, ele procura o gerador
        for walk_pos in possible_walk_pos:
            generator = self.check_pos_for_generator(walk_pos)
            # Se tiver um gerador ao alcance
            if len(generator) > 0:
                # Calcula distância entre o gerador e a posição atual
                current_distance = (
                    current_pos[0] - walk_pos[0])**2 + (current_pos[1] - walk_pos[1])**2
                # Ao fim do loop, seleciona o gerador mais perto
                if current_distance < minimum_distance:
                    minimum_distance = current_distance
                    current_best_pos = walk_pos

        # Se ele encontrou um gerador
        if current_best_pos != None:
            # Define o eixo (x) e direção que vai andar
            if current_pos[0] < current_best_pos[0]:
                step_x = 1
            elif current_pos[0] > current_best_pos[0]:
                step_x = -1
            # Define o eixo (y) e direção que vai andar
            if current_pos[1] < current_best_pos[1]:
                step_y = 1
            elif current_pos[1] > current_best_pos[1]:
                step_y = -1

            # Calcula a próxima posição
            next_pos = (current_pos[0] + min(self.walk_speed, abs(current_pos[0] - current_best_pos[0])) * step_x,
                        current_pos[1] + min(self.walk_speed, abs(current_pos[1] - current_best_pos[1])) * step_y)

            return next_pos

        next_pos = self.model.grid.get_neighborhood(
            self.pos, moore=self.moore, include_center=False, radius=self.walk_speed)
        return self.random.choice(next_pos)

    def check_pos_for_generator(self, pos):
        try:
            # Retorna lista de objetos na célula diferentes de Agent
            this_cell = self.model.grid.get_cell_list_contents([pos])

            # targets = [obj for obj in this_cell if not isinstance(obj, SurvivorAgent)]
            targets = []
            for obj in this_cell:
                if obj is self.model.exit or (obj in self.model.generators and obj.activated == False):
                    targets.append(obj)
            return targets
        except:
            # Retorna nada
            return []
    
    def get_murderer_agent(self, pos):
        try:
            this_cell = self.model.grid.get_cell_list_contents([pos])
            target = []
            for obj in this_cell:
                if obj is self.model.murderer:
                    target.append(obj)
            return target
        except:
            print("aqui")
            return []