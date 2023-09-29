# -*- coding:utf-8 -*-
import numpy as np
import cv2
import matplotlib.pyplot as plt
from fast_slic.avx2 import SlicAvx2
from GF import GuideFilterColor


def get_coarse_at(img, max_ch, assignment):
    R, G, B = cv2.split(img)
    TR = np.zeros_like(R)
    TG = np.zeros_like(G)
    TB = np.zeros_like(B)
    A = np.zeros_like(img)

    max_sp_index = np.max(assignment)

    for sp_index in range(0, max_sp_index + 1):
        max_ch_temp = max_ch.copy()

        target_pos = (assignment == sp_index)
        exclu_pos = (assignment != sp_index)

        temp = R[target_pos]
        TR[target_pos] = np.min(temp)
        temp = G[target_pos]
        TG[target_pos] = np.min(temp)
        temp = B[target_pos]
        TB[target_pos] = np.min(temp)

        max_ch_temp[exclu_pos] = 0
        max_index = np.unravel_index(max_ch_temp.argmax(), max_ch_temp.shape)
        A[target_pos] = img[max_index[0], max_index[1], :]

    TR = np.clip(1 - TR, 0., 1.)
    TG = np.clip(1 - TG, 0., 1.)
    TB = np.clip(1 - TB, 0., 1.)

    return A, TR, TG, TB


def dehaze(img_path, SLIC_K=200, SLIC_M=40, SLIC_Iter=4, gf_size_a=(131, 131), gf_size_t=(39, 39), lambDa=0.85):
    # 1.0 load image
    img = cv2.imread(img_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    img_min = np.min(img_rgb, axis=2)
    img_max = np.max(img_rgb, axis=2)

    # 2.0 Superpixel Segmentation SLIC
    slic = SlicAvx2(num_components=SLIC_K, compactness=SLIC_M)
    assignment = slic.iterate(img_rgb, SLIC_Iter)

    # 3.0 coarse A and coarse T for RGB channel
    a_coarse, TR, TG, TB = get_coarse_at(img_rgb / 255., img_max / 255., assignment)

    # 4.0 Refine A and T
    a_refine = GuideFilterColor(img_max / 255., a_coarse, gf_size_a, 0.5)
    a_refine[a_refine > 1] = 1
    a_refine[a_refine < 0] = 0

    TR = lambDa * TR
    TG = lambDa * TG
    TB = lambDa * TB
    T_coarse = cv2.merge([TR, TG, TB])
    T_refine = GuideFilterColor(img_min / 255., T_coarse, gf_size_t, 0.01)
    T_refine[T_refine > 1] = 1
    T_refine[T_refine < 0.1] = 0.1

    # Haze Removal
    result = (img_rgb / 255. - a_refine) / T_refine + a_refine
    result[result > 1] = 1
    result[result < 0] = 0

    return result, img_rgb, a_coarse, a_refine, T_coarse, T_refine


if __name__ == '__main__':

    img_path = r'img/hazy/AID_railwaystation_22.jpg'

    result, img_rgb, a_coarse, a_refine, T_coarse, T_refine = dehaze(img_path)

    plt.subplot(3, 4, 1)
    plt.title('input')
    plt.imshow(img_rgb, vmin=0.0, vmax=1.0)

    plt.subplot(3, 4, 2)
    plt.title('result')
    plt.imshow(result, vmin=0.0, vmax=1.0)

    plt.subplot(3, 4, 3)
    plt.title('A coarse')
    plt.imshow(a_coarse)

    plt.subplot(3, 4, 4)
    plt.title('A refined')
    plt.imshow(a_refine)

    plt.subplot(3, 4, 5)
    plt.title('Red T coarse')
    plt.imshow(T_coarse[:,:,0], vmin=0.0, vmax=1.0, cmap='jet')

    plt.subplot(3, 4, 6)
    plt.title('Green T coarse')
    plt.imshow(T_coarse[:,:,1], vmin=0.0, vmax=1.0, cmap='jet')

    plt.subplot(3, 4, 7)
    plt.title('Blue T coarse')
    plt.imshow(T_coarse[:,:,2], vmin=0.0, vmax=1.0, cmap='jet')

    plt.subplot(3, 4, 9)
    plt.title('Red T refined')
    plt.imshow(T_refine[:,:,0], vmin=0.0, vmax=1.0, cmap='jet')

    plt.subplot(3, 4, 10)
    plt.title('Green T refined')
    plt.imshow(T_refine[:,:,1], vmin=0.0, vmax=1.0, cmap='jet')

    plt.subplot(3, 4, 11)
    plt.title('Blue T refined')
    plt.imshow(T_refine[:,:,2], vmin=0.0, vmax=1.0, cmap='jet')

    plt.show()

