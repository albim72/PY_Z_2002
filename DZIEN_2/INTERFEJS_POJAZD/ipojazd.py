from abc import ABCMeta, abstractmethod

class IPojazd(metaclass=ABCMeta):
    
    @abstractmethod
    def spalanie_100(self):raise NotImplementedError
    
    @abstractmethod
    def kosztyprzejazdu(self):raise NotImplementedError
    
