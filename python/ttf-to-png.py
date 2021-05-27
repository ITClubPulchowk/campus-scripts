from PIL import Image, ImageFont, ImageDraw
import argparse
import sys

"""
        Python Script to convert a .ttf file into a .png file

        Pass path to a .ttf file to this script and it should give you an out.png file in the directory where you ran it from.
        Unless you specify a output path that is.

        Examples:

        Command: python ttf-to-png.py ./some_font.ttf
        Command: python ttf-to-png.py ~/fonts/ttf/someotherfont.ttf -o ~/project -f 128
"""
parser = argparse.ArgumentParser(
    allow_abbrev=True, formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("font", help="path to .ttf file\nPath can be absolute or relative to where you're running this script from.", type=str)
parser.add_argument("-s", "--start", help="starting ascii character (default 32)", type=int)
parser.add_argument("-e", "--end", help="ending ascii character (default 128)", type=int)
parser.add_argument("-r", "--rows", help="no of rows to divide the font into (default 2)",type=int)
parser.add_argument("-f", "--fontsize", help="size of font (default 24)", type=int)
parser.add_argument("-a", "--aspectratio", help="aspect ratio of the font (default 0.5)", type=float)
parser.add_argument("-o", "--outfile", help="name/path of the output file (default out.png)", type=str)
# For displaying help message even if no argument is passed
if len(sys.argv) == 1:
    parser.print_help(sys.stderr)
    sys.exit(1)
args = parser.parse_args()

if args.start: start = args.start
else: start = 32
if args.end: end = args.end
else: end = 128
if args.rows: rows = args.rows
else: rows = 2
if args.fontsize: size = args.fontsize
else: size = 24
if args.aspectratio: ratio = args.aspectratio
else: ratio = 0.5
if args.outfile: outfile = args.outfile
else: outfile = 'out.png'
font = args.font

interval = (end - start) // rows

img = Image.new('RGBA', (int((end - start) * size // rows * ratio), size * rows + rows))
draw = ImageDraw.Draw(img)
font = ImageFont.truetype(font, size)
y = -1
x = 0
for i in range(start, end):
    if (i - start) % interval == 0:
        y += 1
        x = 0
    draw.text((x * size * ratio, y * size), chr(i),
              (255, 255, 255, 255), font=font)
    x += 1
img.save(outfile)