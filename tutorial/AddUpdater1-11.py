from manimlib import *
class AddUpdater1(Scene):
    def construct(self):
        dot = Dot()
        text = TexText("Label").next_to(dot, RIGHT, buff=SMALL_BUFF)

        self.add(dot, text)

        # Update function 更新函数
        def update_text(obj):
            obj.next_to(dot, RIGHT, buff=SMALL_BUFF)

        # Add update function to the objects
        # 把更新函数加给对象
        text.add_updater(update_text)

        # 如果想简洁，lambda 表达式如下：
        # text.add_updater(lambda m: m.next_to(dot, RIGHT, buff=SMALL_BUFF))
        # 此时下面的 remove_updater(update_text)不能继续使用，需要改为 clear_updaters

        # Add the object again 重新加入 text
        # 注意这个步骤不能少，否则看不到！！！
        # 即使之前加入过，现在还是要重新加入
        self.add(text)

        self.play(dot.shift, UP * 2)

        # Remove update function
        text.remove_updater(update_text)

        self.wait()