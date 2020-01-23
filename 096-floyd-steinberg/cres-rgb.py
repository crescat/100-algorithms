# Day 96: Floyd-Steinberg

from PIL import Image
import copy

def dithering(rgb_matrix, interval):
    width = len(rgb_matrix[0])
    height = len(rgb_matrix)
    mtx = copy.deepcopy(rgb_matrix)
    for i in range(3):
        for y in range(height):
            for x in range(width):
                old_value = mtx[y][x][i]
                new_value = find_closest_value(old_value, interval)
                mtx[y][x][i] = new_value
                quant_error = old_value - new_value
                if x + 1 < width:
                    # right pixel
                    mtx[y][x+1][i] = mtx[y][x+1][i] + quant_error * 7 / 16

                if x - 1 >= 0 and y + 1 < height:
                    # botton left pixel
                    mtx[y+1][x-1][i] = mtx[y+1][x-1][i] + quant_error * 3 / 16

                if y + 1 < height:
                    # botton pixel
                    mtx[y+1][x][i] = mtx[y+1][x][i] + quant_error * 5 / 16

                if x + 1 < width and y + 1 < height:
                    # botton right pixel
                    mtx[y+1][x+1][i] = mtx[y+1][x+1][i] + quant_error * 1 / 16
    return mtx


def get_pixel_map(image_path):
    im = Image.open(image_path, 'r')
    width, height = im.size
    pixels = list(im.getdata())
    pixel_map = [pixels[i:i + width] for i in range(0, len(pixels), width)]
    for i in range(height):
        for j in range(width):
            pixel = pixel_map[i][j]
            pixel_map[i][j] = [pixel[0]/255, pixel[1]/255, pixel[2]/255]
    return pixel_map


def find_closest_value(value, interval):
    candidates = [i / interval for i in range(interval+1)]
    return min(candidates, key=lambda x:abs(x-value))


def process_image(image_path, output_path, color_interval):
    pixel_map = get_pixel_map(image_path)
    dithered_pixel_map = dithering(pixel_map, color_interval)

    height = len(dithered_pixel_map)
    width = len(dithered_pixel_map[0])

    new_image = Image.new('RGB', (width, height))
    pixels = new_image.load()
    for y in range(height):
        for x in range(width):
            r = round(dithered_pixel_map[y][x][0] * 255)
            g = round(dithered_pixel_map[y][x][1] * 255)
            b = round(dithered_pixel_map[y][x][2] * 255)
            pixels[x, y] = (r, g, b)
    new_image.save(output_path)


process_image("096-floyd-steinberg/kiki.png", "096-floyd-steinberg/kiki-dithered-rgb.png", 1)
