from tkinter import *
from tkinter import filedialog
import denoising_image
import main
from denoise_rgb_image import *
import sqlite3


class Application:

    def __init__(self, master):
        self.master = master
        self.file_path = StringVar(master)

        master.title('Denoising image')
        self.master.geometry('700x380')

        self.drop_wavelet_family_text = StringVar(master)
        self.threhold_method = StringVar(master)
        self.blank_label = Label(master, text="\n")
        self.image_color_type = StringVar(master)

    def get_image_url(self):
        filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                              filetypes=(("jpeg files", "*.jpg"),
                                                         ("png files", "*.png"),
                                                         ("all files", "*.*")))
        if filename:
            self.file_path.set(str(filename))


class DenoisedImage(Application):
    wavelet_family_label_list = ['db1',
                                 'db2',
                                 'db3',
                                 'dmey',
                                 'gaus1',
                                 'gaus2',
                                 'haar',
                                 'sym2',
                                 'sym3',
                                 'bior1.3',
                                 'bior2.2'
                                 ]

    threhold_method_list = [
        'soft',
        'hard'
    ]

    color_type_list = [
        'RGB',
        'grayscale'
    ]

    def __init__(self, master):
        Application.__init__(self, master)

        self.top_label = Label(master, text="PROGRAM FOR DENOISING IMAGE", anchor=CENTER, font=("Arial Bold", 17))
        self.top_label.grid(row=0, column=0, padx=(150, 0))
        self.blank_label = Label(master, text="\n")
        self.blank_label.grid()

        self.label_wavelet_family = Label(master, text='Choose wavelet family: ', width=30, font=("Arial", 17))
        self.label_wavelet_family.grid(row=2, column=0)
        self.drop_wavelet_family_text.set(self.wavelet_family_label_list[0])
        self.drop_menu = OptionMenu(master, self.drop_wavelet_family_text, *self.wavelet_family_label_list)
        self.drop_menu.configure(font=("Arial", 17))
        self.drop_menu.grid(row=2, column=1)

        self.label_get_image = Label(master, text='Choose image for denoising: ', font=("Arial", 17))
        self.label_get_image.grid(row=10, column=0)
        self.get_image_button = Button(master, text='Open', command=self.get_image_url)
        self.get_image_button.configure(font=("Arial", 17))
        self.get_image_button.grid(row=10, column=1)

        self.label_threhold_method = Label(master, text="Choose method of thresholding: ", font=("Arial", 17))
        self.label_threhold_method.grid(row=8, column=0)
        self.threhold_method.set(self.threhold_method_list[0])
        self.threhold_method_option = OptionMenu(master, self.threhold_method, *self.threhold_method_list)
        self.threhold_method_option.configure(font=("Arial", 17))
        self.threhold_method_option.grid(row=8, column=1)

        self.label_image_color_type = Label(master, text="Choose image color type: ", font=("Arial", 17))
        self.label_image_color_type.grid(row=4, column=0)
        self.image_color_type.set(self.color_type_list[0])
        self.color_type_option = OptionMenu(master, self.image_color_type, *self.color_type_list)
        self.color_type_option.configure(font=("Arial", 17))
        self.color_type_option.grid(row=4, column=1)
        self.blank_label = Label(master, text="\n")
        self.blank_label.grid()

        self.submit_button = Button(master, text="Submit", command=self.show_denoise_image, fg='GREEN', font=("Arial Bold", 15))
        self.submit_button.grid(row=12, column=1)

    def show_denoise_image(self):
        conn = sqlite3.connect('database.db')
        if str(self.image_color_type.get()) == self.color_type_list[1]:
            main.show_image(denoising_image.denoising_image(str(self.file_path.get()),
                                                            str(self.drop_wavelet_family_text.get()),
                                                            str(self.threhold_method.get()))[0])
        elif str(self.image_color_type.get()) == self.color_type_list[0]:
            image = main.get_image_array(str(self.file_path.get()))
            img = img_as_float(image)
            sigma_est = estimate_sigma(img, multichannel=True, average_sigmas=True)
            denoised_image = denoise_wavelet(img, multichannel=True, convert2ycbcr=True, mode=str(self.threhold_method.get()),
                                             sigma=2 * sigma_est, wavelet=str(self.drop_wavelet_family_text.get()))
            main.show_image(denoised_image)

    def __str__(self):
        return self.file_path, self.drop_wavelet_family_text


root = Tk()
my_gui = DenoisedImage(root)
root.mainloop()
