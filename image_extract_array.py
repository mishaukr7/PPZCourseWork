import scipy.io
from numpy import *
from scipy import ndimage
import numpy as np


def get_image_array(image):
    '''
    :param image: path to image;
    :return: list of RGB color.
    '''
    return scipy.misc.imread(image, mode='RGB').astype(float32)


def get_image_array_with_noise(image, noiseVariance):
    image_with_noise = get_image_array(image) + random.normal(0, noiseVariance, size=get_image_array(image).shape)
    return image_with_noise


def transform_coefficients_from_rgb_to_yuv(input_array, a, b, c, alpha):
    '''
    Transform RGB format to YUV (grayscale layer format)
    :param input_array: array of input data
    :param a: coefficient a
    :param b: coefficient b
    :param c: coefficient c
    :return: array YUV-format of image.
    '''
    transform_list = []
    for first_list in input_array:
        first_list_transform = []
        for second_list in first_list:
            first_list_transform.append(second_list[0] * a + second_list[1] * b + second_list[2] * c + alpha)
        transform_list.append(first_list_transform)
    return transform_list


def last_transform(y, u, v):
    external_array = []
    for q_1 in range(len(y)):
        internal_array = []
        for q_2 in range(len(y[q_1])):
            r = y[q_1][q_2] + 1.13983 * (v[q_1][q_2] - 128)
            g = y[q_1][q_2] - 0.39465 * (u[q_1][q_2] - 128) - 0.58060 * (v[q_1][q_2] - 128)
            b = y[q_1][q_2] + 2.03211 * (u[q_1][q_2] - 128)
            internal_array.append([((int(r))**2)**0.5, ((int(g))**2)**0.5, ((int(b))**2)**0.5])
        external_array.append(internal_array)
    print(external_array)
    return external_array


def ConvertYUVtoRGB(yuv_planes):
    plane_y = yuv_planes[0]
    plane_u = yuv_planes[1]
    plane_v = yuv_planes[2]

    height = plane_y.shape[0]
    width = plane_y.shape[1]

    # upsample if YV12
    plane_u = ndimage.zoom(plane_u, 2, order=0)
    plane_v = ndimage.zoom(plane_v, 2, order=0)
    # alternativelly can perform upsampling with numpy.repeat()
    # plane_u = plane_u.repeat(2, axis=0).repeat(2, axis=1)
    # plane_v = plane_v.repeat(2, axis=0).repeat(2, axis=1)

    # reshape
    plane_y = plane_y.reshape((plane_y.shape[0], plane_y.shape[1], 1))
    plane_u = plane_u.reshape((plane_u.shape[0], plane_u.shape[1], 1))
    plane_v = plane_v.reshape((plane_v.shape[0], plane_v.shape[1], 1))

    # make YUV of shape [height, width, color_plane]
    yuv = np.concatenate((plane_y, plane_u, plane_v), axis=2)

    # according to ITU-R BT.709
    yuv[:, :, 0] = yuv[:, :, 0].clip(16, 235).astype(yuv.dtype) - 16
    yuv[:, :, 1:] = yuv[:, :, 1:].clip(16, 240).astype(yuv.dtype) - 128

    A = np.array([[1.164, 0.000, 1.793],
                  [1.164, -0.213, -0.533],
                  [1.164, 2.112, 0.000]])

    # our result
    rgb = np.dot(yuv, A.T).clip(0, 255).astype('uint8')

    return rgb