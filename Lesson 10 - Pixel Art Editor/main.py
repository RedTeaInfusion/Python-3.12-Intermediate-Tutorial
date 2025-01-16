'''
Lesson 10 - Pixel Art Editor
'''
import tkinter as tk
from tkinter import filedialog, colorchooser
from PIL import Image, ImageDraw

GRID_SIZE = 16
BLOCK_SIZE = 20
root = None
brush_color = 'black'
is_painting = False
image = None
draw = None

def redraw_canvas():
    canvas.config(width=GRID_SIZE * BLOCK_SIZE, height=GRID_SIZE * BLOCK_SIZE)
    canvas.delete('all')
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            x0 = x * BLOCK_SIZE
            y0 = y * BLOCK_SIZE
            x1 = x0 + BLOCK_SIZE
            y1 = y0 + BLOCK_SIZE
            color = image.getpixel((x0, y0))
            hex_color = '#{:02x}{:02x}{:02x}'.format(*color[:3])
            canvas.create_rectangle(x0, y0, x1, y1, fill=hex_color, outline='black', width=1)

def change_color(new_color):
    global brush_color
    brush_color = new_color

def create_custom_color():
    global brush_color
    color_code = colorchooser.askcolor()[1]
    if color_code:
        brush_color = color_code
        create_color_button(color_code)

def create_color_button(color):
    col = len(color_buttons) % 10 + 1
    row = len(color_buttons) // 10
    button = tk.Button(color_frame, bg=color, width=3, height=2, command=lambda: change_color(color))
    button.grid(row=row, column=col, pady=2)
    color_buttons.append(button)

def start_paint(event):
    global is_painting
    is_painting = True
    paint(event)

def stop_paint(event):
    global is_painting
    is_painting = False

def paint(event):
    if not is_painting:
        return
    x_index = event.x // BLOCK_SIZE
    y_index = event.y // BLOCK_SIZE
    if 0 <= x_index < GRID_SIZE and 0 <= y_index < GRID_SIZE:
        x0 = x_index * BLOCK_SIZE
        y0 = y_index * BLOCK_SIZE
        x1 = x0 + BLOCK_SIZE
        y1 = y0 + BLOCK_SIZE
        draw.rectangle([(x0, y0), (x1, y1)], fill=brush_color)
        canvas.create_rectangle(x0, y0, x1, y1, fill=brush_color, outline='black', width=1)

def new_image():
    global image, draw
    image = Image.new('RGBA', (GRID_SIZE * BLOCK_SIZE, GRID_SIZE * BLOCK_SIZE), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    redraw_canvas()

def open_image():
    file_path = filedialog.askopenfilename(filetypes=[('PNG files','*.png'),
                                                      ('All files', '*.*')])
    if file_path:
        img = Image.open(file_path).convert('RGBA')
        img_resized = img.resize((GRID_SIZE * BLOCK_SIZE, GRID_SIZE * BLOCK_SIZE), Image.NEAREST)
        global image, draw
        image = img_resized
        draw = ImageDraw.Draw(image)
        redraw_canvas()

def save_image():
    file_path = filedialog.asksaveasfilename(defaultextension='.png',
                                             filetypes=[('PNG files', '*.png'),
                                                        ('All files', '*.*')])
    if file_path:
        resized_image = image.resize((GRID_SIZE, GRID_SIZE), Image.NEAREST)
        resized_image.save(file_path)

def exit():
    root.destroy()

def setup_app():
    global root, image, draw, color_buttons, color_frame, canvas
    root = tk.Tk()
    root.title('Pixel Art Editor')
    image = Image.new('RGBA', (GRID_SIZE * BLOCK_SIZE, GRID_SIZE * BLOCK_SIZE), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)

    menu_bar = tk.Menu(root)
    root.config(menu=menu_bar)
    file_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label='File', menu=file_menu)
    file_menu.add_command(label='New', command=new_image)
    file_menu.add_command(label='Open', command=open_image)
    file_menu.add_command(label='Save', command=save_image)
    file_menu.add_separator()
    file_menu.add_command(label='Exit', command=exit)

    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=True)

    color_frame = tk.Frame(main_frame)
    color_frame.grid(row=0, column=0, padx=10, pady=10, sticky='ns')
    color_buttons = []
    colors = ['black', 'white', 'gray', 'red', 'blue', 'yellow', 'orange', 'green']
    for color in colors:
        create_color_button(color)
    custom_color_button = tk.Button(color_frame, text='+', command=create_custom_color)
    custom_color_button.grid(row=0, column=0, padx=10)

    canvas_frame = tk.Frame(main_frame)
    canvas_frame.grid(row=1, column=0, padx=10, pady=10)
    canvas = tk.Canvas(canvas_frame)
    canvas.pack()
    canvas.bind('<Button-1>', start_paint)
    canvas.bind('<B1-Motion>', paint)
    canvas.bind('<ButtonRelease-1>', stop_paint)

    redraw_canvas()

if __name__ == "__main__":
    setup_app()
    root.mainloop()