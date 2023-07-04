# Dead by Daylight

**Disciplina**: FGA0210 - PARADIGMAS DE PROGRAMAÇÃO - T03 <br>
**Nro do Grupo**: G1<br>
**Paradigma**: SMA<br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 17/0140571  |  Douglas Farias de Castro      |
| 20/0038141  |  Gustavo Duarte Moreira        |
| 17/0013987  |  João Victor de Oliveira Matos |
| 18/0042378  |  Kathlyn Lara Murussi          |
| 18/0022962  |  Luís Guilherme Gaboardi Lins  |
| 18/0028260  |  Thiago Aparecido Lopes Santos |
| 19/0055294  |  Thiago Siqueira Gomes         |
| 19/0038969  |  Victor Hugo Carvalho Silva    |
| 20/0028677  |  Vitor Manoel Aquino de Brito  |

## Sobre 
"Dead by Daylight" é um jogo multiplayer de terror assimétrico em que os jogadores são divididos em sobreviventes e assassino. Os sobreviventes devem colaborar para consertar geradores e escapar do mapa, enquanto o assassino busca caçar e eliminar os sobreviventes. 

A simulação do jogo "Dead by Daylight" é realizada utilizando a biblioteca Mesa. Nessa abordagem, os elementos do jogo, como os sobreviventes, o assassino e outros agentes, são modelados e interagem em um ambiente simulado. Isso permite explorar estratégias, analisar cenários e estudar o impacto de diferentes decisões e eventos no desenrolar do jogo.

## Screenshots
![Captura de tela de 2023-07-03 19-47-21](https://github.com/UnBParadigmas2023-1/2023.1_G1_SMA_Dead-by-Daylight/assets/54643372/d40deb17-6482-4741-92af-0108637bddb6)

![image](https://github.com/UnBParadigmas2023-1/2023.1_G1_SMA_Dead-by-Daylight/assets/54643372/ff75f9c4-5aff-434f-b26a-1b972a678da8)

## Instalação 
**Linguagens**: Python<br>
**Tecnologias**: Mesa: Agent-based modeling in Python<br>

Siga as etapas abaixo para configurar e executar o projeto em seu ambiente local.

### 1. Crie um ambiente virtual usando o comando:

```
python3 -m venv env   
```

### 2. Ative o ambiente virtual digitando o seguinte comando:
```
source env/bin/activate
```

### 3. Instale as dependências do projeto usando o comando:

```
pip install -r requirements.txt
```

### 4. Após a instalação bem-sucedida das dependências, execute o servidor usando o comando:

```
mesa runserver
```
Certifique-se de estar no diretório correto onde o arquivo run.py   está localizado.

![dbd-instalacao](https://github.com/UnBParadigmas2023-1/2023.1_G1_SMA_Dead-by-Daylight/assets/69691521/599a4480-1f48-45fb-9970-4dd316027d72)

## Uso 
Executando o servidor, gerará uma página em seu navegador, onde:

Antes de iniciar uma simulação é possível alterar os números de sobreviventes e geradores, além da velocidade dos passos nos sliders mostrados abaixo:

![image](https://github.com/UnBParadigmas2023-1/2023.1_G1_SMA_Dead-by-Daylight/assets/54643372/b1b817d6-4b76-49c3-a813-da71f8801e03)

![image](https://github.com/UnBParadigmas2023-1/2023.1_G1_SMA_Dead-by-Daylight/assets/54643372/d92bfd9c-540b-4a69-8d8b-1ab61bafb704)

Para iniciar/pausar, rodar passo a passo ou resetar uma simulação aperte os seguintes botões respectivamente:

![image](https://github.com/UnBParadigmas2023-1/2023.1_G1_SMA_Dead-by-Daylight/assets/54643372/29d76b06-d357-4d82-90be-8f95c92eee32)

Por fim, para visualizar uma breve descrição do simulador, acesse pelo botão abaixo:

![image](https://github.com/UnBParadigmas2023-1/2023.1_G1_SMA_Dead-by-Daylight/assets/54643372/5e269bb1-8866-4206-8900-f4624c39c046)


## Vídeo
Adicione 1 ou mais vídeos com a execução do projeto.
Procure: 
(i) Introduzir o projeto;
(ii) Mostrar passo a passo o código, explicando-o, e deixando claro o que é de terceiros, e o que é contribuição real da equipe;
(iii) Apresentar particularidades do Paradigma, da Linguagem, e das Tecnologias, e
(iV) Apresentar lições aprendidas, contribuições, pendências, e ideias para trabalhos futuros.
OBS: TODOS DEVEM PARTICIPAR, CONFERINDO PONTOS DE VISTA.
TEMPO: +/- 15min

## Participações
|Nome do Membro | Contribuição | Significância da Contribuição para o Projeto (Excelente/Boa/Regular/Ruim/Nula) |
| -- | -- | -- |
|  Douglas Farias de Castro      | Inclusão de boas práticas recomendadas pelo framework Mesa e documentação da Instação e execução do projeto. | Regular |
|  Gustavo Duarte Moreira        | Criação do repositório, documentação do README.md; | Regular |
|  João Victor de Oliveira Matos | Criação do agente Murderer, implementação da logica de fim de jogo e melhorias nos outros agentes | Excelente |
|  Kathlyn Lara Murussi          | | |
|  Luís Guilherme Gaboardi Lins  | | |
|  Thiago Aparecido Lopes Santos | Participação na criação do agente assassino, adaptações na lógica dos outros agentes, participação nas lógicas de encerramento da partida | Excelente |
|  Thiago Siqueira Gomes         | Criação do agente Assassino e implementação de lógica de finalização de partidas junto com outros integrantes, criação de lógica para acender luzes dos geradores | Excelente |
|  Victor Hugo Carvalho Silva    | Criação da descrição e adição da logo de vitória dos sobreviventes | Boa |
|  Vitor Manoel Aquino de Brito  | Criação do Agente base junto com o Luís, servindo como referência para melhorias no projeto, inserção de sliders para dar dinamismo ao jogo permitindo que o jogador selecione o número de sobreviventes e geradores | Excelente |

## Outros 

(i) Lições Aprendidas;
- Aprendizado e uso da biblioteca Mesa para simular o jogo Dead by Daylight;
  
(ii) Percepções;
- A biblioteca Mesa permite a criação de modelos de simulação de forma simples e intuitiva;

(iii) Contribuições e Fragilidades, e
- O projeto apresenta algumas fragilidades que precisam ser consideradas: 

(iV) Trabalhos Futuros.
- Incluir a expansão do modelo para acrescentar elementos adicionais do jogo como: 
    - diferentes mapas;
    - itens;
    - habilidades dos agentes;
    - diferentes assassinos;
    - diferentes sobreviventes;
- Explorar diferentes estratégias de sobrevivência e de caça;
- Explorar diferentes cenários e eventos;

## Fontes
- Behaviour Interactive. (2021). Dead by Daylight [Video game]. Disponível em: https://deadbydaylight.com/;
- Mesa, Documentação oficial: Mesa. (s.d.). Documentação oficial do Mesa. Disponível em: https://mesa.readthedocs.io/. Accessado em 02 de julho de 2023.
- Mesa, Repositório no Github: https://github.com/projectmesa/mesa.  Accessado em 02 de julho de 2023.
