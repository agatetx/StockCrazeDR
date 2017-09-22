import subprocess
import os
import sys

if sys.version_info >= (3, 0):
    python_cmd = 'python3'
    pip_cmd = 'pip3'
else:
    python_cmd = 'python'
    pip_cmd = 'pip'

def install_python_lib(path):
    #subprocess.call(['pwd'])
    #print(os.path.join(os.path.dirname(os.path.realpath(__file__)),path))
    #subprocess.call(['cd', os.path.join(os.path.dirname(os.path.realpath(__file__)),path), 'sudo', 'python', 'setup.py', 'install'], shell=True)
    prev_dir = os.getcwd()
    os.chdir(path)
    subprocess.call(['sudo', python_cmd, 'setup.py','install'])
    os.chdir(prev_dir)


def install_with_pip(pkg_name):
    subprocess.call(['sudo', pip_cmd, 'install', pkg_name])


if __name__ == '__main__':
    install_python_lib('third_party/yahoo-finance')
    install_python_lib('third_party/googlefinance')
    install_with_pip('demjson')
    install_with_pip('realtime-stock')
