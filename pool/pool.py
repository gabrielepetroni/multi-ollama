import logging
from agent.agent import *
import time

__loggerPath__ = "pool/logs/"

class Pool:
    def __init__(self, name: str):
        
        try:
            self.name = name
            
            self.logger = logging.getLogger("Pool "+name)
            self.logger.setLevel(logging.DEBUG)
            fh = logging.FileHandler(
                os.path.join(__loggerPath__,"pool_"+name+".log"), encoding="utf-8", mode="a")
            fh.setLevel(logging.DEBUG)

            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            fh.setFormatter(formatter)

            self.logger.addHandler(fh)
            
            self.agents = dict()
            
            self.logger.debug("Successfully initiated pool %s", self.name)
        except Exception as e:
            self.logger.error("Cannot initialize pool %s with error: %s", self.name, str(e))

        
    def add_agent(self, agent: Agent):
        self.agents[agent.name] = agent
        
    def del_agent(self, agent: Agent):
        self.agents.pop(agent.name)   
        
    def simulate_two(self, iteractions: int, name1: str, name2: str, prompt: str, to_log = False):
        agent1 = self.agents[name1]
        agent2 = self.agents[name2]
        
        if to_log: self.logger.info("SIMULATION START")
        
        resp = agent1.request(prompt)
        print(name1+": "+resp)
        if to_log: self.logger.debug(name1+": "+resp)
       
        
        for x in range(iteractions):
            m = agent2.request(resp)
            print(name2+": "+m)
            if to_log: self.logger.debug(name2+": "+m)
            time.sleep(1)
            resp = agent1.request(m)
            print(name1+": "+resp)
            if to_log: self.logger.debug(name1+": "+resp)
            time.sleep(1)
        
        if to_log: self.logger.info("SIMULATION END")
