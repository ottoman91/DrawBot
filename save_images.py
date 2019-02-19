from quickdraw import QuickDrawDataGroup
from quickdraw import QuickDrawData
import sys
import os

qd = QuickDrawData()

for drawing_num, drawing_name in enumerate(qd.drawing_names):
    print("Saving " + drawing_name + " images")
    qdg = QuickDrawDataGroup(drawing_name, max_drawings=200)
    directory_name = 'images/' + drawing_name
    if not os.path.isdir(os.path.join(os.getcwd(), directory_name)):
        os.mkdir(directory_name)        
    for drawing_count, drawing in enumerate(qdg.drawings, 1):
        drawing.image.save(directory_name + "/" + drawing_name + "{:0>4d}.png".format(drawing_count))
