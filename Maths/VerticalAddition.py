from manimlib import *
class VerticalAdditionWithLine(Scene):
    """
    两个数字的竖式加法
    """

    def addition(self, num1, num2):
        # 将数字转换为字符串并分解为个位和十位
        num1_str = str(num1)
        num2_str = str(num2)

        # 创建每一位的数字对象
        num1_digits = VGroup(*[Text(char) for char in num1_str])
        num2_digits = VGroup(*[Text(char) for char in num2_str])

        # 创建加号、等号和横线
        plus = Text("+")
        equals = Text("=")

        line = Line(LEFT, RIGHT).next_to(num2_digits, DOWN)

        # 创建结果的数字对象
        result = num1 + num2
        result_str = str(result)

        # 定位数字和符号
        num1_digits.arrange(RIGHT, buff=0.5).move_to(UP)
        num2_digits.arrange(RIGHT, buff=0.5).next_to(num1_digits, DOWN, buff=0.5)
        plus.next_to(num2_digits, LEFT, buff=0.5)
        equals.next_to(num2_digits, RIGHT, buff=0.5)

        # 创建大括号
        dot1 = Dot(color=BLUE)
        dot1.next_to(num1_digits, RIGHT, buff=0.5)
        dot2 = Dot(color=RED)
        dot2.next_to(num2_digits, RIGHT, buff=0.5)

        group = VGroup(dot1, dot2)
        brace = Brace(group, RIGHT)
        brace_text = brace.get_text("先进行个位加法").scale(0.6)

        # 显示数字和符号
        self.play(Write(num1_digits))
        self.play(Write(num2_digits))
        self.play(Write(plus))

        # 显示横线
        self.play(ShowCreation(line))
        self.wait(3)

        self.play(ShowCreation(dot1))
        self.play(ShowCreation(dot2))
        self.play(ShowCreation(brace))
        self.play(Write(brace_text))

        self.wait(3)

        # 计算个位的加和及进位
        ones_sum = int(num1_str[1]) + int(num2_str[1])
        carry = ones_sum // 10
        ones_digit = ones_sum % 10
        ones_result = Text(str(ones_digit)).next_to(num2_digits[1], DOWN, buff=1).set_color(YELLOW)

        brace_text2 = brace.get_text(
            f" {num1_str[1]} + {num2_str[1]} =  {ones_sum} \n {'和大于 10，需要进位' if carry > 0 else '和不大于 10，不需要进位'} ").scale(0.6)
        self.play(Transform(brace_text, brace_text2))
        self.wait(3)

        # 计算个位的加和及进位
        if carry > 0:
            carry1 = Text("1").set_color(YELLOW)
            carry1.next_to(num1_digits[0], UP, buff=0.5)
            self.play(Write(carry1))
            self.wait(3)

        # 显示个位的结果
        self.play(Write(ones_result))
        self.remove(dot1,dot2,brace,brace_text,brace_text2)

        dot3 = Dot(color=BLUE)
        dot3.next_to(carry1 if carry > 0 else num1_digits[0], LEFT, buff=0.5)
        dot4 = Dot(color=RED)
        dot4.next_to(num2_digits[0], LEFT, buff=0.5)

        group = VGroup(dot3, dot4)
        brace3 = Brace(group, LEFT)
        brace_text3 = brace3.get_text("再进行十位加法").scale(0.6)
        self.play(ShowCreation(dot3))
        self.play(ShowCreation(dot4))
        self.play(ShowCreation(brace3))
        self.play(Write(brace_text3))
        self.wait(3)


        # 计算十位的加和及进位
        tens_sum = int(num1_str[0]) + int(num2_str[0]) + carry
        tens_digit = Text(str(tens_sum)).next_to(ones_result, LEFT, buff=0.5)

        brace_text4 = brace3.get_text(
            f" {num1_str[0]} + {num2_str[0]} + {carry} =  {tens_sum}   \n " if carry > 0 else f" {num1_str[0]} + {num2_str[0]}  =  {tens_sum}   \n "+
            f"{'和大于 10，需要进位' if tens_sum > 10 else '和不大于 10，不需要进位'} ").scale(0.6)
        self.play(Transform(brace_text3, brace_text4))
        self.wait(3)

        # # 显示十位的结果
        self.play(Write(tens_digit))
        #
        # # 显示最终结果
        # self.play(Write(result_digits))

        self.wait(2)
        # self.embed()

    def construct(self):
        # 定义两个较大数字
        num1 = 76
        num2 = 58
        self.addition(num1, num2)
        self.wait(2)
        self.clear()


        num1 = 23
        num2 = 45
        self.addition(num1, num2)


