import main
from denoise_rgb_image import *
from compare_estimation import compare_psnr

image = main.get_image_array('images/taj.jpg')

img = img_as_float(image)

sigma_est = estimate_sigma(img, multichannel=True, average_sigmas=True)
#print(sigma_est)
denoised_image = denoise_wavelet(img, multichannel=True, convert2ycbcr=True, mode='soft',
                                 sigma=2*sigma_est, wavelet='db3')
#print(im_visushrink2)
print(compare_psnr(img, denoised_image))
main.show_image(denoised_image)
# plt.gray()
# plt.figure(1)
# plt.show(im_visushrink2)
# plt.show()