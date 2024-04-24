from PIL import Image


i=Image.open(r'C:\1-MD-25-Korshunov\g.jpg')

ri=i.resize((320,200))
ri
ri.save('g_2.jpg')