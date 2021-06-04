import os
import signal
import subprocess

import pytest


@pytest.fixture(scope="module", autouse=True)
def record_vedio():
    # 使用scrcpy录制视频
    command = "scrcpy -r tmp.mp4"
    # 使用command命令
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    print(p)
    yield
    # 录制结束，生成视频,CTRL_C_EVENT是windows系统的属性
    # os.kill(p.pid, signal.CTRL_C_EVENT)
    """
    macos系统的属性是SIG_DFL，参考文档
    https://docs.python.org/3/library/signal.html#module-signal
    """
    # SIGINT是Ctrl+C的名称
    os.kill(p.pid, signal.SIGINT)