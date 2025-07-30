f = CurrentFont()

layerName = "foreground"

for g in f:
    layerGlyph = g.getLayer(layerName)
    
    layerGlyph.correctDirection()
    
    print(g.name)