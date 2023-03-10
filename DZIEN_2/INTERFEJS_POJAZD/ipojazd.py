from abc import ABCMeta, abstractmethod

class IPojazd(metaclass=ABCMeta):

    @abstractmethod
    def spalanie_100(self,litry,odl):raise NotImplementedError

    @abstractmethod
    def kosztyprzejazdu(self,litry,odl,cena_l):raise NotImplementedError
