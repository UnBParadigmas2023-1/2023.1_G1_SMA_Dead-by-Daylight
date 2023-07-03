from mesa import Agent


class MurdererAgent(Agent):
    def __init__(self, unique_id, model, view_range=10,walk_speed=2, moore=False):
        super().__init__(unique_id, model)
        self.view_range = view_range  # Alcance da visão do personagem
        self.walk_speed = walk_speed  # Quadrados andados por passo('velocidade')
        self.moore = moore  # Personagem só anda na vertical e horizontal

    def step(self):
        if self.model.game_over:
            self.view_range = float('inf')  # Atribui o valor infinito ao view_range quando game_over for True
        self.walk()

    def walk(self):

        possible_walk_pos = self.model.grid.get_neighborhood(
            self.pos, moore=self.moore, include_center=True, radius=self.view_range)
        new_position = self.get_new_position(
            possible_walk_pos, self.pos)
        self.model.grid.move_agent(self, new_position)
        # print(format(self.role), "> Andei pro gerador")

    def get_new_position(self, possible_walk_pos, current_pos):
        next_pos = None
        current_best_pos = None
        minimum_distance = 10**6
        step_x = 0
        step_y = 0
        # Para cada posição possível de andar, ele procura um sobrevivente
        for walk_pos in possible_walk_pos:

            survivor = self.check_pos_for_survivor(walk_pos)
            # Se tiver um gerador ao alcance
            if len(survivor) > 0:
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
    
    def check_pos_for_survivor(self, pos):
        try:
            # Retorna lista de objetos na célula diferentes de Agent
            this_cell = self.model.grid.get_cell_list_contents([pos])
            target = []
            # print("AQUI POSIÇAO ATUAL ", this_cell)
            for obj in this_cell:
                if obj in self.model.survivors:
                    target.append(obj)
                # print("TESTE POSICAO: ", target)
            return target
        except:
            # Retorna nada
            print("ERRO AO PROCURAR POSICAO")
            return []