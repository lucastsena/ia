from room import Room
from path_finder_agents import RandAgent
from path_finder_agents import BFSAgent
from path_finder_agents import TestAgent
from path_finder_agents import DFSAgent


#env = Room(room=[[0, 0, 1], [0, 0, 1], [0, 0, 0]], target=[2, 2], plot_on=True)
env = Room(prob=0.3, n=20, plot_on=True)
#agent = RandAgent(env)
#agent = TestAgent(env) 
#agent = BFSAgent(env)
agent = DFSAgent(env)
# agent = AStarAgent(env)
# agent = GreedyAgent(env)

agent.run()

input('Press ENTER to get out of here')
