# -*- coding:utf-8 -*-
import cv2


def GuideFilter(I, p, winSize, eps):
    # I的均值平滑
    mean_I = cv2.blur(I, winSize)

    # p的均值平滑
    mean_p = cv2.blur(p, winSize)

    # I*I和I*p的均值平滑
    mean_II = cv2.blur(I * I, winSize)

    mean_Ip = cv2.blur(I * p, winSize)

    # 方差
    var_I = mean_II - mean_I * mean_I  # 方差公式

    # 协方差
    cov_Ip = mean_Ip - mean_I * mean_p

    a = cov_Ip / (var_I + eps)
    b = mean_p - a * mean_I

    # 对a、b进行均值平滑
    mean_a = cv2.blur(a, winSize)
    mean_b = cv2.blur(b, winSize)

    q = mean_a * I + mean_b

    return q


def FastGuideFilter(I, p, winSize, eps, s):
    # 输入图像的高、宽
    h, w = I.shape[:2]

    # 缩小图像
    size = (int(round(w * s)), int(round(h * s)))

    small_I = cv2.resize(I, size, interpolation=cv2.INTER_CUBIC)
    small_p = cv2.resize(p, size, interpolation=cv2.INTER_CUBIC)

    # 缩小滑动窗口
    X = winSize[0]
    small_winSize = (int(round(X * s)), int(round(X * s)))

    # I的均值平滑
    mean_small_I = cv2.blur(small_I, small_winSize)

    # p的均值平滑
    mean_small_p = cv2.blur(small_p, small_winSize)

    # I*I和I*p的均值平滑
    mean_small_II = cv2.blur(small_I * small_I, small_winSize)

    mean_small_Ip = cv2.blur(small_I * small_p, small_winSize)

    # 方差
    var_small_I = mean_small_II - mean_small_I * mean_small_I  # 方差公式

    # 协方差
    cov_small_Ip = mean_small_Ip - mean_small_I * mean_small_p

    small_a = cov_small_Ip / (var_small_I + eps)
    small_b = mean_small_p - small_a * mean_small_I

    # 对a、b进行均值平滑
    mean_small_a = cv2.blur(small_a, small_winSize)
    mean_small_b = cv2.blur(small_b, small_winSize)

    # 放大
    size1 = (w, h)
    mean_a = cv2.resize(mean_small_a, size1, interpolation=cv2.INTER_LINEAR)
    mean_b = cv2.resize(mean_small_b, size1, interpolation=cv2.INTER_LINEAR)

    q = mean_a * I + mean_b

    return q


def FastGuideFilterColor(I, p, winSize, eps, s=0.5):
    # 引导图I为单通道
    # 滤波图像p为3通道，图像为[0,1]范围float型
    r, g, b = cv2.split(p)
    rr = FastGuideFilter(I, r, winSize, eps, s)
    gg = FastGuideFilter(I, g, winSize, eps, s)
    bb = FastGuideFilter(I, b, winSize, eps, s)
    return cv2.merge([rr, gg, bb])


def GuideFilterColor(I, p, winSize, eps):
    # 引导图I为单通道
    # 滤波图像p为3通道，图像为[0,1]范围float型
    r, g, b = cv2.split(p)
    rr = GuideFilter(I, r, winSize, eps)
    gg = GuideFilter(I, g, winSize, eps)
    bb = GuideFilter(I, b, winSize, eps)
    return cv2.merge([rr, gg, bb])