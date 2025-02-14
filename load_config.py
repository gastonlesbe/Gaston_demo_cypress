import configparser
import os

def load_tools_config():
    tools = configparser.RawConfigParser()
    tools.read(os.path.join(os.getcwd(),"tools.cfg"))
    return tools