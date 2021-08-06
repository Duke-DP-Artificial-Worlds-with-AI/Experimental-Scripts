import glob
import re
import random

#city_img_dir = "/hdd/dataplus2021/share/data/images_new/"
#city_imgs = glob.glob(city_img_dir + "*.jpg")

#exper_city = random.sample(city_imgs, 40)

def create_file(train, val,sample_imgs,sample_txts):
    img_file = "/hdd/dataplus2021/share/domain_experiment/BC_team_domain_experiment/Train {my_train} Val {my_val} 100 real 75 syn/baseline/training_img_paths.txt".format(my_train=train,my_val=val)
    lbl_file = img_file.replace("img", "lbl")

    absolute_dir = "/hdd/dataplus2021/share"

    with open(img_file, "r") as f:
        img_files = f.read().replace("..", absolute_dir).split("\n")

    with open(lbl_file, "r") as f:
        txt_files = f.read().replace("..", absolute_dir).split("\n")

    out_img_file = "/hdd/dataplus2021/fcw/domain_txt_files2/train_{my_train}_val_{my_val}_imgs.txt".format(my_train=train,my_val=val)
    out_lbl_file = out_img_file.replace("imgs", "lbls")

    with open(out_img_file, "w") as f:
        f.writelines("%s\n" % l for l in img_files)
        f.writelines("%s\n" % l for l in sample_imgs)

    with open(out_lbl_file, "w") as f:
        f.writelines("%s\n" % l for l in txt_files)
        f.writelines("%s\n" % l for l in sample_txts)

random.seed(42)

NW_dir = "/hdd/dataplus2021/fcw/experimental_output_ratio_NW"
all_NW_imgs = glob.glob(NW_dir + "/**/*.jpg", recursive = True)

SW_dir = "/hdd/dataplus2021/fcw/experimental_output_ratio_SW"
all_SW_imgs = glob.glob(SW_dir + "/**/*.jpg", recursive = True)

NE_dir = "/hdd/dataplus2021/fcw/experimental_output_ratio_NE"
all_NE_imgs = glob.glob(NE_dir + "/**/*.jpg", recursive = True)

EM_dir = "/hdd/dataplus2021/fcw/experimental_output_ratio_EM"
all_EM_imgs = glob.glob(EM_dir + "/**/*.jpg", recursive = True)


EM_sample_img_file = "/hdd/dataplus2021/fcw/domain_txt_files/train_EM_val_EM_imgs.txt"
EM_sample_lbl_file = "/hdd/dataplus2021/fcw/domain_txt_files/train_EM_val_EM_lbls.txt"

with open(EM_sample_img_file, "r") as f:
    EM_sample_imgs = f.read().split("\n")[100:]

with open(EM_sample_lbl_file, "r") as f:
    EM_sample_txts = f.read().split("\n")[100:]

NE_sample_img_file = "/hdd/dataplus2021/fcw/domain_txt_files/train_NE_val_NE_imgs.txt"
NE_sample_lbl_file = "/hdd/dataplus2021/fcw/domain_txt_files/train_NE_val_NE_lbls.txt"

with open(NE_sample_img_file, "r") as f:
    NE_sample_imgs = f.read().split("\n")[100:]

with open(NE_sample_lbl_file, "r") as f:
    NE_sample_txts = f.read().split("\n")[100:]

#EM_sample_imgs = random.sample(all_EM_imgs, 75)
#EM_sample_txts = [x.replace(".jpg", ".txt") for x in EM_sample_imgs]

#NE_sample_imgs = random.sample(all_NE_imgs, 75)
#NE_sample_txts = [x.replace(".jpg", ".txt") for x in NE_sample_imgs]


SW_sample_imgs = random.sample(all_SW_imgs, 75)
SW_sample_txts = [x.replace(".jpg", ".txt") for x in SW_sample_imgs]

NW_sample_imgs = random.sample(all_NW_imgs, 75)
NW_sample_txts = [x.replace(".jpg", ".txt") for x in NW_sample_imgs]

domains = ["EM", "NE", "NW", "SW"]

for x in domains:
    for y in domains:
        create_file(x,y,eval(y + "_sample_imgs"),eval(y + "_sample_txts"))
