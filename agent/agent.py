from ollama import chat
from ollama import ChatResponse
from ollama import Client
import logging
import os

__loggerPath__ = "agent/logs/"
__contextPath__ = "agent/contexts/"


class Agent:
    # Initialize an agent with a context message, it will be stored in the conversation.
    def __init__(self, model: str, name: str, context: str):
        self.logger = logging.getLogger("Agent "+name)
        self.logger.setLevel(logging.DEBUG)
        fh = logging.FileHandler(
            os.path.join(__loggerPath__,"agent_"+name+".log") ,encoding="utf-8", mode="w")
        fh.setLevel(logging.DEBUG)

        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)

        self.logger.addHandler(fh)

        self.path = __contextPath__+context+".txt"
        with open(self.path) as f:
            context_message = f.read().replace('\n', ' ')
            
        self.messages = [
            {'role': 'user', 'content': context_message},
        ]
        self.client = Client()
        self.model = model
        self.name = name

        try:

            init_msg = chat(
                model,
                messages=self.messages
            )

            self.messages += [
                {'role': 'assistant', 'content': init_msg.message.content},
            ]
            self.logger.debug("Successfully initiated agent %s model %s with context %s",
                              self.name, self.model, self.path)
        except Exception as e:
            self.logger.error(
                "Cannot initialize agent %s with error: %s", self.name, str(e))

    # With debug "true", returns the whole "ChatResponse" object
    def request(self, msg: str, debug=False):
        try:
            response = chat(
                self.model,
                messages=self.messages
                + [
                    {'role': 'user', 'content': msg},
                ],
            )

            self.messages += [
                {'role': 'user', 'content': msg},
                {'role': 'assistant', 'content': response.message.content},
            ]

            if debug:
                return response
            else:
                return response.message.content
        except Exception as e:
            self.logger.error(
                "Agent %s cannot process request. Error: %s", self.name, str(e))

    def __str__(self):
        return f"{self.name}({self.messages})"



