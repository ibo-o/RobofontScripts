# menuTitle: Jumpy
# shortCut: control + j

"""
Jumpy
v1.1

This an update version of jumpy script written by Hugues Gentile.
Thanks to Connor Davenport for the help: https://discord.com/channels/1052516637489766411/1390652591528214538/1390710418590273667

"""

import ezui
from mojo.UI import CurrentGlyphWindow

class FontSelectorController(ezui.WindowController):

    def build(self):
        content = """
        |-fonts----| @fontsTable
        |          |
        |----------|
        """
        descriptionData = dict(
            fontsTable=dict(
                items=AllFonts(),
                allowsDragOut=True,
                height=200,
            ),
        )
        self.w = ezui.EZWindow(
            title="Font Selector",
            content=content,
            descriptionData=descriptionData,
            controller=self,
            size=(350, "auto"),
        )

    def started(self):
        self.w.open()

    def fontsTableDoubleClickCallback(self, sender):
        font = sender.getSelectedItems() or None
        if font:            
            font = font[0]
            try:
                currentGlyphName = CurrentGlyph().name
                if currentGlyphName:
                    if currentGlyphName in font:
                        newGlyph = font[currentGlyphName]
                    else:
                        newGlyph = font.newGlyph(currentGlyphName)
                    CurrentGlyphWindow().setGlyph(newGlyph)
            except:
                pass

FontSelectorController()