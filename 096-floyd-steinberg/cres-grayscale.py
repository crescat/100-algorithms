# Day 96: Floyd-Steinberg

from PIL import Image
import copy

def dithering(rgb_matrix, interval):
    width = len(rgb_matrix[0])
    height = len(rgb_matrix)
    mtx = copy.deepcopy(rgb_matrix)
    for y in range(height):
        for x in range(width):
            old_value = mtx[y][x]
            new_value = find_closest_value(old_value, interval)
            mtx[y][x] = new_value
            quant_error = old_value - new_value
            if x + 1 < width:
                # right pixel
                mtx[y][x+1] = mtx[y][x+1] + quant_error * 7 / 16

            if x - 1 >= 0 and y + 1 < height:
                # botton left pixel
                mtx[y+1][x-1] = mtx[y+1][x-1] + quant_error * 3 / 16

            if y + 1 < height:
                # botton pixel
                mtx[y+1][x] = mtx[y+1][x] + quant_error * 5 / 16

            if x + 1 < width and y + 1 < height:
                # botton right pixel
                mtx[y+1][x+1] = mtx[y+1][x+1] + quant_error * 1 / 16
    return mtx


def get_pixel_map(image_path):
    im = Image.open(image_path, 'r')
    width, height = im.size
    pixels = list(im.getdata())
    pixel_map = [pixels[i:i + width] for i in range(0, len(pixels), width)]
    for i in range(height):
        for j in range(width):
            pixel = pixel_map[i][j]
            pixel_map[i][j] = (pixel[0]/255 + pixel[1]/255 + pixel[2]/255) / 3
    return pixel_map


def find_closest_value(value, interval):
    candidates = [i / interval for i in range(interval+1)]
    return min(candidates, key=lambda x:abs(x-value))

def save_image(matrix, filename):
    height = len(matrix)
    width = len(matrix[0])
    new_image = Image.new('RGB', (width, height))
    pixels = new_image.load()
    for y in range(height):
        for x in range(width):
            brightness = round(matrix[y][x] * 255)
            pixels[x, y] = (brightness, brightness, brightness)
    new_image.save(filename)

def process_image(image_path, output_path, color_interval):
    pixel_map = get_pixel_map(image_path)
    save_image(pixel_map, "grayscale.png")
    dithered_pixel_map = dithering(pixel_map, color_interval)


    save_image(dithered_pixel_map, output_path)


process_image("pyu.png", "pyu-dithered-grayscale.png", 1)
