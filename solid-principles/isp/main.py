'''
Instead of creating a single generic interface,
create multiple specific interfaces
'''
from abc import ABC, abstractmethod


class Printer(ABC):
    @abstractmethod
    def print(self, page: str) -> None:
        pass

    @abstractmethod
    def fax(self, page: str) -> None:
        pass


class ModernPrinter(Printer):
    def print(self, page: str) -> None:
        print(page)
    
    def fax(self, page: str) -> None:
        # send mail -> some logic
        pass 


class OldPrinter(Printer):
    def print(self, page: str) -> None:
        print(page)
    
    def fax(self, page: str) -> None:
        raise NotImplementedError("old printer doesn't support fax") 
    
'''
The problem above is that we created a generic interface called printer.
which old printers do not support
'''

############ SOLUTION ################
class Printer2(ABC):
    @abstractmethod
    def print(self, page: str) -> None:
        pass


class FaxMachine(ABC):

    @abstractmethod
    def fax(self, page: str) -> None:
        pass


class ModernPrinter2(Printer2, FaxMachine):
    def print(self, page: str) -> None:
        print(page)
    
    def fax(self, page: str) -> None:
        # send mail -> some logic
        pass 


class OldPrinter2(Printer2):
    def print(self, page: str) -> None:
        print(page)
    

''' 
Above we created specific interfaces so we can use them more precisely
'''