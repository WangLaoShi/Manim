from manimlib import *

class TextExample(Scene):
   def construct(self):
      text = Text('ABCDEABCDE', font='Microsoft YaHei UI',
                  t2c={'[:1]': RED, '[5:6]': YELLOW},
                  t2f={'B': 'Microsoft YaHei UI'},
                  t2g={'C': BLUE},
                  t2s={'D': ITALIC},
                  t2w={'D': BOLD})
      mtext = MarkupText('<span foreground="red" underline="double">foo</span> <span underline="error">bar</span> <s>remove</s>')
      mtext.next_to(text, DOWN)
      self.add(text, mtext)