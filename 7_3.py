from PIL import Image
from PIL import ImageFilter

for i in range(1,6):
    a=Image.open(f'C:\1-MD-25-Korshunov\{i}')
    a=a.filter(ImageFilter.SHARPEN)
    a.save(f'C:\1-MD-25-Korshunov\{i}')