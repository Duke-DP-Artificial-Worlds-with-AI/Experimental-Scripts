import cv2
import random
import glob
import os
import re

def plot_one_box(x_ctrs, y_ctrs, widths, heights, img, fname, color=None, label=None, line_thickness=None):
    for i in range(len(x_ctrs)):
      x = [x_ctrs[i]-widths[i],y_ctrs[i]-heights[i],x_ctrs[i]+widths[i],y_ctrs[i]+heights[i]]
      # Plots one bounding box on image img
      tl = line_thickness or round(0.002 * (img.shape[0] + img.shape[1]) / 2) + 1  # line/font thickness
      color = color or [random.randint(0, 255) for _ in range(3)]
      c1, c2 = (int(x[0]), int(x[1])), (int(x[2]), int(x[3]))
      cv2.rectangle(img, c1, c2, color, thickness=tl, lineType=cv2.LINE_AA)
    #Save file
    cv2.imwrite(fname, img)

def multiple_replace(dict, text):
  # Create a regular expression  from the dictionary keys
  regex = re.compile("(%s)" % "|".join(map(re.escape, dict.keys())))

  # For each match, look-up corresponding value in dictionary
  return regex.sub(lambda mo: dict[mo.string[mo.start():mo.end()]], text) 


reg_dict = {
    "ImageAugment4":"BoundingBoxes",
    "results9":"results6"
}

my_img_dir = "/hdd/dataplus2021/fcw/ImageAugment4/results9/"
results_dir = "/hdd/dataplus2021/fcw/BoundingBoxes/results6/"

if not os.path.exists(results_dir):
  os.mkdir(results_dir)

my_imgs = glob.glob(my_img_dir + "*.jpg")
my_txts = glob.glob(my_img_dir + "*.txt")

my_imgs.sort()
my_txts.sort()


for k in range(len(my_imgs)):
  #Inputs- can make it glob and sort so array
  my_png_file = my_imgs[k]
  my_txt_file = my_txts[k]
  #Add output folder

  #Can loop over
  with open(my_txt_file, "r") as f:
      lst = [float(x) for x in f.read().split()]

  x_ctrs = [i*608 for i in lst[1::5]]
  y_ctrs = [i*608 for i in lst[2::5]]
  widths = [i*304 for i in lst[3::5]]
  heights = [i*304  for i in lst[4::5]]

  my_img = cv2.imread(my_png_file)

  new_fname = multiple_replace(reg_dict, my_png_file)
  print(new_fname)

  plot_one_box(x_ctrs=x_ctrs, y_ctrs=y_ctrs, widths=widths, heights=heights,img=my_img,fname=new_fname)
