import re
import math
from typing import Union
import random


class Proxies:
    def __init__(self):
        self.initialVariables = {}
        self.calculatedVariables = {}
        self.content = ""
        self._time = 0
        self.firstTime = True
        self.deltaTime = 0

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        if value > 0:
            self.firstTime = False
        self.deltaTime = value - self._time
        self._time = value

    def initVariables(self, variables: Union[str, list]):
        try:
            if isinstance(variables, list):
                if variables[0] not in self.initialVariables:
                    self.initialVariables[variables[0]] = variables[1]
                    self.calculatedVariables[variables[0]] = variables[1]
                    variables = variables[0]
                    return variables
                else:
                    return variables[0]
            elif isinstance(variables, str):
                if variables not in self.initialVariables:
                    self.initialVariables[variables] = 0.0
                    self.calculatedVariables[variables] = 0.0
                    return variables
                else:
                    return variables
        except Exception:
            print("initVariables error")

    # 四则运算
    def Add(
        self,
        srcVar1: Union[str, list],
        srcVar2: Union[str, list],
        resultVar: Union[str, list],
    ):
        """加法
        resultVar = srcVar1 + srcVar2

        Args:
            srcVar1 (str): 加数1
            srcVar2 (str): 加数2
            resultVar (str): 存储结果的变量
        """
        srcVar1 = self.initVariables(srcVar1)
        srcVar2 = self.initVariables(srcVar2)
        resultVar = self.initVariables(resultVar)
        if self.firstTime:
            self.content += f'\tAdd\n\t{{\n\t\tsrcVar1\t"${srcVar1}"\n\t\tsrcVar2\t"${srcVar2}"\n\t\tresultVar\t"${resultVar}"\n\t}}\n'

        try:
            self.calculatedVariables[resultVar] = (
                self.calculatedVariables[srcVar1] + self.calculatedVariables[srcVar2]
            )
        except Exception:
            print("Add error")

    def Subtract(
        self,
        srcVar1: Union[str, list],
        srcVar2: Union[str, list],
        resultVar: Union[str, list],
    ):
        """减法
        resultVar = srcVar1 - srcVar2

        Args:
            srcVar1 (str): 被减数
            srcVar2 (str): 减数
            resultVar (str): 存储结果的变量
        """
        srcVar1 = self.initVariables(srcVar1)
        srcVar2 = self.initVariables(srcVar2)
        resultVar = self.initVariables(resultVar)
        if self.firstTime:
            self.content += f'\tSubtract\n\t{{\n\t\tsrcVar1\t"${srcVar1}"\n\t\tsrcVar2\t"${srcVar2}"\n\t\tresultVar\t"${resultVar}"\n\t}}\n'

        try:
            self.calculatedVariables[resultVar] = (
                self.calculatedVariables[srcVar1] - self.calculatedVariables[srcVar2]
            )
        except Exception:
            pass

    def Multiply(
        self,
        srcVar1: Union[str, list],
        srcVar2: Union[str, list],
        resultVar: Union[str, list],
    ):
        """乘法
        resultVar = srcVar1 * srcVar2

        Args:
            srcVar1 (str): 乘数1
            srcVar2 (str): 乘数2
            resultVar (str): 存储结果的变量
        """
        srcVar1 = self.initVariables(srcVar1)
        srcVar2 = self.initVariables(srcVar2)
        resultVar = self.initVariables(resultVar)
        if self.firstTime:
            self.content += f'\tMultiply\n\t{{\n\t\tsrcVar1\t"${srcVar1}"\n\t\tsrcVar2\t"${srcVar2}"\n\t\tresultVar\t"${resultVar}"\n\t}}\n'

        try:
            self.calculatedVariables[resultVar] = (
                self.calculatedVariables[srcVar1] * self.calculatedVariables[srcVar2]
            )
        except Exception:
            pass

    def Divide(
        self,
        srcVar1: Union[str, list],
        srcVar2: Union[str, list],
        resultVar: Union[str, list],
    ):
        """除法
        resultVar = srcVar1 / srcVar2

        Args:
            srcVar1 (str): 被除数
            srcVar2 (str): 除数
            resultVar (str): 存储结果的变量
        """
        srcVar1 = self.initVariables(srcVar1)
        srcVar2 = self.initVariables(srcVar2)
        resultVar = self.initVariables(resultVar)
        if self.firstTime:
            self.content += f'\tDivide\n\t{{\n\t\tsrcVar1\t"${srcVar1}"\n\t\tsrcVar2\t"${srcVar2}"\n\t\tresultVar\t"${resultVar}"\n\t}}\n'

        try:
            self.calculatedVariables[resultVar] = (
                self.calculatedVariables[srcVar1] / self.calculatedVariables[srcVar2]
            )
        except Exception:
            pass

    def Equals(self, srcVar1: Union[str, list], resultVar: Union[str, list]):
        """赋值
        resultVar = srcVar1

        Args:
            srcVar1 (str): 源变量
            resultVar (str): 存储结果的变量
        """
        srcVar1 = self.initVariables(srcVar1)
        resultVar = self.initVariables(resultVar)
        if self.firstTime:
            self.content += f'\tEquals\n\t{{\n\t\tsrcVar1\t"${srcVar1}"\n\t\tresultVar\t"${resultVar}"\n\t}}\n'

        try:
            self.calculatedVariables[resultVar] = self.calculatedVariables[srcVar1]
        except Exception:
            pass

    def Abs(self, srcVar1: Union[str, list], resultVar: Union[str, list]):
        """取绝对值
        resultVar = abs(srcVar1)

        Args:
            srcVar1 (str): 源变量
            resultVar (str): 存储结果的变量
        """
        srcVar1 = self.initVariables(srcVar1)
        resultVar = self.initVariables(resultVar)
        if self.firstTime:
            self.content += f'\tAbs\n\t{{\n\t\tsrcVar1\t"${srcVar1}"\n\t\tresultVar\t"${resultVar}"\n\t}}\n'

        try:
            self.calculatedVariables[resultVar] = abs(self.calculatedVariables[srcVar1])
        except Exception:
            pass

    def Frac(self, srcVar1: Union[str, list], resultVar: Union[str, list]):
        """取小数
        resultVar = srcVar1 - int(srcVar1)

        Args:
            srcVar1 (str): 源变量
            resultVar (str): 存储结果的变量
        """
        srcVar1 = self.initVariables(srcVar1)
        resultVar = self.initVariables(resultVar)
        if self.firstTime:
            self.content += f'\tFrac\n\t{{\n\t\tsrcVar1\t"${srcVar1}"\n\t\tresultVar\t"${resultVar}"\n\t}}\n'

        try:
            self.calculatedVariables[resultVar] = self.calculatedVariables[
                srcVar1
            ] - int(self.calculatedVariables[srcVar1])
        except Exception:
            pass

    def Int(self, srcVar1: Union[str, list], resultVar: Union[str, list]):
        """取整
        resultVar = int(srcVar1)
        Args:
            srcVar1 (str): 源变量
            resultVar (str): 存储结果的变量
        """
        srcVar1 = self.initVariables(srcVar1)
        resultVar = self.initVariables(resultVar)
        if self.firstTime:
            self.content += f'\tInt\n\t{{\n\t\tsrcVar1\t"${srcVar1}"\n\t\tresultVar\t"${resultVar}"\n\t}}\n'

        try:
            self.calculatedVariables[resultVar] = int(self.calculatedVariables[srcVar1])
        except Exception:
            pass

    def Clamp(
        self,
        min: Union[str, list],
        max: Union[str, list],
        srcVar1: Union[str, list],
        resultVar: Union[str, list],
    ):
        """限制变量的取值范围

        Args:
            min (str): 最小值
            max (str): 最大值
            srcVar1 (str): 数值源变量
            resultVar (str): 存储限制后值的变量
        """
        min = self.initVariables(min)
        max = self.initVariables(max)
        srcVar1 = self.initVariables(srcVar1)
        resultVar = self.initVariables(resultVar)
        if self.firstTime:
            self.content += f'\tClamp\n\t{{\n\t\tmin\t"${min}"\n\t\tmax\t"${max}"\n\t\tsrcVar1\t"${srcVar1}"\n\t\tresultVar\t"${resultVar}"\n\t}}\n'

        try:
            self.calculatedVariables[resultVar] = max(
                self.calculatedVariables[min],
                min(self.calculatedVariables[max], self.calculatedVariables[srcVar1]),
            )
        except Exception:
            pass

    def LessOrEqual(
        self,
        lessEqualVar: Union[str, list],
        greaterVar: Union[str, list],
        srcVar1: Union[str, list],
        srcVar2: Union[str, list],
        resultVar: Union[str, list],
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
        lessEqualVar = self.initVariables(lessEqualVar)
        greaterVar = self.initVariables(greaterVar)
        srcVar1 = self.initVariables(srcVar1)
        srcVar2 = self.initVariables(srcVar2)
        resultVar = self.initVariables(resultVar)
        if self.firstTime:
            self.content += f'\tLessOrEqual\n\t{{\n\t\tlessEqualVar\t"${lessEqualVar}"\n\t\tgreaterVar\t"${greaterVar}"\n\t\tsrcVar1\t"${srcVar1}"\n\t\tsrcVar2\t"${srcVar2}"\n\t\tresultVar\t"${resultVar}"\n\t}}\n'

        try:
            if self.calculatedVariables[srcVar1] <= self.calculatedVariables[srcVar2]:
                self.calculatedVariables[resultVar] = self.calculatedVariables[
                    lessEqualVar
                ]
            else:
                self.calculatedVariables[resultVar] = self.calculatedVariables[
                    greaterVar
                ]
        except Exception as e:
            print("LessOrEqual error: ", e)

    def SelectFirstIfNonZero(
        self,
        srcVar1: Union[str, list],
        srcVar2: Union[str, list],
        resultVar: Union[str, list],
    ):
        srcVar1 = self.initVariables(srcVar1)
        srcVar2 = self.initVariables(srcVar2)
        resultVar = self.initVariables(resultVar)
        if self.firstTime:
            self.content += f'\tSelectFirstIfNonZero\n\t{{\n\t\tsrcVar1\t"${srcVar1}"\n\t\tsrcVar2\t"${srcVar2}"\n\t\tresultVar\t"${resultVar}"\n\t}}\n'

        try:
            if self.calculatedVariables[srcVar1] != 0:
                self.calculatedVariables[resultVar] = self.calculatedVariables[srcVar1]
            else:
                self.calculatedVariables[resultVar] = self.calculatedVariables[srcVar2]
        except Exception:
            pass

    def WrapMinMax(
        self,
        srcVar1: Union[str, list],
        min: Union[str, list],
        max: Union[str, list],
        resultVar: Union[str, list],
    ):
        srcVar1 = self.initVariables(srcVar1)
        min = self.initVariables(min)
        max = self.initVariables(max)
        resultVar = self.initVariables(resultVar)
        if self.firstTime:
            self.content += f'\tWrapMinMax\n\t{{\n\t\tsrcVar1\t"${srcVar1}"\n\t\tmin\t"${min}"\n\t\tmax\t"${max}"\n\t\tresultVar\t"${resultVar}"\n\t}}\n'

    def Exponential(
        self,
        minVal: Union[str, list],
        maxVal: Union[str, list],
        srcVar1: Union[str, list],
        offset: Union[str, list],
        scale: Union[str, list],
        resultVar: Union[str, list],
    ):
        minVal = self.initVariables(minVal)
        maxVal = self.initVariables(maxVal)
        srcVar1 = self.initVariables(srcVar1)
        offset = self.initVariables(offset)
        scale = self.initVariables(scale)
        resultVar = self.initVariables(resultVar)
        if self.firstTime:
            self.content += f'\tExponential\n\t{{\n\t\tminVal\t"${minVal}"\n\t\tmaxVal\t"${maxVal}"\n\t\tsrcVar1\t"${srcVar1}"\n\t\toffset\t"${offset}"\n\t\tscale\t"${scale}"\n\t\tresultVar\t"${resultVar}"\n\t}}\n'

    # 数值生成
    def Sine(
        self,
        sineperiod: Union[str, list],
        sinemin: Union[str, list],
        sinemax: Union[str, list],
        timeoffset: Union[str, list],
        resultVar: Union[str, list],
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
        sineperiod = self.initVariables(sineperiod)
        sinemin = self.initVariables(sinemin)
        sinemax = self.initVariables(sinemax)
        timeoffset = self.initVariables(timeoffset)
        resultVar = self.initVariables(resultVar)
        if self.firstTime:
            self.content += f'\tSine\n\t{{\n\t\tsineperiod\t"${sineperiod}"\n\t\tsinemin\t"${sinemin}"\n\t\tsinemax\t"${sinemax}"\n\t\ttimeoffset\t"${timeoffset}"\n\t\tresultVar\t"${resultVar}"\n\t}}\n'

        self.calculatedVariables[resultVar] = self.calculatedVariables[sinemin] + (
            self.calculatedVariables[sinemax] - self.calculatedVariables[sinemin]
        )/2 * (1+math.sin(
            2 * math.pi * self.time / self.calculatedVariables[sineperiod]
            + self.calculatedVariables[timeoffset])
        )

    def LinearRamp(
        self,
        rate: Union[str, list],
        initialValue: Union[str, list],
        resultVar: Union[str, list],
    ):
        """线性函数
        resultVar = initialValue + rate * time

        Args:
            rate (str): 斜率/增长速率
            initialValue (str): 初始值
            resultVar (str): 存储结果的变量
        """
        rate = self.initVariables(rate)
        initialValue = self.initVariables(initialValue)
        resultVar = self.initVariables(resultVar)
        if self.firstTime:
            self.content += f'\tLinearRamp\n\t{{\n\t\trate\t"${rate}"\n\t\tinitialValue\t"${initialValue}"\n\t\tresultVar\t"${resultVar}"\n\t}}\n'
        try:
            self.calculatedVariables[resultVar] = (
                self.calculatedVariables[rate] * self.deltaTime
                + self.calculatedVariables[initialValue]
            )
            self.calculatedVariables[initialValue] = self.calculatedVariables[resultVar]
        except Exception as e:
            print("LinearRamp error: ", e)

    def CurrentTime(self, resultVar: Union[str, list]):
        """获取当前地图时间

        Args:
            resultVar (str): 存储时间的变量
        """
        resultVar = self.initVariables(resultVar)
        if self.firstTime:
            self.content += (
                f'\tCurrentTime\n\t{{\n\t\tresultVar\t"${resultVar}"\n\t}}\n'
            )
        try:
            self.calculatedVariables[resultVar] = self.time
        except Exception as e:
            print("CurrentTime error:", e)

    def UniformNoise(
        self,
        minVal: Union[str, list],
        maxVal: Union[str, list],
        resultVar: Union[str, list],
    ):
        """生成均匀分布噪声, 生成范围[minVal, maxVal]

        Args:
            minVal (str): 最小值
            maxVal (str): 最大值
            resultVar (str): 存储结果的变量
        """
        minVal = self.initVariables(minVal)
        maxVal = self.initVariables(maxVal)
        resultVar = self.initVariables(resultVar)
        if self.firstTime:
            self.content += f'\tUniformNoise\n\t{{\n\t\tminVal\t"${minVal}"\n\t\tmaxVal\t"${maxVal}"\n\t\tresultVar\t"${resultVar}"\n\t}}\n'
        try:
            self.calculatedVariables[resultVar] = random.uniform(
                self.calculatedVariables[minVal], self.calculatedVariables[maxVal]
            )
        except Exception as e:
            print("UniformNoise error:", e)

    def GaussianNoise(
        self,
        mean: Union[str, list],
        halfWidth: Union[str, list],
        minVal: Union[str, list],
        maxVal: Union[str, list],
        resultVar: Union[str, list],
    ):
        mean = self.initVariables(mean)
        halfWidth = self.initVariables(halfWidth)
        minVal = self.initVariables(minVal)
        maxVal = self.initVariables(maxVal)
        resultVar = self.initVariables(resultVar)
        if self.firstTime:
            self.content += f'\tGaussianNoise\n\t{{\n\t\tmean\t"${mean}"\n\t\thalfWidth\t"${halfWidth}"\n\t\tminVal\t"${minVal}"\n\t\tmaxVal\t"${maxVal}"\n\t\tresultVar\t"${resultVar}"\n\t}}\n'

    def MatrixRotate(
        self,
        axisVar: Union[str, list],
        angle: Union[str, list],
        resultVar: Union[str, list],
    ):
        axisVar = self.initVariables(axisVar)
        angle = self.initVariables(angle)
        resultVar = self.initVariables(resultVar)
        if self.firstTime:
            self.content += f'\tMatrixRotate\n\t{{\n\t\taxisVar\t"${axisVar}"\n\t\tangle\t"${angle}"\n\t\tresultVar\t"${resultVar}"\n\t}}\n'

    # 实体数据获取
    def Alpha(self):
        self.content += f"\tAlpha\n\t{{\n\t\t$alpha\n\t}}\n"

    def Cycle(
        self,
        start: Union[str, list],
        end: Union[str, list],
        easein: Union[str, list],
        easeout: Union[str, list],
        resultVar: Union[str, list],
    ):
        start = self.initVariables(start)
        end = self.initVariables(end)
        easein = self.initVariables(easein)
        easeout = self.initVariables(easeout)
        resultVar = self.initVariables(resultVar)
        if self.firstTime:
            self.content += f'\tCycle\n\t{{\n\t\tstart\t"${start}"\n\t\tend\t"${end}"\n\t\teasein\t"${easein}"\n\t\teaseout\t"${easeout}"\n\t\tresultVar\t"${resultVar}"\n\t}}\n'

    def PlayerProximity(self, scale: Union[str, list], resultVar: Union[str, list]):
        """获取实体与玩家的距离

        Args:
            scale (str): 数值缩放
            resultVar (str): 存储缩放后结果的变量
        """
        scale = self.initVariables(scale)
        resultVar = self.initVariables(resultVar)
        if self.firstTime:
            self.content += f'\tPlayerProximity\n\t{{\n\t\tscale\t"${scale}"\n\t\tresultVar\t"${resultVar}"\n\t}}\n'

    def PlayerTeamMatch(self, resultVar: Union[str, list]):
        resultVar = self.initVariables(resultVar)
        if self.firstTime:
            self.content += (
                f'\tPlayerTeamMatch\n\t{{\n\t\tresultVar\t"${resultVar}"\n\t}}\n'
            )

    def PlayerView(self, resultVar: Union[str, list]):
        resultVar = self.initVariables(resultVar)
        if self.firstTime:
            self.content += f'\tPlayerView\n\t{{\n\t\tresultVar\t"${resultVar}"\n\t}}\n'

    def PlayerSpeed(self, scale: Union[str, list], resultVar: Union[str, list]):
        """获取玩家速度

        Args:
            scale (str): 数值缩放(=1时玩家最大行走速度为220)
            resultVar (str): 存储缩放后速度的变量
        """
        scale = self.initVariables(scale)
        resultVar = self.initVariables(resultVar)
        if self.firstTime:
            self.content += f'\tPlayerSpeed\n\t{{\n\t\tscale\t"${scale}"\n\t\tresultVar\t"${resultVar}"\n\t}}\n'

    def PlayerPosition(self, scale: Union[str, list], resultVar: Union[str, list]):
        scale = self.initVariables(scale)
        resultVar = self.initVariables(resultVar)
        if self.firstTime:
            self.content += f'\tPlayerPosition\n\t{{\n\t\tscale\t"${scale}"\n\t\tresultVar\t"${resultVar}"\n\t}}\n'

    def EntitySpeed(self, resultVar: Union[str, list]):
        resultVar = self.initVariables(resultVar)
        if self.firstTime:
            self.content += f'\tEntitySpeed\n\t{{\n\t\tresultVar\t"${resultVar}"\n\t}}\n'

    def EntityOrigin(self):
        if self.firstTime:
            self.content += f"\tEntityOrigin\n\t{{\n\t\t$entityorigin}}\n"

    def EntityRandom(self, scale: Union[str, list], resultVar: Union[str, list]):
        """生成一个绑定实体的随机数

        Args:
            scale (str): 数值缩放
            resultVar (str): 存储缩放后结果的变量
        """
        scale = self.initVariables(scale)
        resultVar = self.initVariables(resultVar)
        if self.firstTime:
            self.content += f'\tEntityRandom\n\t{{\n\t\tscale\t"${scale}"\n\t\tresultVar\t"${resultVar}"\n\t}}\n'
            self.calculatedVariables[resultVar] = random.uniform(
                0, self.calculatedVariables[scale]
            )

    def Health(self, scale: Union[str, list], resultVar: Union[str, list]):
        scale = self.initVariables(scale)
        resultVar = self.initVariables(resultVar)
        if self.firstTime:
            self.content += f'\tHealth\n\t{{\n\t\tscale\t"${scale}"\n\t\tresultVar\t"${resultVar}"\n\t}}\n'

    def IsNPC(self, scale: Union[str, list], resultVar: Union[str, list]):
        scale = self.initVariables(scale)
        resultVar = self.initVariables(resultVar)
        if self.firstTime:
            self.content += f'\tIsNPC\n\t{{\n\t\tscale\t"${scale}"\n\t\tresultVar\t"${resultVar}"\n\t}}\n'

    def WorldDims(self):
        if self.firstTime:
            self.content += f"\tWorldDims\n\t{{\n\t\t$world_mins\n\t\t$world_maxs}}\n"

    def CrosshariColor(self, resultVar: Union[str, list]):
        resultVar = self.initVariables(resultVar)
        if self.firstTime:
            self.content += f'\tCrosshariColor\n\t{{\n\t\tresultVar\t"${resultVar}"\n\t}}\n'

    # 贴图操纵 Texture manipulation
    def AnimatedTexture(
        self,
        animatedtexturevar: Union[str, list],
        animatedtextureframenumvar: Union[str, list],
        animatedtextureframerate: Union[str, list],
    ):
        """贴图播放

        Args:
            animatedtexturevar (str): 要播放的贴图路径变量
            animatedtextureframenumvar (str): 控制帧数的变量
            animatedtextureframerate (str): 帧率常量
        """
        animatedtexturevar = self.initVariables(animatedtexturevar)
        animatedtextureframenumvar = self.initVariables(animatedtextureframenumvar)
        animatedtextureframerate = self.initVariables(animatedtextureframerate)
        if self.firstTime:
            self.content += f'\tAnimatedTexture\n\t{{\n\t\tanimatedtexturevar\t"${animatedtexturevar}"\n\t\tanimatedtextureframenumvar\t"${animatedtextureframenumvar}"\n\t\tanimatedtextureframerate\t"${animatedtextureframerate}"\n\t}}\n'

    def AnimatedEntityTexture(
        self,
        animatedtexturevar: Union[str, list],
        animatedtextureframenumvar: Union[str, list],
        animatedtextureframerate: Union[str, list],
    ):
        animatedtexturevar = self.initVariables(animatedtexturevar)
        animatedtextureframenumvar = self.initVariables(animatedtextureframenumvar)
        animatedtextureframerate = self.initVariables(animatedtextureframerate)
        if self.firstTime:
            self.content += f'\tAnimatedEntityTexture\n\t{{\n\t\tanimatedtexturevar\t"${animatedtexturevar}"\n\t\tanimatedtextureframenumvar\t"${animatedtextureframenumvar}"\n\t\tanimatedtextureframerate\t"${animatedtextureframerate}"\n\t}}\n'

    def AnimatedOffsetTexture(
        self,
        animatedtexturevar: Union[str, list],
        animatedtextureframenumvar: Union[str, list],
        animatedtextureframerate: Union[str, list],
    ):
        animatedtexturevar = self.initVariables(animatedtexturevar)
        animatedtextureframenumvar = self.initVariables(animatedtextureframenumvar)
        animatedtextureframerate = self.initVariables(animatedtextureframerate)
        if self.firstTime:
            self.content += f'\tAnimatedOffsetTexture\n\t{{\n\t\tanimatedtexturevar\t"${animatedtexturevar}"\n\t\tanimatedtextureframenumvar\t"${animatedtextureframenumvar}"\n\t\tanimatedtextureframerate\t"${animatedtextureframerate}"\n\t}}\n'

    def AnimateSpecificTexture(
        self,
        animatedtexturevar: Union[str, list],
        animatedtextureframenumvar: Union[str, list],
        animatedtextureframerate: Union[str, list],
        onlyAnimateOnTexture: Union[str, list],
    ):
        animatedtexturevar = self.initVariables(animatedtexturevar)
        animatedtextureframenumvar = self.initVariables(animatedtextureframenumvar)
        animatedtextureframerate = self.initVariables(animatedtextureframerate)
        onlyAnimateOnTexture = self.initVariables(onlyAnimateOnTexture)
        if self.firstTime:
            self.content += f'\tAnimateSpecificTexture\n\t{{\n\t\tanimatedtexturevar\t"${animatedtexturevar}"\n\t\tanimatedtextureframenumvar\t"${animatedtextureframenumvar}"\n\t\tanimatedtextureframerate\t"${animatedtextureframerate}"\n\t\tonlyAnimateOnTexture\t"${onlyAnimateOnTexture}"\n\t}}\n'

    def Pupil(
        self,
        TextureVar: Union[str, list],
        TextureFrameNumVar: Union[str, list],
        PupilCloseRate: Union[str, list],
        PupilOpenRate: Union[str, list],
    ):
        TextureVar = self.initVariables(TextureVar)
        TextureFrameNumVar = self.initVariables(TextureFrameNumVar)
        PupilCloseRate = self.initVariables(PupilCloseRate)
        PupilOpenRate = self.initVariables(PupilOpenRate)
        if self.firstTime:
            self.content += f'\tPupil\n\t{{\n\t\tTextureVar\t"${TextureVar}"\n\t\tTextureFrameNumVar\t"${TextureFrameNumVar}"\n\t\tPupilCloseRate\t"${PupilCloseRate}"\n\t\tPupilOpenRate\t"${PupilOpenRate}"\n\t\t$lighting\n\t}}\n'

    def TextureTransform(
        self,
        centerVar: Union[str, list],
        scaleVar: Union[str, list],
        rotateVar: Union[str, list],
        translateVar: Union[str, list],
        resultVar: Union[str, list],
    ):
        centerVar = self.initVariables(centerVar)
        scaleVar = self.initVariables(scaleVar)
        rotateVar = self.initVariables(rotateVar)
        translateVar = self.initVariables(translateVar)
        resultVar = self.initVariables(resultVar)
        if self.firstTime:
            self.content += f'\tTextureTransform\n\t{{\n\t\tcenterVar\t"${centerVar}"\n\t\tscaleVar\t"${scaleVar}"\n\t\trotateVar\t"${rotateVar}"\n\t\ttranslateVar\t"${translateVar}"\n\t\tresultVar\t"${resultVar}"\n\t}}\n'

    def TextureScroll(
        self,
        textureScrollVar: Union[str, list],
        textureScrollRate: Union[str, list],
        textureScrollAngle: Union[str, list],
        textureScale: Union[str, list],
    ):
        textureScrollVar = self.initVariables(textureScrollVar)
        textureScrollRate = self.initVariables(textureScrollRate)
        textureScrollAngle = self.initVariables(textureScrollAngle)
        textureScale = self.initVariables(textureScale)
        if self.firstTime:
            self.content += f'\tTextureScroll\n\t{{\n\t\ttextureScrollVar\t"${textureScrollVar}"\n\t\ttextureScrollRate\t"${textureScrollRate}"\n\t\ttextureScrollAngle\t"${textureScrollAngle}"\n\t\ttextureScale\t"${textureScale}"\n\t}}\n'

    def LampBeam(self):
        if self.firstTime:
            self.content += f"\tLampBeam\n\t{{\n\t}}\n"

    def LampHalo(self):
        if self.firstTime:
            self.content += f"\tLampHalo\n\t{{\n\t}}\n"

    def CustomSteamImageOnModel(self):
        if self.firstTime:
            self.content += f"\tCustomSteamImageOnModel\n\t{{\n\t}}\n"

    # Entity integration
    def MaterialModify(self):
        if self.firstTime:
            self.content += f"\tMaterialModify\n\t{{\n\t}}\n"

    def MaterialModifyAnimated(self):
        if self.firstTime:
            self.content += f"\tMaterialModify\n\t{{\n\t}}\n"

    def WaterLOD(
        self,
        CHEAPWATERSTARTDISTANCE: Union[str, list],
        CHEAPWATERENDDISTANCE: Union[str, list],
    ):
        CHEAPWATERENDDISTANCE = self.initVariables(CHEAPWATERENDDISTANCE)
        CHEAPWATERENDDISTANCE = self.initVariables(CHEAPWATERENDDISTANCE)
        if self.firstTime:
            self.content += f'\tWaterLOD\n\t{{\n\t\t$CHEAPWATERSTARTDISTANCE\t"${CHEAPWATERSTARTDISTANCE}"\n\t\t$CHEAPWATERENDDISTANCE\t"${CHEAPWATERENDDISTANCE}"\n\t}}\n'

    def ConVar(self, convar: Union[str, list], resultVar: Union[str, list]):
        """获取一个控制台变量值

        Args:
            convar (str): 目标控制台变量
            resultVar (str): 存储该控制台变量值的变量
        """
        convar = self.initVariables(convar)
        if self.firstTime:
            self.content += f'\tConVar\n\t{{\n\t\tconvar\t"${convar}"\n\t\tresultVar\t"${resultVar}"\n\t}}\n'

    # 生成结果
    def build(self, path: str = "./Proxies.txt"):
        self.finalContent = ""
        for key, value in self.initialVariables.items():
            self.finalContent += f"${key} {value}\n"
        self.finalContent += "\nProxies\n{\n" + self.content + "}\n"
        with open(path, "w", encoding="utf-8") as f:
            f.write(self.finalContent)
        print(self.finalContent)
        print("Proxies.txt has been generated.")

    def reverse(self, path: str):
        initialization = True
        inProxy = False
        reversedContent = "from Pyroxies import Proxies\n\nmyProxies = Proxies()\n\n"
        variablePattern = r'\$(\w+)\s+([+-]?\d*\.?\d+|".*?")'
        varialbePatternInProxy = r'"\w+"\s+"([^"]+)"'
        varibales = {}
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
        # print(lines)
        for line in lines:
            if "proxies" in line.lower():
                initialization = False
                for name, value in varibales.items():
                    reversedContent += f"{name} = {float(value)}\n"
                reversedContent += "\n"
            if initialization:
                match = re.match(variablePattern, line)
                if match:
                    varibales[match.group(1)] = (
                        match.group(2)[1:-1]
                        if match.group(2).startswith('"')
                        and match.group(2).endswith('"')
                        else float(match.group(2))
                    )
            else:
                if line in proxiesMethod:
                    reversedContent += "myProxies." + line + "("
                    inProxy = True
                elif line.startswith('"') and line.endswith('"'):
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
        print(varibales)
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
    import pathlib

    path = "./RNG"
    for file in pathlib.Path(path).glob("*.txt"):
        proxies.reverse(file)
