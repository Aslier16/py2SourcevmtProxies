import threading
import re


class Proxies:
    def __init__(self):
        self.initVariables = {}
        self.calculatedVariables = {}
        self.content = ""
        self.time = 0
        self.frequency = 1
        self.timer = threading.Timer(self.frequency, self.updateTime)
        self.timer.start()

    def updateTime(self):
        self.time += self.frequency
        # print(self.time)
        self.timer = threading.Timer(self.frequency, self.updateTime)
        self.timer.start()

    # 四则运算
    def Add(self, srcVar1: str, srcVar2: str, resultVar: str):
        """加法
        resultVar = srcVar1 + srcVar2

        Args:
            srcVar1 (str): 加数1
            srcVar2 (str): 加数2
            resultVar (str): 存储结果的变量
        """
        if srcVar1 not in self.initVariables:
            self.initVariables[srcVar1] = 0.0
            self.calculatedVariables[srcVar1] = 0.0
        if srcVar2 not in self.initVariables:
            self.initVariables[srcVar2] = 0.0
            self.calculatedVariables[srcVar2] = 0.0
        if resultVar not in self.initVariables:
            self.initVariables[resultVar] = 0.0
            self.calculatedVariables[resultVar] = 0.0
        self.content += f'\tAdd\n\t{{\n\t\tsrcVar1\t"${srcVar1}"\n\t\tsrcVar2\t"${srcVar2}",\n\t\tresultVar\t"${resultVar}"\n\t}}\n'

        # try:
        #     self.calculatedVariables[resultVar] = self.calculatedVariables[srcVar1] + self.calculatedVariables[srcVar2]
        # except Exception:
        #     pass

    def Subtract(self, srcVar1: str, srcVar2: str, resultVar: str):
        """减法
        resultVar = srcVar1 - srcVar2

        Args:
            srcVar1 (str): 被减数
            srcVar2 (str): 减数
            resultVar (str): 存储结果的变量
        """
        if srcVar1 not in self.initVariables:
            self.initVariables[srcVar1] = 0.0
            self.calculatedVariables[srcVar1] = 0.0
        if srcVar2 not in self.initVariables:
            self.initVariables[srcVar2] = 0.0
            self.calculatedVariables[srcVar2] = 0.0
        if resultVar not in self.initVariables:
            self.initVariables[resultVar] = 0.0
            self.calculatedVariables[resultVar] = 0.0

        self.content += f'\tSubtract\n\t{{\n\t\tsrcVar1\t"${srcVar1}"\n\t\tsrcVar2\t"${srcVar2}"\n\t\tresultVar\t"${resultVar}"\n\t}}\n'
        # try:
        #     self.calculatedVariables[resultVar] = self.calculatedVariables[srcVar1] - self.calculatedVariables[srcVar2]
        # except Exception:
        #     pass

    def Multiply(self, srcVar1: str, srcVar2: str, resultVar: str):
        """乘法
        resultVar = srcVar1 * srcVar2

        Args:
            srcVar1 (str): 乘数1
            srcVar2 (str): 乘数2
            resultVar (str): 存储结果的变量
        """
        if srcVar1 not in self.initVariables:
            self.initVariables[srcVar1] = 0.0
            self.calculatedVariables[srcVar1] = 0.0
        if srcVar2 not in self.initVariables:
            self.initVariables[srcVar2] = 0.0
            self.calculatedVariables[srcVar2] = 0.0
        if resultVar not in self.initVariables:
            self.initVariables[resultVar] = 0.0
            self.calculatedVariables[resultVar] = 0.0
        self.content += f'\tMultiply\n\t{{\n\t\tsrcVar1\t"${srcVar1}"\n\t\tsrcVar2\t"${srcVar2}"\n\t\tresultVar\t"${resultVar}"\n\t}}\n'

        # try:
        #     self.calculatedVariables[resultVar] = self.calculatedVariables[srcVar1] * self.calculatedVariables[srcVar2]
        # except Exception:
        #     pass

    def Divide(self, srcVar1: str, srcVar2: str, resultVar: str):
        """除法
        resultVar = srcVar1 / srcVar2

        Args:
            srcVar1 (str): 被除数
            srcVar2 (str): 除数
            resultVar (str): 存储结果的变量
        """
        if srcVar1 not in self.initVariables:
            self.initVariables[srcVar1] = 0.0
            self.calculatedVariables[srcVar1] = 0.0
        if srcVar2 not in self.initVariables:
            self.initVariables[srcVar2] = 0.0
            self.calculatedVariables[srcVar2] = 0.0
        if resultVar not in self.initVariables:
            self.initVariables[resultVar] = 0.0
            self.calculatedVariables[resultVar] = 0.0
        self.content += f'\tDivide\n\t{{\n\t\tsrcVar1\t"${srcVar1}"\n\t\tsrcVar2\t"${srcVar2}"\n\t\tresultVar\t"${resultVar}"\n\t}}\n'

        # try:
        #     self.calculatedVariables[resultVar] = self.calculatedVariables[srcVar1] / self.calculatedVariables[srcVar2]
        # except Exception:
        #     pass

    def Equals(self, srcVar1: str, resultVar: str):
        """赋值
        resultVar = srcVar1

        Args:
            srcVar1 (str): 源变量
            resultVar (str): 存储结果的变量
        """
        if srcVar1 not in self.initVariables:
            self.initVariables[srcVar1] = 0.0
            self.calculatedVariables[srcVar1] = 0.0
        if resultVar not in self.initVariables:
            self.initVariables[resultVar] = 0.0
            self.calculatedVariables[resultVar] = 0.0
        self.content += f'\tEquals\n\t{{\n\t\tsrcVar1\t"${srcVar1}"\n\t\tresultVar\t"${resultVar}"\n\t}}\n'

        # try:
        #     self.calculatedVariables[resultVar] = self.calculatedVariables[srcVar1] + self.calculatedVariables[srcVar2]
        # except Exception:
        #     pass

    def Abs(self, srcVar1: str, resultVar: str):
        """取绝对值
        resultVar = abs(srcVar1)

        Args:
            srcVar1 (str): 源变量
            resultVar (str): 存储结果的变量
        """
        if srcVar1 not in self.initVariables:
            self.initVariables[srcVar1] = 0.0
            self.calculatedVariables[srcVar1] = 0.0
        if resultVar not in self.initVariables:
            self.initVariables[resultVar] = 0.0
            self.calculatedVariables[resultVar] = 0.0
        self.content += f'\tAbs\n\t{{\n\t\tsrcVar1\t"${srcVar1}"\n\t\tresultVar\t"${resultVar}"\n\t}}\n'

    def Frac(self, srcVar1: str, resultVar: str):
        """取小数
        resultVar = srcVar1 - int(srcVar1)

        Args:
            srcVar1 (str): 源变量
            resultVar (str): 存储结果的变量
        """
        if srcVar1 not in self.initVariables:
            self.initVariables[srcVar1] = 0.0
            self.calculatedVariables[srcVar1] = 0.0
        if resultVar not in self.initVariables:
            self.initVariables[resultVar] = 0.0
            self.calculatedVariables[resultVar] = 0.0
        self.content += f'\tFrac\n\t{{\n\t\tsrcVar1\t"${srcVar1}"\n\t\tresultVar\t"${resultVar}"\n\t}}\n'

    def Int(self, srcVar1: str, resultVar: str):
        """取整
        resultVar = int(srcVar1)
        Args:
            srcVar1 (str): 源变量
            resultVar (str): 存储结果的变量
        """
        if srcVar1 not in self.initVariables:
            self.initVariables[srcVar1] = 0.0
            self.calculatedVariables[srcVar1] = 0.0
        if resultVar not in self.initVariables:
            self.initVariables[resultVar] = 0.0
            self.calculatedVariables[resultVar] = 0.0
        self.content += f'\tInt\n\t{{\n\t\tsrcVar1\t"${srcVar1}"\n\t\tresultVar\t"${resultVar}"\n\t}}\n'

    def Clamp(self, min: str, max: str, srcVar1: str, resultVar: str):
        """限制变量的取值范围

        Args:
            min (str): 最小值
            max (str): 最大值
            srcVar1 (str): 数值源变量
            resultVar (str): 存储限制后值的变量
        """
        if min not in self.initVariables:
            self.initVariables[min] = 0.0
            self.calculatedVariables[min] = 0.0
        if max not in self.initVariables:
            self.initVariables[max] = 0.0
            self.calculatedVariables[max] = 0.0
        if srcVar1 not in self.initVariables:
            self.initVariables[srcVar1] = 0.0
            self.calculatedVariables[srcVar1] = 0.0
        if resultVar not in self.initVariables:
            self.initVariables[resultVar] = 0.0
            self.calculatedVariables[resultVar] = 0.0
        self.content += f'\tClamp\n\t{{\n\t\tmin\t"${min}"\n\t\tmax\t"${max}"\n\t\tsrcVar1\t"${srcVar1}"\n\t\tresultVar\t"${resultVar}"\n\t}}\n'

    def LessOrEqual(
        self,
        lessEqualVar: str,
        greaterVar: str,
        srcVar1: str,
        srcVar2: str,
        resultVar: str,
    ):
        """比较大小, 如果srcVar1小于等于srcVar2, resultVar等于lessEqualVar, 否则等于greaterVar
            resultVar = lessEqualVar if srcVar1 <= srcVar2 else resultVar = greaterVar

        Args:
            lessEqualVar (str): 小于等于时
            greaterVar (str): 大于时
            srcVar1 (str): 比较的左值
            srcVar2 (str): 比较的右值
            resultVar (str): 存储结果的变量
        """
        if lessEqualVar not in self.initVariables:
            self.initVariables[lessEqualVar] = 0.0
            self.calculatedVariables[lessEqualVar] = 0.0
        if greaterVar not in self.initVariables:
            self.initVariables[greaterVar] = 0.0
            self.calculatedVariables[greaterVar] = 0.0
        if srcVar1 not in self.initVariables:
            self.initVariables[srcVar1] = 0.0
            self.calculatedVariables[srcVar1] = 0.0
        if srcVar2 not in self.initVariables:
            self.initVariables[srcVar2] = 0.0
            self.calculatedVariables[srcVar2] = 0.0
        if resultVar not in self.initVariables:
            self.initVariables[resultVar] = 0.0
            self.calculatedVariables[resultVar] = 0.0
        self.content += f'\tLessOrEqual\n\t{{\n\t\tlessEqualVar\t"${lessEqualVar}"\n\t\tgreaterVar\t"${greaterVar}"\n\t\tsrcVar1\t"${srcVar1}"\n\t\tsrcVar2\t"${srcVar2}"\n\t\tresultVar\t"${resultVar}"\n\t}}\n'

    def SelectFirstIfNonZero(self, srcVar1: str, srcVar2: str, resultVar: str):
        if srcVar1 not in self.initVariables:
            self.initVariables[srcVar1] = 0.0
            self.calculatedVariables[srcVar1] = 0.0
        if srcVar2 not in self.initVariables:
            self.initVariables[srcVar2] = 0.0
            self.calculatedVariables[srcVar2] = 0.0
        if resultVar not in self.initVariables:
            self.initVariables[resultVar] = 0.0
            self.calculatedVariables[resultVar] = 0.0
        self.content += f'\tSelectFirstIfNonZero\n\t{{\n\t\tsrcVar1\t"${srcVar1}"\n\t\tsrcVar2\t"${srcVar2}"\n\t\tresultVar\t"${resultVar}"\n\t}}\n'

    def WrapMinMax(self, srcVar1: str, min: str, max: str, resultVar: str):
        if srcVar1 not in self.initVariables:
            self.initVariables[srcVar1] = 0.0
            self.calculatedVariables[srcVar1] = 0.0
        if min not in self.initVariables:
            self.initVariables[min] = 0.0
            self.calculatedVariables[min] = 0.0
        if max not in self.initVariables:
            self.initVariables[max] = 0.0
            self.calculatedVariables[max] = 0.0
        if resultVar not in self.initVariables:
            self.initVariables[resultVar] = 0.0
            self.calculatedVariables[resultVar] = 0.0
        self.content += f'\tWrapMinMax\n\t{{\n\t\tsrcVar1\t"${srcVar1}"\n\t\tmin\t"${min}"\n\t\tmax\t"${max}"\n\t\tresultVar\t"${resultVar}"\n\t}}\n'

    def Exponential(
        self,
        minVal: str,
        maxVal: str,
        srcVar1: str,
        offset: str,
        scale: str,
        resultVar: str,
    ):
        if minVal not in self.initVariables:
            self.initVariables[minVal] = 0.0
            self.calculatedVariables[minVal] = 0.0
        if maxVal not in self.initVariables:
            self.initVariables[maxVal] = 0.0
            self.calculatedVariables[maxVal] = 0.0
        if srcVar1 not in self.initVariables:
            self.initVariables[srcVar1] = 0.0
            self.calculatedVariables[srcVar1] = 0.0
        if offset not in self.initVariables:
            self.initVariables[offset] = 0.0
            self.calculatedVariables[offset] = 0.0
        if scale not in self.initVariables:
            self.initVariables[scale] = 0.0
            self.calculatedVariables[scale] = 0.0
        if resultVar not in self.initVariables:
            self.initVariables[resultVar] = 0.0
            self.calculatedVariables[resultVar] = 0.0
        self.content += f'\tExponential\n\t{{\n\t\tminVal\t"${minVal}"\n\t\tmaxVal\t"${maxVal}"\n\t\tsrcVar1\t"${srcVar1}"\n\t\toffset\t"${offset}"\n\t\tscale\t"${scale}"\n\t\tresultVar\t"${resultVar}"\n\t}}\n'

    # 数值生成
    def Sine(
        self,
        sineperiod: str,
        sinemin: str,
        sinemax: str,
        timeoffset: str,
        resultVar: str,
    ):
        """正弦函数
        resultVar = sinemin + (sinemax - sinemin) * sin(2 * pi * time / sineperiod + timeoffset)

        Args:
            sineperiod (str): 周期
            sinemin (str): 最小值
            sinemax (str): 最大值
            timeoffset (str): 相位
            resultVar (str): 存储正弦值的变量
        """
        if sineperiod not in self.initVariables:
            self.initVariables[sineperiod] = 0.0
            self.calculatedVariables[sineperiod] = 0.0
        if sinemin not in self.initVariables:
            self.initVariables[sinemin] = 0.0
            self.calculatedVariables[sinemin] = 0.0
        if sinemax not in self.initVariables:
            self.initVariables[sinemax] = 0.0
            self.calculatedVariables[sinemax] = 0.0
        if timeoffset not in self.initVariables:
            self.initVariables[timeoffset] = 0.0
            self.calculatedVariables[timeoffset] = 0.0
        if resultVar not in self.initVariables:
            self.initVariables[resultVar] = 0.0
            self.calculatedVariables[resultVar] = 0.0
        self.content += f'\tSine\n\t{{\n\t\tsineperiod\t"${sineperiod}"\n\t\tsinemin\t"${sinemin}"\n\t\tsinemax\t"${sinemax}"\n\t\ttimeoffset\t"${timeoffset}"\n\t\tresultVar\t"${resultVar}"\n\t}}\n'

    def LinearRamp(self, rate: str, initialValue: str, resultVar: str):
        """线性函数
        resultVar = initialValue + rate * time

        Args:
            rate (str): 斜率/增长速率
            initialValue (str): 初始值
            resultVar (str): 存储结果的变量
        """
        if rate not in self.initVariables:
            self.initVariables[rate] = 0.0
            self.calculatedVariables[rate] = 0.0
        if initialValue not in self.initVariables:
            self.initVariables[initialValue] = 0.0
            self.calculatedVariables[initialValue] = 0.0
        if resultVar not in self.initVariables:
            self.initVariables[resultVar] = 0.0
            self.calculatedVariables[resultVar] = 0.0
        self.content += f'\tLinearRamp\n\t{{\n\t\trate\t"${rate}"\n\t\tinitialValue\t"${initialValue}"\n\t\tresultVar\t"${resultVar}"\n\t}}\n'

    def CurrentTime(self, resultVar: str):
        """获取当前地图时间

        Args:
            resultVar (str): 存储时间的变量
        """
        if resultVar not in self.initVariables:
            self.initVariables[resultVar] = 0.0
            self.calculatedVariables[resultVar] = 0.0

        self.content += f'\tCurrentTime\n\t{{\n\t\tresultVar\t"${resultVar}"\n\t}}\n'
        # try:
        #     self.calculatedVariables[resultVar] = self.time
        # except Exception:
        #     pass

    def UniformNoise(self, minVal: str, maxVal: str, resultVar: str):
        if minVal not in self.initVariables:
            self.initVariables[minVal] = 0.0
            self.calculatedVariables[minVal] = 0.0
        if maxVal not in self.initVariables:
            self.initVariables[maxVal] = 0.0
            self.calculatedVariables[maxVal] = 0.0
        if resultVar not in self.initVariables:
            self.initVariables[resultVar] = 0.0
            self.calculatedVariables[resultVar] = 0.0
        self.content += f'\tUniformNoise\n\t{{\n\t\tminVal\t"${minVal}"\n\t\tmaxVal\t"${maxVal}"\n\t\tresultVar\t"${resultVar}"\n\t}}\n'

    def GaussianNoise(
        self, mean: str, halfWidth: str, minVal: str, maxVal: str, resultVar: str
    ):
        if mean not in self.initVariables:
            self.initVariables[mean] = 0.0
            self.calculatedVariables[mean] = 0.0
        if halfWidth not in self.initVariables:
            self.initVariables[halfWidth] = 0.0
            self.calculatedVariables[halfWidth] = 0.0
        if minVal not in self.initVariables:
            self.initVariables[minVal] = 0.0
            self.calculatedVariables[minVal] = 0.0
        if maxVal not in self.initVariables:
            self.initVariables[maxVal] = 0.0
            self.calculatedVariables[maxVal] = 0.0
        if resultVar not in self.initVariables:
            self.initVariables[resultVar] = 0.0
            self.calculatedVariables[resultVar] = 0.0
        self.content += f'\tGaussianNoise\n\t{{\n\t\tmean\t"${mean}"\n\t\thalfWidth\t"${halfWidth}"\n\t\tminVal\t"${minVal}"\n\t\tmaxVal\t"${maxVal}"\n\t\tresultVar\t"${resultVar}"\n\t}}\n'

    def MatrixRotate(self, axisVar: str, angle: str, resultVar: str):
        if axisVar not in self.initVariables:
            self.initVariables[axisVar] = 0.0
            self.calculatedVariables[axisVar] = 0.0
        if angle not in self.initVariables:
            self.initVariables[angle] = 0.0
            self.calculatedVariables[angle] = 0.0
        if resultVar not in self.initVariables:
            self.initVariables[resultVar] = 0.0
            self.calculatedVariables[resultVar] = 0.0
        self.content += f'\tMatrixRotate\n\t{{\n\t\taxisVar\t"${axisVar}"\n\t\tangle\t"${angle}"\n\t\tresultVar\t"${resultVar}"\n\t}}\n'

    # 实体数据获取
    def Alpha(self):
        self.content += f"\tAlpha\n\t{{\n\t\t$alpha\n\t}}\n"

    def Cycle(self, start: str, end: str, easein: str, easeout: str, resultVar: str):
        if start not in self.initVariables:
            self.initVariables[start] = 0.0
            self.calculatedVariables[start] = 0.0
        if end not in self.initVariables:
            self.initVariables[end] = 0.0
            self.calculatedVariables[end] = 0.0
        if easein not in self.initVariables:
            self.initVariables[easein] = 0.0
            self.calculatedVariables[easein] = 0.0
        if easeout not in self.initVariables:
            self.initVariables[easeout] = 0.0
            self.calculatedVariables[easeout] = 0.0
        if resultVar not in self.initVariables:
            self.initVariables[resultVar] = 0.0
            self.calculatedVariables[resultVar] = 0.0
        self.content += f'\tCycle\n\t{{\n\t\tstart\t"${start}"\n\t\tend\t"${end}"\n\t\teasein\t"${easein}"\n\t\teaseout\t"${easeout}"\n\t\tresultVar\t"${resultVar}"\n\t}}\n'

    def PlayerProximity(self, scale: str, resultVar: str):
        """获取实体与玩家的距离

        Args:
            scale (str): 数值缩放
            resultVar (str): 存储缩放后结果的变量
        """
        if scale not in self.initVariables:
            self.initVariables[scale] = 0.0
            self.calculatedVariables[scale] = 0.0
        if resultVar not in self.initVariables:
            self.initVariables[resultVar] = 0.0
            self.calculatedVariables[resultVar] = 0.0
        self.content += f'\tPlayerProximity\n\t{{\n\t\tscale\t"${scale}"\n\t\tresultVar\t"${resultVar}"\n\t}}\n'

    def PlayerTeamMatch(self, resultVar: str):
        if resultVar not in self.initVariables:
            self.initVariables[resultVar] = 0.0
            self.calculatedVariables[resultVar] = 0.0
        self.content += (
            f'\tPlayerTeamMatch\n\t{{\n\t\tresultVar\t"${resultVar}"\n\t}}\n'
        )

    def PlayerView(self, resultVar: str):
        if resultVar not in self.initVariables:
            self.initVariables[resultVar] = 0.0
            self.calculatedVariables[resultVar] = 0.0
        self.content += f'\tPlayerView\n\t{{\n\t\tresultVar\t"${resultVar}"\n\t}}\n'

    def PlayerSpeed(self, scale: str, resultVar: str):
        """获取玩家速度

        Args:
            scale (str): 数值缩放(=1时玩家最大行走速度为220)
            resultVar (str): 存储缩放后速度的变量
        """
        if scale not in self.initVariables:
            self.initVariables[scale] = 0.0
            self.calculatedVariables[scale] = 0.0
        if resultVar not in self.initVariables:
            self.initVariables[resultVar] = 0.0
            self.calculatedVariables[resultVar] = 0.0
        self.content += f'\tPlayerSpeed\n\t{{\n\t\tscale\t"${scale}"\n\t\tresultVar\t"${resultVar}"\n\t}}\n'

    def PlayerPosition(self, scale: str, resultVar: str):
        if scale not in self.initVariables:
            self.initVariables[scale] = 0.0
            self.calculatedVariables[scale] = 0.0
        if resultVar not in self.initVariables:
            self.initVariables[resultVar] = 0.0
            self.calculatedVariables[resultVar] = 0.0
        self.content += f'\tPlayerPosition\n\t{{\n\t\tscale\t"${scale}"\n\t\tresultVar\t"${resultVar}"\n\t}}\n'

    def EntitySpeed(self, resultVar: str):
        if resultVar not in self.initVariables:
            self.initVariables[resultVar] = 0.0
            self.calculatedVariables[resultVar] = 0.0
        self.content += f'\tEntitySpeed\n\t{{\n\t\tresultVar\t"${resultVar}"\n\t}}\n'

    def EntityOrigin(self):
        self.content += f"\tEntityOrigin\n\t{{\n\t\t$entityorigin}}\n"

    def EntityRandom(self, scale: str, resultVar: str):
        """生成一个绑定实体的随机数

        Args:
            scale (str): 数值缩放
            resultVar (str): 存储缩放后结果的变量
        """
        if scale not in self.initVariables:
            self.initVariables[scale] = 0.0
            self.calculatedVariables[scale] = 0.0
        if resultVar not in self.initVariables:
            self.initVariables[resultVar] = 0.0
            self.calculatedVariables[resultVar] = 0.0
        self.content += f'\tEntityRandom\n\t{{\n\t\tscale\t"${scale}"\n\t\tresultVar\t"${resultVar}"\n\t}}\n'

    def Health(self, scale: str, resultVar: str):
        if scale not in self.initVariables:
            self.initVariables[scale] = 0.0
            self.calculatedVariables[scale] = 0.0
        if resultVar not in self.initVariables:
            self.initVariables[resultVar] = 0.0
            self.calculatedVariables[resultVar] = 0.0
        self.content += f'\tHealth\n\t{{\n\t\tscale\t"${scale}"\n\t\tresultVar\t"${resultVar}"\n\t}}\n'

    def IsNPC(self, scale: str, resultVar: str):
        if scale not in self.initVariables:
            self.initVariables[scale] = 0.0
            self.calculatedVariables[scale] = 0.0
        if resultVar not in self.initVariables:
            self.initVariables[resultVar] = 0.0
            self.calculatedVariables[resultVar] = 0.0
        self.content += f'\tIsNPC\n\t{{\n\t\tscale\t"${scale}"\n\t\tresultVar\t"${resultVar}"\n\t}}\n'

    def WorldDims(self):
        self.content += f"\tWorldDims\n\t{{\n\t\t$world_mins\n\t\t$world_maxs}}\n"

    def CrosshariColor(self, resultVar: str):
        if resultVar not in self.initVariables:
            self.initVariables[resultVar] = 0.0
            self.calculatedVariables[resultVar] = 0.0
        self.content += f'\tCrosshariColor\n\t{{\n\t\tresultVar\t"${resultVar}"\n\t}}\n'

    # 贴图操纵 Texture manipulation
    def AnimatedTexture(
        self,
        animatedtexturevar: str,
        animatedtextureframenumvar: str,
        animatedtextureframerate: str,
    ):
        """贴图播放

        Args:
            animatedtexturevar (str): 要播放的贴图路径变量
            animatedtextureframenumvar (str): 控制帧数的变量
            animatedtextureframerate (str): 帧率常量
        """
        if animatedtexturevar not in self.initVariables:
            self.initVariables[animatedtexturevar] = 0.0
            self.calculatedVariables[animatedtexturevar] = 0.0
        if animatedtextureframenumvar not in self.initVariables:
            self.initVariables[animatedtextureframenumvar] = 0.0
            self.calculatedVariables[animatedtextureframenumvar] = 0.0
        if animatedtextureframerate not in self.initVariables:
            self.initVariables[animatedtextureframerate] = 0.0
            self.calculatedVariables[animatedtextureframerate] = 0.0
        self.content += f'\tAnimatedTexture\n\t{{\n\t\tanimatedtexturevar\t"${animatedtexturevar}"\n\t\tanimatedtextureframenumvar\t"${animatedtextureframenumvar}"\n\t\tanimatedtextureframerate\t"${animatedtextureframerate}"\n\t}}\n'

    def AnimatedEntityTexture(
        self,
        animatedtexturevar: str,
        animatedtextureframenumvar: str,
        animatedtextureframerate: str,
    ):
        if animatedtexturevar not in self.initVariables:
            self.initVariables[animatedtexturevar] = 0.0
            self.calculatedVariables[animatedtexturevar] = 0.0
        if animatedtextureframenumvar not in self.initVariables:
            self.initVariables[animatedtextureframenumvar] = 0.0
            self.calculatedVariables[animatedtextureframenumvar] = 0.0
        if animatedtextureframerate not in self.initVariables:
            self.initVariables[animatedtextureframerate] = 0.0
            self.calculatedVariables[animatedtextureframerate] = 0.0
        self.content += f'\tAnimatedEntityTexture\n\t{{\n\t\tanimatedtexturevar\t"${animatedtexturevar}"\n\t\tanimatedtextureframenumvar\t"${animatedtextureframenumvar}"\n\t\tanimatedtextureframerate\t"${animatedtextureframerate}"\n\t}}\n'

    def AnimatedOffsetTexture(
        self,
        animatedtexturevar: str,
        animatedtextureframenumvar: str,
        animatedtextureframerate: str,
    ):
        if animatedtexturevar not in self.initVariables:
            self.initVariables[animatedtexturevar] = 0.0
            self.calculatedVariables[animatedtexturevar] = 0.0
        if animatedtextureframenumvar not in self.initVariables:
            self.initVariables[animatedtextureframenumvar] = 0.0
            self.calculatedVariables[animatedtextureframenumvar] = 0.0
        if animatedtextureframerate not in self.initVariables:
            self.initVariables[animatedtextureframerate] = 0.0
            self.calculatedVariables[animatedtextureframerate] = 0.0
        self.content += f'\tAnimatedOffsetTexture\n\t{{\n\t\tanimatedtexturevar\t"${animatedtexturevar}"\n\t\tanimatedtextureframenumvar\t"${animatedtextureframenumvar}"\n\t\tanimatedtextureframerate\t"${animatedtextureframerate}"\n\t}}\n'

    def AnimateSpecificTexture(
        self,
        animatedtexturevar: str,
        animatedtextureframenumvar: str,
        animatedtextureframerate: str,
        onlyAnimateOnTexture: str,
    ):
        if animatedtexturevar not in self.initVariables:
            self.initVariables[animatedtexturevar] = 0.0
            self.calculatedVariables[animatedtexturevar] = 0.0
        if animatedtextureframenumvar not in self.initVariables:
            self.initVariables[animatedtextureframenumvar] = 0.0
            self.calculatedVariables[animatedtextureframenumvar] = 0.0
        if animatedtextureframerate not in self.initVariables:
            self.initVariables[animatedtextureframerate] = 0.0
            self.calculatedVariables[animatedtextureframerate] = 0.0
        if onlyAnimateOnTexture not in self.initVariables:
            self.initVariables[onlyAnimateOnTexture] = 0.0
            self.calculatedVariables[onlyAnimateOnTexture] = 0.0
        self.content += f'\tAnimateSpecificTexture\n\t{{\n\t\tanimatedtexturevar\t"${animatedtexturevar}"\n\t\tanimatedtextureframenumvar\t"${animatedtextureframenumvar}"\n\t\tanimatedtextureframerate\t"${animatedtextureframerate}"\n\t\tonlyAnimateOnTexture\t"${onlyAnimateOnTexture}"\n\t}}\n'

    def Pupil(
        self,
        TextureVar: str,
        TextureFrameNumVar: str,
        PupilCloseRate: str,
        PupilOpenRate: str,
    ):
        if TextureVar not in self.initVariables:
            self.initVariables[TextureVar] = 0.0
            self.calculatedVariables[TextureVar] = 0.0
        if TextureFrameNumVar not in self.initVariables:
            self.initVariables[TextureFrameNumVar] = 0.0
            self.calculatedVariables[TextureFrameNumVar] = 0.0
        if PupilCloseRate not in self.initVariables:
            self.initVariables[PupilCloseRate] = 0.0
            self.calculatedVariables[PupilCloseRate] = 0.0
        if PupilOpenRate not in self.initVariables:
            self.initVariables[PupilOpenRate] = 0.0
            self.calculatedVariables[PupilOpenRate] = 0.0
        self.content += f'\tPupil\n\t{{\n\t\tTextureVar\t"${TextureVar}"\n\t\tTextureFrameNumVar\t"${TextureFrameNumVar}"\n\t\tPupilCloseRate\t"${PupilCloseRate}"\n\t\tPupilOpenRate\t"${PupilOpenRate}"\n\t\t$lighting\n\t}}\n'

    def TextureTransform(
        self,
        centerVar: str,
        scaleVar: str,
        rotateVar: str,
        translateVar: str,
        resultVar: str,
    ):
        if centerVar not in self.initVariables:
            self.initVariables[centerVar] = 0.0
            self.calculatedVariables[centerVar] = 0.0
        if scaleVar not in self.initVariables:
            self.initVariables[scaleVar] = 0.0
            self.calculatedVariables[scaleVar] = 0.0
        if rotateVar not in self.initVariables:
            self.initVariables[rotateVar] = 0.0
            self.calculatedVariables[rotateVar] = 0.0
        if translateVar not in self.initVariables:
            self.initVariables[translateVar] = 0.0
            self.calculatedVariables[translateVar] = 0.0
        if resultVar not in self.initVariables:
            self.initVariables[resultVar] = 0.0
            self.calculatedVariables[resultVar] = 0.0
        self.content += f'\tTextureTransform\n\t{{\n\t\tcenterVar\t"${centerVar}"\n\t\tscaleVar\t"${scaleVar}"\n\t\trotateVar\t"${rotateVar}"\n\t\ttranslateVar\t"${translateVar}"\n\t\tresultVar\t"${resultVar}"\n\t}}\n'

    def TextureScroll(
        self,
        textureScrollVar: str,
        textureScrollRate: str,
        textureScrollAngle: str,
        textureScale: str,
    ):
        if textureScrollVar not in self.initVariables:
            self.initVariables[textureScrollVar] = 0.0
            self.calculatedVariables[textureScrollVar] = 0.0
        if textureScrollRate not in self.initVariables:
            self.initVariables[textureScrollRate] = 0.0
            self.calculatedVariables[textureScrollRate] = 0.0
        if textureScrollAngle not in self.initVariables:
            self.initVariables[textureScrollAngle] = 0.0
            self.calculatedVariables[textureScrollAngle] = 0.0
        if textureScale not in self.initVariables:
            self.initVariables[textureScale] = 0.0
            self.calculatedVariables[textureScale] = 0.0
        self.content += f'\tTextureScroll\n\t{{\n\t\ttextureScrollVar\t"${textureScrollVar}"\n\t\ttextureScrollRate\t"${textureScrollRate}"\n\t\ttextureScrollAngle\t"${textureScrollAngle}"\n\t\ttextureScale\t"${textureScale}"\n\t}}\n'

    def LampBeam(self):
        self.content += f"\tLampBeam\n\t{{\n\t}}\n"

    def LampHalo(self):
        self.content += f"\tLampHalo\n\t{{\n\t}}\n"

    def CustomSteamImageOnModel(self):
        self.content += f"\tCustomSteamImageOnModel\n\t{{\n\t}}\n"

    # Entity integration
    def MaterialModify(self):
        self.content += f"\tMaterialModify\n\t{{\n\t}}\n"

    def MaterialModifyAnimated(self):
        self.content += f"\tMaterialModify\n\t{{\n\t}}\n"

    def WaterLOD(self, CHEAPWATERSTARTDISTANCE: str, CHEAPWATERENDDISTANCE: str):
        if CHEAPWATERENDDISTANCE not in self.initVariables:
            self.initVariables[CHEAPWATERENDDISTANCE] = 0.0
            self.calculatedVariables[CHEAPWATERENDDISTANCE] = 0.0
        if CHEAPWATERSTARTDISTANCE not in self.initVariables:
            self.initVariables[CHEAPWATERSTARTDISTANCE] = 0.0
            self.calculatedVariables[CHEAPWATERSTARTDISTANCE] = 0.0
        self.content += f'\tWaterLOD\n\t{{\n\t\t$CHEAPWATERSTARTDISTANCE\t"${CHEAPWATERSTARTDISTANCE}"\n\t\t$CHEAPWATERENDDISTANCE\t"${CHEAPWATERENDDISTANCE}"\n\t}}\n'

    def ConVar(self, convar: str, resultVar: str):
        """获取一个控制台变量值

        Args:
            convar (str): 目标控制台变量
            resultVar (str): 存储该控制台变量值的变量
        """
        if resultVar not in self.initVariables:
            self.initVariables[resultVar] = 0.0
            self.calculatedVariables[resultVar] = 0.0
        self.content += f'\tConVar\n\t{{\n\t\tconvar\t"${convar}"\n\t\tresultVar\t"${resultVar}"\n\t}}\n'

    # 生成结果
    def build(self):
        self.finalContent = ""
        for key, value in self.initVariables.items():
            self.finalContent += f"${key} = {value}\n"
        self.finalContent += "\nProxies\n{\n" + self.content + "}\n"
        with open("Proxies.txt", "w", encoding="utf-8") as f:
            f.write(self.finalContent)
        print(self.finalContent)
        print("Proxies.txt has been generated.")

    def reverse(self, path: str):
        initialization = True
        inProxy = False
        reversedContent = "from Pyroxies import Proxies\n\nmyProxies = Proxies()\n\n"
        variablePattern = r'\$(\w+)\s+([+-]?\d*\.?\d+|".*?")'
        varialbePatternInProxy = r'"\w+"\s+"([^"]+)"'
        proxiesMethod = [
            "Add",
            "Multiply",
            "Subtract",
            "Divide",
            "Equals",
            "Abs",
            "Frac",
            "Int",
            "Clamp",
            "LessOrEqual",
            "SelectFirstIfNonZero",
            "WrapMinMax",
            "Exponential",
            "Sine",
            "LinearRamp",
            "CurrentTime",
            "UniformNoise",
            "GaussianNoise",
            "MatrixRotate",
            "Alpha",
            "Cycle",
            "PlayerProximity",
            "PlayerTeamMatch",
            "PlayerView",
            "PlayerSpeed",
            "PlayerPosition",
            "EntitySpeed",
            "EntityOrigin",
            "EntityRandom",
            "Health",
            "IsNPC",
            "WorldDims",
            "CrosshairColor",
            "AnimatedTexture",
            "AnimatedEntityTexture",
            "AnimatedOffsetTexture",
            "AnimateSpecificTexture",
            "Pupil",
            "TextureTransform",
            "TextureScroll",
            "LampBeam",
            "LampHalo",
            "CustomSteamImageOnModel",
            "MaterialModify",
            "MaterialModifyAnimated",
            "WaterLOD",
            "ConVar",
        ]
        with open(path, "r", encoding="utf-8") as f:
            self.srcContent = f.read()
        lines = self.srcContent.split("\n")
        # lines = re.sub(r'\s+', ' ', self.srcContent).split("\n")
        for i in range(len(lines)):
            lines[i] = re.sub(r"\s+", " ", lines[i]).strip()
        print(lines)
        for line in lines:
            if "proxies" in line.lower():
                initialization = False
                for name, value in self.initVariables.items():
                    reversedContent += f"{name} = {float(value)}\n"
                reversedContent += "\n"
            if initialization:
                match = re.match(variablePattern, line)
                if match:
                    self.initVariables[match.group(1)] = (
                        match.group(2)[1:-1]
                        if match.group(2).startswith('"')
                        and match.group(2).endswith('"')
                        else float(match.group(2))
                    )
            else:
                if line in proxiesMethod:
                    reversedContent += "myProxies." + line + "("
                    inProxy = True
                elif line.startswith("\"") and line.endswith("\""):
                    if line[1:-1] in proxiesMethod:
                        reversedContent += f"myProxies.{line[1:-1]}("
                        inProxy = True
                        
                if inProxy:
                    matchVar = re.match(varialbePatternInProxy, line)
                    if matchVar:
                        # if matchVar.group(1) in self.initVariables:
                        #     fVar = float(self.initVariables[matchVar.group(1)])
                        # if fVar -0 < 0.001:
                        #     reversedContent += matchVar.group(1) + ", "
                        # else:
                        #     reversedContent += str(fVar) + ", "
                        reversedContent += matchVar.group(1) + ", "
                if inProxy and line == "}":
                    inProxy = False
                    reversedContent = reversedContent[:-2] + ")\n"

            # print(line)
            # print(reversedContent)
        # for i in range(len(lines)):
        #     print(lines[i])
        # print(lines)
        # print(self.initVariables)
        with open(f"{path}.py", "w", encoding="utf-8") as f:
            f.write(reversedContent)
        print("Proxies.txt has been reversed.")


if __name__ == "__main__":
    proxies = Proxies()
    # proxies.Add("a", "b", "c")
    # proxies.Subtract("c", "b", "d")
    # proxies.Multiply("d", "b", "e")
    # proxies.Divide("e", "b", "f")
    # proxies.Equals("f", "g")
    # proxies.Abs("g", "h")
    # proxies.Frac("h", "i")
    # proxies.Int("i", "j")
    # proxies.Clamp("j", "k", "l", "m")
    # proxies.LessOrEqual("m", "n", "o", "p")
    # proxies.SelectFirstIfNonZero("p", "q", "r")
    # proxies.WrapMinMax("r", "s", "t", "u")
    # proxies.Exponential("u", "v", "w", "x", "y", "z")
    # proxies.Sine("z", "aa", "ab", "ac", "ad")
    # proxies.LinearRamp("ad", "ae", "af")
    # proxies.CurrentTime("ag")
    # proxies.UniformNoise("ah", "af", "ai")
    # proxies.GaussianNoise("aj", "ak", "al", "am", "an")
    # proxies.MatrixRotate("ao", "ap", "aq")
    # proxies.Alpha()
    # proxies.Cycle("ar", "as", "at", "au", "av")
    # proxies.PlayerProximity("aw", "ax")

    proxies.reverse("./RNG/EntityRandom_ModelRNG.txt")
    # print(proxies.initVariables)
    # print(proxies.calculatedVariables)
    # proxies.build()
    # try:
    #     threading.Event().wait(10)  # 等待 10 秒
    # finally:
    #     proxies.timer.cancel()
