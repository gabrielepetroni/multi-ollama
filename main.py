from agent.agent import Agent
from pool.pool import Pool


pool = Pool("Aula")
pool.add_agent(Agent("llama3.2", "Diego", "student_diego"))
pool.add_agent(Agent("llama3.2", "Alvaro", "student_alvaro"))
pool.simulate_two(10, "Diego", "Alvaro", "Hola, me llamo Alvaro, que tal?", True)