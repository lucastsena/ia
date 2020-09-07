from definitions import Agent
import numpy as np

class RandAgent(Agent):
    """
    This class implements an agent that explores the environmente randomly
    until it reaches the target
    """

    def __init__(self, env):
        """Connects to the next available port.

        Args:
            env: A reference to an environment.

        """

        # Make a connection to the environment using the superclass constructor
        Agent.__init__(self,env)
        
        # Get initial percepts
        self.percepts = env.initial_percepts()
        
        # Initializes the frontier with the initial postion 
        self.frontier = [[self.percepts['current_position']]]
        
        # Initializes list of visited nodes for multiple path prunning
        self.visited = []

    def act(self):
        """Implements the agent action
        """

        # Select a path from the frontier
        path = self.frontier.pop(0)
        print('fronteira')
        print(self.frontier)
        # Visit the last node in the path
        action = {'visit_position': path[-1], 'path': path} 
        # The agente sends a position and the full path to the environment, the environment can plot the path in the room 
        
        self.percepts = self.env.signal(action)

        # Add visited node 
        self.visited.append(path[-1])

        # From the list of viable neighbors given by the environment
        # Select a random neighbor that has not been visited yet
        
        viable_neighbors =  self.percepts['neighbors']

        # If the agent is not stuck
        if viable_neighbors:
            # Select random neighbor
            visit = viable_neighbors[np.random.randint(0,len(viable_neighbors))]
                    
            # Append neighbor to the path and add it to the frontier
            self.frontier = [path + [visit]] + self.frontier
                 
                    

        print ('caminho')

        print([path])    

    def run(self):
        """Keeps the agent acting until it finds the target
        """

        # Run agent
        while (self.percepts['current_position'] != self.percepts['target']).any() and self.frontier:
            self.act()
            print('posiçao atual') 
            print(self.percepts['current_position'])
            print('Vizinhos') 
            print(self.percepts['neighbors'])
            print('fronteira')
            print(self.frontier)
            print('visitado')
            print(self.visited)
            input('Press ENTER to get out of here')
        print('Posicao final')
        print(self.percepts['current_position'])

class TestAgent(Agent):
    """
    This class implements an agent that explores the environmente randomly
    until it reaches the target
    """

    def __init__(self, env):
        """Connects to the next available port.

        Args:
            env: A reference to an environment.

        """

        # Make a connection to the environment using the superclass constructor
        Agent.__init__(self,env)
        
        # Get initial percepts
        self.percepts = env.initial_percepts()
        
        # Initializes the frontier with the initial postion 
        self.frontier = [[self.percepts['current_position']]]
        
        # Initializes list of visited nodes for multiple path prunning
        self.visited = []

    def act(self):
        """Implements the agent action
        """

        # Select a path from the frontier
        path = self.frontier.pop(0)
        print('fronteira')
        print(self.frontier)
        # Visit the last node in the path
        action = {'visit_position': path[-1], 'path': path} 
        # The agente sends a position and the full path to the environment, the environment can plot the path in the room 
        
        self.percepts = self.env.signal(action)

        # Add visited node 
        self.visited.append(path[-1])

        # From the list of viable neighbors given by the environment
        # Select a random neighbor that has not been visited yet
        
        viable_neighbors =  self.percepts['neighbors']

        # If the agent is not stuck
        if viable_neighbors:
            ok = 1 
            # Select random neighbor
            while (ok == 1):
                visit = viable_neighbors[np.random.randint(0,len(viable_neighbors))]
                if visit is not self.visited:
                    # Append neighbor to the path and add it to the frontier
                    self.frontier = [path + [visit]] + self.frontier
                    ok = 0
                    

        print ('caminho')

        print([path])    

    def run(self):
        """Keeps the agent acting until it finds the target
        """

        # Run agent
        while (self.percepts['current_position'] != self.percepts['target']).any() and self.frontier:
            self.act()
            print('posiçao atual') 
            print(self.percepts['current_position'])
            print('Vizinhos') 
            print(self.percepts['neighbors'])
            print('fronteira')
            print(self.frontier)
            print('visitado')
            print(self.visited)
            input('Press ENTER to get out of here')
        print('Posicao final')
        print(self.percepts['current_position'])
                

class BFSAgent(Agent):
    """
    This class implements an agent that explores the environmente randomly
    until it reaches the target
    """

    def __init__(self, env):
        """Connects to the next available port.

        Args:
            env: A reference to an environment.

        """

        # Make a connection to the environment using the superclass constructor
        Agent.__init__(self,env)
        
        # Get initial percepts
        self.percepts = env.initial_percepts()
        
        # Initializes the frontier with the initial postion 
        self.frontier = [[self.percepts['current_position']]]
        
        # Initializes list of visited nodes for multiple path prunning
        self.visited = []

    def act(self):
        """Implements the agent action
        """

        # Select a path from the frontier
        path = self.frontier.pop(0)
        print('fronteira')
        print(self.frontier)
        # Visit the last node in the path
        action = {'visit_position': path[0], 'path': path} ############################pega o primeiro
        # The agente sends a position and the full path to the environment, the environment can plot the path in the room 
        
        self.percepts = self.env.signal(action)

        # Add visited node 
        self.visited.append(path[0])

        # From the list of viable neighbors given by the environment
        # Select a random neighbor that has not been visited yet
        
        viable_neighbors =  self.percepts['neighbors']
        
        if viable_neighbors:
            for i in viable_neighbors: 
                if np.all( i != self.visited):########vizinhoa nao adicinados 
                    print ('vi')
                    print(i)
                    self.frontier.append([path + [i]]) # adiciona no final
                    

        print ('caminho')

        print([path])   

    def run(self):
        """Keeps the agent acting until it finds the target
        """

        # Run agent
        while (self.percepts['current_position'] != self.percepts['target']).any() and self.frontier:
            self.act()
            print('posiçao atual') 
            print(self.percepts['current_position'])
            print('Vizinhos') 
            print(self.percepts['neighbors'])
            print('fronteira')
            print(self.frontier)
            print('visitado')
            print(self.visited)
            input('Press ENTER to get out of here')
        print('Posicao final')
        print(self.percepts['current_position'])


class DFSAgent(Agent):
    """
    This class implements an agent that explores the environmente randomly
    until it reaches the target
    """

    def __init__(self, env):
        """Connects to the next available port.

        Args:
            env: A reference to an environment.

        """

        
        Agent.__init__(self,env)
        
        # Get initial percepts
        self.percepts = env.initial_percepts()
        
        # Initializes the frontier with the initial postion 
        self.frontier = [[self.percepts['current_position']]]
        
        # Initializes list of visited nodes for multiple path prunning
        self.visited = []

    def act(self):
        """Implements the agent action
        """

        # Select a path from the frontier
        path = self.frontier.pop(0)
        print('fronteira')
        print(self.frontier)
        # Visit the last node in the path
        action = {'visit_position': path[-1], 'path': path} ############################pega o ultimo
        # The agente sends a position and the full path to the environment, the environment can plot the path in the room 
        
        self.percepts = self.env.signal(action)

        # Add visited node
        self.visited.append(path[-1])

        # From the list of viable neighbors given by the environment
        # Select a random neighbor that has not been visited yet
        
        viable_neighbors =  self.percepts['neighbors']
        
        if viable_neighbors:
            for i in viable_neighbors: 
                if np.all( i != self.visited): ########vizinhoa nao adicinados
                    print ('vi')
                    print(i)
                    self.frontier.append([path + [i]]) # adiciona no final
                    

        print ('caminho')

        print([path])   

    def run(self):
        """Keeps the agent acting until it finds the target
        """

        # Run agent
        while (self.percepts['current_position'] != self.percepts['target']).any() and self.frontier:
            self.act()
            print('posiçao atual') 
            print(self.percepts['current_position'])
            print('Vizinhos') 
            print(self.percepts['neighbors'])
            print('fronteira')
            print(self.frontier)
            print('visitado')
            print(self.visited)
            input('Press ENTER to get out of here')
        print('Posicao final')
        print(self.percepts['current_position'])        