from Pyroxies import Proxies
myProxies = Proxies()
# LinearRamp锯齿波循环
myProxies.LinearRamp(["rate", 1.0], "initialVal", "ramp")
myProxies.LessOrEqual(["zero", 0.0],["one",1.0],"ramp",["rampmax", 9.99],"corr")
myProxies.Multiply("corr","rampmax","corrnum")
myProxies.Subtract("initialVal","corrnum","initialVal")

# 根据LinearRamp，周期性的取一个随机数，将其增加到frame中，并且保证frame不超过最大值，超过则进行减法修正循环数值
myProxies.initVariables(["frame", 1000])
myProxies.initVariables(["fh", 500])
myProxies.UniformNoise(["min", 0], ["max", 9.99], "noise")
myProxies.LessOrEqual("frame", "noise", "frame", "fh", "frame")
myProxies.LinearRamp(["rate", 1.0], "initialVal", "ramp")
myProxies.LessOrEqual(["zero", 0.0], ["one", 1.0], "ramp", ["rampmax", 9.99], "corr")
myProxies.Multiply("corr", "rampmax", "corrnum")
myProxies.Subtract("initialVal", "corrnum", "initialVal")
myProxies.Multiply("noise", "corr", "deltaframe")
myProxies.Int("deltaframe", "intdeltaframe")
myProxies.Add("intdeltaframe", "frame", "frame")
myProxies.LessOrEqual(["zero", 0.0], ["one", 1.0], "frame", "max", "framecorr")
myProxies.Multiply("max", "framecorr", "framecorrnum")
myProxies.Subtract("frame", "framecorrnum", "frame")

# 依托Sine值，周期性的取一个随机数
myProxies.UniformNoise(["min", 0], ["max", 3.99], "noise")
myProxies.Sine(["period", 4], ["sinemin", -1.5], ["sinemax", 2.5],["sineoffset", 0], "sine")
myProxies.LessOrEqual(["zero", 0.0], ["one", 1.0], "sine", ["cap", 2.4999], "switch")
myProxies.Multiply("switch", "noise", "Delta")