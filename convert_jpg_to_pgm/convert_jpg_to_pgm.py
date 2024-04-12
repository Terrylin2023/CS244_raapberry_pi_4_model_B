import sys
from PIL import Image

def convert_jpg_to_pgm(jpg_file):
    # Generate PGM file name based on input file name.
    pgm_file = jpg_file.replace('.jpg', '.pgm').replace('.jpeg', '.pgm')
    
    # Open JPEG image files
    with Image.open(jpg_file) as img:
        # Convert image to grayscale
        img = img.convert('L')
        # Save images in PGM format
        img.save(pgm_file, 'PPM')
    print(f"Converted {jpg_file} to {pgm_file}")

if len(sys.argv) != 2:
    print("Usage: python3 convert_jpg_to_pgm.py input.jpg")
    sys.exit(1)

input_file = sys.argv[1]

convert_jpg_to_pgm(input_file)
