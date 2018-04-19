import scipy.io
from numpy import *

def get_image_array(image):
    '''

    :param image: path to image;
    :return: list of RGB color.
    '''
    return scipy.misc.imread(image, mode='RGB')


def get_image_array_with_noise(image, noiseVariance):
    image_with_noise = get_image_array(image) + random.normal(0, noiseVariance, size=get_image_array(image).shape)
    return image_with_noise


def transform_coefficients_from_rgb_to_yuv(input_array, a, b, c):
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
            first_list_transform.append(second_list[0] * a + second_list[1] * b + second_list[2] * c)
        transform_list.append(first_list_transform)
    return transform_list


def last_transform(y, u, v):
    external_array = []
    for q_1 in range(len(y)):
        internal_array = []
        for q_2 in range(len(y[q_1])):
            r = y[q_1][q_2] + 1.3707 * (v[q_1][q_2] - 128)
            g = y[q_1][q_2] - 0.3365 * (u[q_1][q_2] - 128) - 0.6982 * (v[q_1][q_2] - 128)
            b = y[q_1][q_2] + 1.7324 * (u[q_1][q_2] - 128)
            internal_array.append([int(r), int(g), int(b)])
        external_array.append(internal_array)
    return external_array

