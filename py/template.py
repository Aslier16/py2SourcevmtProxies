from Py2Proxies.Pyroxies import Proxies
import time

myProxies = Proxies()

# frequency 为模拟的时间间隔，单位为秒
def proxy(myProxies: Proxies, frequency: int = 1):
    # ====================书写proxies=======================

    # ======================================================
    myProxies.time += frequency

if __name__ == "__main__":
    start_time = time.time()
    while time.time() - start_time <= 10:
        proxy(myProxies, 1)
        time.sleep(1)
        # 查看每隔frequency秒，指定变量的值
        # print("xxx: ", myProxies.calculatedVariables["变量名"])

    # 引号内填入输出到的txt路径，如"Proxies.txt"，不填则默认输出到当前路径下的Proxies.txt
    myProxies.build(f"{__file__}.txt")