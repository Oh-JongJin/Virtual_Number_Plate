#!/usr/bin/env python3
#
# Authors:
#   5jx2oh@gmail.com
#
# Reference:
#   https://scorchingnraining.tistory.com/31


import os
import sys
import time
import json
import random
import argparse
import urllib.request

from tqdm import tqdm
from colorama import Fore, Style, Back
from PIL import Image, ImageDraw, ImageFont


# Hangul Classification Used for Vehicle License Plates
korean = '가나다라마' \
         '거너더러머버서어저' \
         '고노도로모보소오조' \
         '구누두루무부수우주'
korean_taxi = '바사아자'
korean_rent = '하허호'
korean_parcel = '배'

os.makedirs('images', exist_ok=True)
new_img_path = 'images/number_plate_new.png'
old_img_path = 'images/number_plate_old.png'
# Proceed with the download if the background image is missing
if os.path.isfile(new_img_path) and os.path.isfile(old_img_path):
    pass
else:
    with open('images_url.json', 'r') as f:
        data = json.load(f)
    for fname in data:
        print(f'Download {Fore.GREEN + fname}{Style.RESET_ALL}.png image file in images/.')
        urllib.request.urlretrieve(data[fname], f'images/{fname}.png')

# Hangil font variable declare
hangil_font = ImageFont.truetype('fonts/Hangil.ttf', 100, encoding='unic')

# Noto Sans font variable declare
notosans_font = ImageFont.truetype('fonts/NotoSansKR-Medium.ttf', 120, encoding='unic')


def run(opts):
    count, save_path = opts.count, opts.save_path

    start = time.time()

    # Make folder to saving outputs
    os.makedirs(f'{save_path}/new8', exist_ok=True)
    os.makedirs(f'{save_path}/old8', exist_ok=True)
    os.makedirs(f'{save_path}/old7', exist_ok=True)

    # 8-digit license plate with holographic
    for i in tqdm(range(count), desc='8-digit license plate(holographic)'):
        front = f'{random.randint(100, 999)}'
        middle = random.choice(korean)
        back = f' {random.randint(1000, 9999)}'
        full_name = front + middle + back

        image_pil = Image.open(new_img_path)
        draw = ImageDraw.Draw(image_pil)
        # draw.text( (x,y), License plate string, Font color, Font )
        draw.text((85, -20), front, 'black', notosans_font)
        draw.text((290, 35), middle, 'black', hangil_font)
        draw.text((375, -20), back, 'black', notosans_font)

        image_pil.save(f'{save_path}/new8/' + full_name + '.png', 'PNG')

    # 8-digit license plate
    for i in tqdm(range(count), desc='8-digit license plate'):
        front = f'{random.randint(100, 999)}'
        middle = random.choice(korean)
        back = f' {random.randint(1000, 9999)}'
        full_name = front + middle + back

        image_pil = Image.open(old_img_path)
        draw = ImageDraw.Draw(image_pil)
        draw.text((40, -20), front, 'black', notosans_font)
        draw.text((245, 35), middle, 'black', hangil_font)
        draw.text((340, -20), back, 'black', notosans_font)

        image_pil.save(f'{save_path}/old8/' + full_name + '.png', 'PNG')

    # 7-digit license plate
    for i in tqdm(range(count), desc='7-digit license plate'):
        front = f'{random.randint(10, 99)}'
        middle = random.choice(korean)
        back = f' {random.randint(1000, 9999)}'
        full_name = front + middle + back

        image_pil = Image.open(old_img_path)
        draw = ImageDraw.Draw(image_pil)
        draw.text((65, -20), front, 'black', notosans_font)
        draw.text((205, 30), middle, 'black', hangil_font)
        draw.text((315, -20), back, 'black', notosans_font)

        image_pil.save(f'{save_path}/old7/' + full_name + '.png', 'PNG')

    print(f'Done. ({round(time.time() - start, 3)}s)')  # Spending time


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--count', type=int, default=10, help='Number of image to save')
    parser.add_argument('--save-path', type=str, default='result', help='Output path')
    opt = parser.parse_args()

    run(opts=opt)
