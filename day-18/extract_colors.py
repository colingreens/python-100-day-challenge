import colorgram as cg

color_list = cg.extract('Ellipticine.png', 30)
color_pallette = []

for color in color_list:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    color_pallette.append((r,g,b))

print(color_pallette)