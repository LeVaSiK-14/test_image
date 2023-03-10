from wand.image import Image
from wand.font import Font
from wand.display import display

with Image() as img:
    img.background_color = 'white'
    img.font = Font('Arial', 20)
    img.read(filename='label: Your Curved Text  Your Curved Text ')
    img.virtual_pixel = 'white'
    # 360 degree arc, rotated -90 degrees
    img.distort('arc', (360,-90))
    img.save(filename='arc_text.png')
    img.format = 'png'
    display(img)
