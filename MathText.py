from manimlib import *
from datetime import datetime

# 这个案例能充分的体现 MamimGL 和 ManimCE 的区别
# https://docs.manim.community/en/stable/guides/using_text.html
class MathTex(Scene):
    def construct(self) -> None:
        dt = datetime.now()
        solar_day = dt.strftime('%Y年%m月%d日')
        print(solar_day)
        text_solar_day = Title(solar_day, include_underline=False)
        text_solar_day.move_to(DR)
        # tex1 = Tex(r"$\int_a^b f'(x) dx = f(b)- f(a)$")  # r表示raw string
        tex1 = Tex(r"\int_a^b f'(x) dx = f(b)- f(a)")  # r表示raw string
        # tex1 = Tex(r"123")  # r表示raw string
        # tex2 = Tex(r'Hello \LaTeX')
        # tex3 = MathTex(r"\int_a^b f'(x) dx = f(b)- f(a)")
        tex3 = TexText("$\int_a^b f'(x) dx = f(b)- f(a)$")
        # equation = MathTex(r"e^x = x^0 + x^1 + \frac{1}{2} x^2 + \frac{1}{6} x^3 + \cdots + \frac{1}{n!} x^n + \cdots",
        #                    substrings_to_isolate="x")
        # equation.set_color_by_tex("x", YELLOW)
        equation = TexText("$e^x = x^0 + x^1 + \\frac{1}{2} x^2 + \\frac{1}{6} x^3 + \cdots + \\frac{1}{n!} x^n + \cdots$")
        equation.set_color_by_tex("x", YELLOW)
        tex3.to_edge(DOWN)
        equation.to_edge(UL)
        self.add(text_solar_day,tex1,tex3,equation)