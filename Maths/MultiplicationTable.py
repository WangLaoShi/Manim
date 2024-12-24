from manimlib import *
class MultiplicationTable(Scene):
    def construct(self):
        # 创建一个 9x9 的表格
        table = VGroup()
        row_spacing = 0.5  # 设置行间距
        col_spacing = 1.6  # 设置列间距

        colors = []
        for i in range(1, 10):
            for j in range(1, i+1):
                colors.append(interpolate_color(BLUE, RED, (i * j) / 45))
        print(len(colors))
        coor = 0
        for i in range(1, 10):
            for j in range(1, i+1):
                product = Text(f"{j} x {i} = {i * j}", font_size=24)
                product.move_to((j - 1) * col_spacing * RIGHT + (i - 1) * row_spacing * DOWN)
                product.set_color(colors[coor])
                coor += 1
                table.add(product)

        # 将表格居中
        table.move_to(ORIGIN)

        # 依次显示表格中的每个元素
        for product in table:
            self.play(Write(product), run_time=0.3)

        self.wait(2)

