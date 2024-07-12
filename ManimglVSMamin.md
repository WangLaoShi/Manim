# Manimgl VS ManimCE

I also just started learning Manim with the GL version. I have both version but never used ManimCE and I have no conflict for now.

you can get manimGL examples on this channel (and his github) : https://www.youtube.com/channel/UCMUR4wag0L2aamwuJMDmktQ


I use manim gl since it gives a preview of the video without saving it as a .mp4 format unlike manim CE.

This is the only reason, otherwise manim CE is well documented.

[更详细的对比](https://dianyao.co/manim/1.%E5%9F%BA%E6%9C%AC%E4%BD%BF%E7%94%A8/Manim%E4%BB%8B%E7%BB%8D%E5%8F%8A%E5%AE%89%E8%A3%85.html)

**（1）Manim简介及版本**

Manim原先是由Grant Sanderson开发的一个动画引擎，用在他的Youtube频道[3Blue1Brown - YouTube](https://www.youtube.com/channel/UCYO_jab_esuFRV4b17AJtAw)，旨在用动画直观解释数学的一些问题。随着他的YouTube频道变得流行，其他开发者也想用Manim来开发，于是有了社区版。目前Manim有如下版本（详情见[Differences between Manim Versions](https://docs.manim.community/en/stable/installation/versions.html)）：

* ManimCE: The community edition of manim, named [manim](https://pypi.org/project/manim/) on pip.
* [ManimGL](https://github.com/3b1b/manim): The current version of manim that is used by 3blue1brown. It supports OpenGL rendering and interactivity, and is named `manimgl` on pip. You can find documentation for it [here](https://3b1b.github.io/manim/index.html).
* [ManimCairo](https://github.com/3b1b/manim/tree/cairo-backend): The old version of manim originally used by 3blue1brown. It is not available on pip.

**（2）选用哪个版本**

总体上，两者文档都很易读。ManimGL渲染更快，Manim社区版，提供[Jupyter Notebooks ](https://docs.manim.community/en/stable/installation/jupyter.html)，声称更稳定。Manim社区版说2021年4月会全部支持OpenGL。