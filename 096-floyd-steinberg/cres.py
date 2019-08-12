import importlib

print("Generating rgb dithering")
importlib.import_module("cres-rgb.py")

print("Generating grayscale dithering")
importlib.import_module("cres-grayscale.py")
