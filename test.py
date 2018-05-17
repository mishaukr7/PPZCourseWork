import main
import scipy
from PIL import Image
import numpy

image = Image.open('images/lena.png')
pix = numpy.array(image.getdata()).reshape(image.size[0], image.size[1], 3)
print(scipy)
