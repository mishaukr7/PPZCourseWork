from skimage.util import random_noise
from scipy.misc import imread
from denoise_rgb_image import estimate_sigma
from denoising_image import denoising_image
from compare_estimation import compare_psnr, compare_mse
from skimage import img_as_float
from denoise_rgb_image import denoise_wavelet


#sigma_est = estimate_sigma(img, multichannel=True, average_sigmas=True)
#print(sigma_est)
#denoised_image = denoise_wavelet(img, multichannel=True, convert2ycbcr=True, mode='soft',
 #                                sigma=2*sigma_est, wavelet='db3')
#print(im_visushrink2)
#print(compare_psnr(img, denoised_image))
#main.show_image(denoised_image)

# plt.figure(1)
# plt.gray()
# plt.axis('off')
# plt.imshow(noisy)
# plt.show()


wavelet_family_label_list = ['haar',
                             'db2',
                             'db3',
                             'db4',
                             'dmey',
                             'sym2',
                             'sym3',
                             'bior1.3',
                             ]

image1 = imread('C:\img\zz.jpg')
image_noise = imread('C:\img\zz_noise.jpg')
img = img_as_float(image1)
img_noise = img_as_float(image_noise)

mse_noise = compare_mse(img, img_noise)*255
psnr_noise = compare_psnr(img, img_noise)
print(mse_noise, psnr_noise)
#sigma = estimate_sigma(image_noise)
print('threshloding mode', 'Wavelet', 'sigma', 'MSE', 'PSNR', 'delta_MSE_%', 'delta_PSNR_%')
for x in wavelet_family_label_list:
    #mse = compare_mse(img, img_as_float(denoising_image('C:\img\lena_noise.png', x, 'hard')[0]))*255
    #psnr = compare_psnr(img, img_as_float(denoising_image('C:\img\lena_noise.png', x, 'hard')[0]))
    sigma_est = estimate_sigma(img_noise, multichannel=True, average_sigmas=True)*255
    mse = compare_mse(img, img_as_float(denoise_wavelet(img_noise, multichannel=True, convert2ycbcr=True, mode='soft',
                                                        sigma=2*sigma_est, wavelet=x)))*255
    psnr = compare_psnr(img, img_as_float(denoise_wavelet(img_noise, multichannel=True, convert2ycbcr=True, mode='soft',
                                                          sigma=2*sigma_est, wavelet=x)))

    print('soft', x, sigma_est, 2*mse, psnr, (mse_noise/2*mse)*100-100, abs((psnr_noise/psnr)*100-100))

# print(pywt.wavelist())