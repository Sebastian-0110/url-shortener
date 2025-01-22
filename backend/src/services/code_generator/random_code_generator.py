import random
import string

from .code_generator import CodeGeneratorService


class RandomCodeGeneratorService(CodeGeneratorService):
    def generate(self, length: int) -> str:
        return "".join([random.choice(string.ascii_letters) for _ in range(length)])
