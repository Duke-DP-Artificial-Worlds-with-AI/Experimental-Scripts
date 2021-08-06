import glob
import os
from shutil import copyfile
import random

#IF CHANGE THIS CHANGE LINE 48
src_dir = "/hdd/dataplus2021/fcw/ImageAugment4/results9/"
all_srcs = glob.glob(src_dir + "*.jpg")
all_masks = glob.glob(src_dir + "*.png")
all_txts = glob.glob(src_dir + "*.txt")
all_srcs.sort()
all_masks.sort()
all_txts.sort()

#print(all_srcs[i].replace(".jpg", "__mask2.png") == all_masks[i])
random.seed(42)

dest_dir = "/hdd/dataplus2021/fcw/background_by_domain/"

#Change to NW
all_em_dsts = glob.glob(dest_dir + "NW/*.jpg")
EM_dsts = random.sample(all_em_dsts, 25)

#Change to SW
all_ne_dsts = glob.glob(dest_dir + "SW/*.jpg")
NE_dsts = random.sample(all_ne_dsts, 25)

def run_a_grid(curr_subdir, all_dsts, my_src, my_mask, my_txt, src_address):
    if not os.path.exists(curr_subdir):
        os.makedirs(curr_subdir)
        print(curr_subdir + " directory was made")
    for j in range(len(all_dsts)):
        my_dst = all_dsts[j]
        dst_address = my_dst[my_dst.rfind("/")+1:]
        #blended_out = "{subdir}{src_addr}_{dst_addr}".format(subdir=curr_subdir,src_addr=src_address,dst_addr=dst_address)
        blended_out = "{subdir}{dst_addr}".format(subdir=curr_subdir,src_addr=src_address,dst_addr=dst_address)
        blended_out = blended_out.replace(" ", "")
        copyfile(my_txt, blended_out.replace(".jpg",".txt"))
        cmd = "python run_gp_gan.py --src_image {src} --dst_image \"{dst}\" --mask_image {mask} --blended_image {out}".format(src=my_src,dst=my_dst,mask=my_mask,out=blended_out)
        print("Running command:")
        print(cmd)
        os.system(cmd)

for i in range(len(all_srcs)):
    my_src = all_srcs[i]
    my_mask = all_masks[i]
    my_txt = all_txts[i]
    src_address = my_src[my_src.find("results9/")+len("results9/"):my_src.find(".jpg")]

    em_subdir = "/hdd/dataplus2021/fcw/experimental_output_ratio_NW/{src_addr}/".format(src_addr=src_address)

    run_a_grid(em_subdir, EM_dsts, my_src, my_mask, my_txt, src_address)

    ne_subdir = "/hdd/dataplus2021/fcw/experimental_output_ratio_SW/{src_addr}/".format(src_addr=src_address)
    
    run_a_grid(ne_subdir, NE_dsts, my_src, my_mask, my_txt, src_address)


