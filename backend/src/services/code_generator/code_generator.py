from abc import ABC, abstractmethod


class CodeGeneratorService(ABC):
    @abstractmethod
    def generate(self, length: int) -> str:
        pass