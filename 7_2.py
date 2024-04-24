from PIL import Image


i=Image.open(r'C:\1-MD-25-Korshunov\g.jpg')

ri=i.resize((320,200))
riz= ri.transpose(Image.FLIP_LEFT_RIGHT)
riz.save('gz.jpg')
riz1= ri.transpose(Image.FLIP_LEFT_RIGHT)
riz1.save('gz_2.jpg')