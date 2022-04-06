# Install library
#pip install pillow
#pip install webcolors
#pip install KDTrees

# Import Module
from PIL import Image

from scipy.spatial import KDTree
import webcolors as wb
import time
# from webcolors import css3_hex_to_names, hex_to_rgb
a = time.time()
def convert_rgb_to_names(rgb_tuple):
    
    # a dictionary of all the hex and their respective names in css3
    css3_db = wb.CSS3_HEX_TO_NAMES
    names = []
    rgb_values = []

    for color_hex, color_name in css3_db.items():
        names.append(color_name)
        rgb_values.append(wb.hex_to_rgb(color_hex))
    
    kdt_db = KDTree(rgb_values)
    distance, index = kdt_db.query(rgb_tuple)
    return f'closest match: {names[index]}'
def most_common_used_color(img):
  # Get width and height of Image
  width, height = img.size
  # Initialize Variable
  r_total = 0
  g_total = 0
  b_total = 0
  count = 0
  # Iterate through each pixel
  for x in range(0, width):
    for y in range(0, height):
      # r,g,b value of pixel
      r, g, b = img.getpixel((x, y))
      r_total += r
      g_total += g
      b_total += b
      count += 1
  return (r_total/count, g_total/count, b_total/count)
# Read Image
img = Image.open('blue.jpg')
# Convert Image into RGB
img = img.convert('RGB')
# call function
common_color = most_common_used_color(img)
print(common_color)
# Output is (R, G, B)
#print(most_common_used_color(common_color))
print(convert_rgb_to_names(common_color))
print(time.time()-a)