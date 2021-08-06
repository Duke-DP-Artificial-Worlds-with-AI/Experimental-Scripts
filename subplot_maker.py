import matplotlib.pyplot as plt
from PIL import Image
import textwrap, os
import glob

def display_images(name,images=[Image],columns=10, width=50, height=15, 
    label_wrap_length=50, label_font_size=8):
  print(name)
  plt.figure(figsize=(width, height))
  for i, image in enumerate(images):
        plt.subplot(int(len(images) / columns + 1), columns, i + 1)
        plt.axis('off')
        plt.imshow(image)

        if hasattr(image, 'filename'):
            title=image.filename
            if title.endswith("/"): title = title[0:-1]
            title=os.path.basename(title)
            title=textwrap.wrap(title, label_wrap_length)
            title="\n".join(title)
            plt.title(title, fontsize=label_font_size);
  plt.savefig('/hdd/dataplus2021/fcw/grids/' + name + ' grid.png')

path = "/hdd/dataplus2021/ct260/windmills/GP-GAN/"

#forest4, glacier1, suburban11
#forest9, glacier2, suburban36
current_imgs = ["forest4", "glacier1", "suburban11", "forest9", "glacier2", "suburban36"]

for j in current_imgs:
  print(j)
  my_name = j
  image_paths = glob.glob(path + my_name + "**/*.png", recursive=True)

  image_paths.sort()
  print(image_paths)

  images = []
  for x in image_paths:
      print(x)
      images.append(Image.open(x))

  display_images(my_name,images)

print("DONE!")
