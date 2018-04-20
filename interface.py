from tkinter import *
from tkinter import filedialog
import denoising_image
import main


class Application:

    def __init__(self, master):
        self.master = master
        self.file_path = StringVar(master)

        master.title('Denoising image')
        self.master.geometry('350x200')

        self.drop_wavelet_family_text = StringVar(master)
        self.threhold_method = StringVar(master)
        self.blank_label = Label(master, text="\n")

    def get_image_url(self):
        filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                              filetypes=(("jpeg files", "*.jpg"),
                                                         ("png files", "*.png"),
                                                         ("all files", "*.*")))
        if filename:
            self.file_path.set(str(filename))


class DenoisedImage(Application):
    wavelet_family_label_list = ['bior1.1',
                                 'cgau1',
                                 'cmor',
                                 'coif1',
                                 'coif2',
                                 'db1',
                                 'db2',
                                 'db3',
                                 'dmey',
                                 'gaus1',
                                 'gaus2',
                                 'haar',
                                 'sym2',
                                 'sym3'
                                 ]

    threhold_method_list = [
        'soft',
        'hard',
        'greater',
        'less'
    ]

    def __init__(self, master):
        Application.__init__(self, master)

        self.top_label = Label(master, text="PROGRAM FOR DENOISING IMAGE", anchor=CENTER)
        self.top_label.grid()

        self.label_wavelet_family = Label(master, text='Choose wavelet family: ', width=30)
        self.label_wavelet_family.grid(row=2, column=0)
        self.drop_wavelet_family_text.set(self.wavelet_family_label_list[0])
        self.drop_menu = OptionMenu(master, self.drop_wavelet_family_text, *self.wavelet_family_label_list)
        self.drop_menu.grid(row=2, column=1)

        self.label_get_image = Label(master, text='Choose image for denoising: ')
        self.label_get_image.grid(row=4, column=0)
        self.get_image_button = Button(master, text='Open', command=self.get_image_url)
        self.get_image_button.grid(row=4, column=1)

        self.label_threhold = Label(master, text="Choose threshold denoising: ")
        self.label_threhold.grid(row=6, column=0)
        self.threhold = Spinbox(master, from_=0, to_=1000, width=10)
        self.threhold.grid(row=6, column=1)

        self.label_threhold_method = Label(master, text="Choose method of thresholding: ")
        self.label_threhold_method.grid(row=8, column=0)
        self.threhold_method.set(self.threhold_method_list[0])
        self.threhold_method_option = OptionMenu(master, self.threhold_method, *self.threhold_method_list)
        self.threhold_method_option.grid(row=8, column=1)

        self.blank_label.grid()
        self.submit_button = Button(master, text="Submit", command=self.show_denoise_image, fg='GREEN')
        self.submit_button.grid(row=10, column=1)

    def show_denoise_image(self):
        main.show_image(denoising_image.denoising_image(str(self.file_path.get()),
                                                        str(self.drop_wavelet_family_text.get()),
                                                        1,
                                                        int(self.threhold.get()),
                                                        str(self.threhold_method.get())))

    def __str__(self):
        return self.file_path, self.drop_wavelet_family_text, self.threhold


root = Tk()
my_gui = DenoisedImage(root)
root.mainloop()
