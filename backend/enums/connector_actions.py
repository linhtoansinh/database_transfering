from enum import Enum


class ConnectorAction(str, Enum):
    restart = "restart" #POST
    pause = "pause"
    resume = "resume"
    stop = "stop"
