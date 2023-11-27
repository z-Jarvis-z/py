import time

def progress_bar():
    print("Starting ... ", end="", flush=True)  # 打印起始文本，不换行
    for i in range(10):  # 模拟进度
        print("=", end="", flush=True)  # 打印进度条，不换行
        time.sleep(0.5)  # 暂停一段时间，模拟程序执行
    print(" Done!")  # 打印结束文本

progress_bar()
