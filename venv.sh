#!/bin/sh
# 注释-编写批处理，生成环境并安装 Python 需要的各种库

# 区分操作系统
# Windows
# Linux
# MacOS
brew install virtualenv
# 创建虚拟环境
virtualenv manim_venv --python=python3.9

# 激活虚拟环境
source manim_venv/bin/activate

# 安装依赖库
pip install -r requirements.txt



