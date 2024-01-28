from abc import ABC, abstractmethod

class IO(ABC):
    @abstractmethod
    def bot_print(self, *args, **kwargs):
        pass
    
    @abstractmethod
    def bot_input(self, *args, **kwargs):
        pass

class CliIO(IO):
    def bot_print(self, *args, **kwargs):
        print(*args, **kwargs)
    
    def bot_input(self, *args, **kwargs):
        return input(*args, **kwargs)
