import logging
from agent.agent import Agent

class Pool:
    def __init__(self, name: str):
        self.name = name
        
        self.logger = logging.getLogger("Pool "+name)
        self.logger.setLevel(logging.DEBUG)
        fh = logging.FileHandler(
            "logs/pool_"+name+".log", encoding="utf-8", mode="w")
        fh.setLevel(logging.DEBUG)

        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)

        self.logger.addHandler(fh)
        
    #def add_agent(self, agent: Agent):
        