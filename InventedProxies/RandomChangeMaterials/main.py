import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from Py2Proxies.Pyroxies import Proxies
import time

myProxies = Proxies()


# frequency 为模拟的时间间隔，单位为秒
def proxy(myProxies: Proxies, frequency: int = 1):
    # ====================书写proxies=======================
    myProxies.initVariables(["Period", 4])
    myProxies.initVariables(["MaterialIndex", 3])

    # myProxies.CurrentTime(["Time", 0])
    myProxies.LinearRamp(["Rate", 0.25], "initialVal", "Ramp")
    myProxies.Subtract("Ramp", ["Rampmax", 3.99], "corrFactorone")
    myProxies.Abs("corrFactorone", "corrFactortwo")
    myProxies.Divide("corrFactorone", "corrFactortwo", "corr")
    myProxies.Clamp(["min", 0.0], ["max", 1.0], "corr", "corr")
    myProxies.Multiply("corr", "Rampmax", "corrnum")
    myProxies.Subtract("initialVal", "corrnum", "initialVal")
    myProxies.Int("Ramp", "CurrentIndex")

    myProxies.Sine(
        "Period", ["SineMin", -2], ["SineMax", 2], ["SineOffset", -1], "Sine"
    )

    myProxies.Subtract("CurrentIndex", "MaterialIndex",  ["Signal_Temp1", 1.0])
    # myProxies.Add("Signal_Temp1", ["p5", 0.5], "Signal_Temp1")
    myProxies.Abs("Signal_Temp1", "Signal_Temp1")
    myProxies.Clamp(["zero", 0], ["one", 1], "Signal_Temp1", "Signal")

    # myProxies.Clamp("SineClampMin", ["SineClampMax", 1], "Sine", "SineClamped")
    # myProxies.Subtract(["one", 1], "Signal", ["ReversedSignal", 0])
    # myProxies.Multiply("SineClamped", "ReversedSignal", "SineModify")
    myProxies.Equals("Sine", ["alpha", 1.0])
    myProxies.Clamp("Signal", ["one", 1], "alpha", "alpha")
    # ======================================================
    myProxies.time += frequency


if __name__ == "__main__":
    start_time = time.time()
    while time.time() - start_time <= 1:
        proxy(myProxies, 1)
        time.sleep(1)
        # 查看每隔frequency秒，指定变量的值
        # print("xxx: ", myProxies.calculatedVariables["变量名"])

    # 引号内填入输出到的txt路径，如"Proxies.txt"，不填则默认输出到当前路径下的Proxies.txt
    myProxies.build(f"{__file__}.txt")
