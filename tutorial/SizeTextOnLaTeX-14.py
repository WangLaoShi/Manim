from manimlib import *
class SizeTextOnLaTeX(Scene):
    def construct(self):
        textHuge = TexText("{\\Huge Huge Text 012.\\#!?} Text")
        texthuge = TexText("{\\huge huge Text 012.\\#!?} Text")
        textLARGE = TexText("{\\LARGE LARGE Text 012.\\#!?} Text")
        textLarge = TexText("{\\Large Large Text 012.\\#!?} Text")
        textlarge = TexText("{\\large large Text 012.\\#!?} Text")
        textNormal = TexText("{\\normalsize normal Text 012.\\#!?} Text")
        textsmall = TexText("{\\small small Text 012.\\#!?} Texto normal")
        textfootnotesize = TexText("{\\footnotesize footnotesize Text 012.\\#!?} Text")
        textscriptsize = TexText("{\\scriptsize scriptsize Text 012.\\#!?} Text")
        texttiny = TexText("{\\tiny tiny Texto 012.\\#!?} Text normal")
        textHuge.to_edge(UP)

        texthuge.next_to(textHuge, DOWN, buff=0.1)
        textLARGE.next_to(texthuge, DOWN, buff=0.1)
        textLarge.next_to(textLARGE, DOWN, buff=0.1)
        textlarge.next_to(textLarge, DOWN, buff=0.1)
        textNormal.next_to(textlarge, DOWN, buff=0.1)
        textsmall.next_to(textNormal, DOWN, buff=0.1)
        textfootnotesize.next_to(textsmall, DOWN, buff=0.1)
        textscriptsize.next_to(textfootnotesize, DOWN, buff=0.1)
        texttiny.next_to(textscriptsize, DOWN, buff=0.1)
        self.add(textHuge, texthuge, textLARGE, textLarge, textlarge, textNormal, textsmall, textfootnotesize,
                 textscriptsize, texttiny)
        self.wait(3)