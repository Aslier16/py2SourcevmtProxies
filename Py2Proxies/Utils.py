from Pyroxies import Proxies
from typing import Union
import inspect

class Utils(Proxies):
    def __init__(self):
        super().__init__()
        self.tempVariables = {}

    def initTempVariables(self):
        self.tempVariables = {}

    def MOD(self,
            srcVar1: Union[str, list],
            srcVar2: Union[str, list],
            resultVar: Union[str, list]
        ):
        srcVar1 = self.initialVariables(srcVar1)
        srcVar2 = self.initialVariables(srcVar2)
        resultVar = self.initialVariables(resultVar)
