import tkinter as tk
from compressmodule import compress, decompress
from tkinter import filedialog


# i = input, o = output

def compression(i, o):
    compress(i, o)


def decompression(i, o):
    decompress(i, o)


def open_file():
    filename = filedialog.askopenfilename(initialdir='/', title='Select a file for compression')
    return filename


window = tk.Tk()
window.title('Text File Compressor')
window.geometry('600x400')

input_entry = tk.Entry(window)
output_entry = tk.Entry(window)
decompress_input = tk.Entry(window)
decompress_output = tk.Entry(window)

input_label = tk.Label(window, text='Choose file to be compressed')
output_label = tk.Label(window, text='Name of the compressed file')

compress_btn = tk.Button(window, text='Compress', command=lambda: compression(open_file(), 'compressedfile1.rar'))
# compress_btn = tk.Button(window, text='Compress', command=lambda: compression(input_entry.get(), output_entry.get()))

decompress_input_label = tk.Label(window, text='Choose file to be decompressed')
decompress_output_label = tk.Label(window, text='Name of the decompressed file')

decompress_btn = tk.Button(window, text='Decompress',
                           command=lambda: decompression(open_file(), 'decompressedfile1.txt'))
# decompress_btn = tk.Button(window, text='Decompress',
#                           command=lambda: decompression(decompress_input, decompress_output))

# compression grid
input_label.grid(row=0, column=0)
# input_entry.grid(row=0, column=1)
# output_label.grid(row=1, column=0)
# output_entry.grid(row=1, column=1)
compress_btn.grid(row=0, column=1)
# # decompression grid
decompress_input_label.grid(row=1, column=0)
# decompress_input.grid(row=5, column=1)
# decompress_output_label.grid(row=6, column=0)
# decompress_output.grid(row=6, column=1)
decompress_btn.grid(row=1, column=1)

window.mainloop()
