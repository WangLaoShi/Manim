# Manim

## 1. 安装

```shell
# 通过 pip 安装 manimgl
pip install manimgl

# 配置运行参数，可选
manimgl --config  # 如果想要在 LaTeX 中使用中文，请选择 xelatex 选项

# 测试一下
manimgl
```

## FAQ

1. Failed to build manimpango
   ERROR: Could not build wheels for manimpango, which is required to install pyproject.toml-based projects

解决办法：https://github.com/ManimCommunity/manimpango#linuxmacos

先执行：`brew install pango pkg-config` 然后再执行 `pip install manimpango`

2. ValueError: operands could not be broadcast together with shapes (24,3) (0,3)

解决办法：https://github.com/3b1b/manim/issues/2050#issuecomment-1791948441

3. ERROR LaTeX Error! Not a worry, it happens to the best of us.

解决办法：2.  安装 [MacTex](https://www.tug.org/mactex/)

你可以选择进入上面链接手动安装，也可使用 brew cask 安装

```shell
brew install --cask mactex-no-gui
```

installer: Package name is MacTeX
installer: choices changes file '/private/tmp/choices20240704-14184-e6zadn.xml' applied
installer: Installing at base path /
installer: The install was successful.
🍺  mactex-no-gui was successfully installed!


4. Python 中的 ffmpeg 的名称为 `ffmpeg-python` 应该这样安装 `pip install ffmpeg-python`
