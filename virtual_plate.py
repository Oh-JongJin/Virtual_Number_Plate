# https://scorchingnraining.tistory.com/31

import os
import random
import sys

from tqdm import tqdm
from PIL import Image, ImageDraw, ImageFont

list_A = []
number = '0123456789'
for num in number:
    list_A.append(num)  # 번호판의 숫자를 담은 리스트
list_B = []
korean = '가나다라마바사아자' \
         '거너더러머버서어저' \
         '고노도로모보소오조' \
         '구누두루무부수우주' \
         '하허호'
count = 9899  # 각각 몇개 만들꺼임?

os.makedirs('virtual/new8', exist_ok=True)
os.makedirs('virtual/old8', exist_ok=True)
os.makedirs('virtual/old7', exist_ok=True)

for kor in korean:
    list_B.append(kor)  # 번호판의 문자를 담은 리스트
    
# 한글 문자 폰트 정보
ko_font = ImageFont.truetype('C:/Users/user/AppData/Local/Microsoft/Windows/Fonts/한길체.ttf',
                             100, encoding='unic')
# 숫자 폰트 정보
font = ImageFont.truetype('C:/Users/user/AppData/Local/Microsoft/Windows/Fonts/NotoSansKR-Medium.otf',
                          120, encoding='unic')

# 8자리 신형 번호판
# for i in range(count):
for i in tqdm(range(count), desc='8자리 신형 번호판'):
    front = f'{random.randint(100, 999)}'
    middle = random.choice(korean)
    back = f' {random.randint(1000, 9999)}'
    full_name = front + middle + back

    path = 'license_plate_cp.png'  # 번호판 배경 이미지

    image_pil = Image.open(path)
    draw = ImageDraw.Draw(image_pil)
    draw.text((85, -20), front, 'black', font)  # (x,y), 번호판 문자열, 폰트 색, 위에서 설정한 폰트
    draw.text((290, 35), middle, 'black', ko_font)
    draw.text((375, -20), back, 'black', font)

    image_pil.save('virtual/new8/' + full_name + '.png', 'PNG')


# 8자리 예전 번호판
for i in tqdm(range(count), desc='8자리 이전 번호판'):
    front = f'{random.randint(100, 999)}'
    middle = random.choice(korean)
    back = f' {random.randint(1000, 9999)}'
    full_name = front + middle + back

    path = 'license_plate.png'

    image_pil = Image.open(path)
    draw = ImageDraw.Draw(image_pil)
    draw.text((40, -20), front, 'black', font)  # (x,y), 번호판 문자열, 폰트 색, 위에서 설정한 폰트
    draw.text((245, 35), middle, 'black', ko_font)
    draw.text((340, -20), back, 'black', font)

    image_pil.save('virtual/old8/' + full_name + '.png', 'PNG')


# 7자리 예전 번호판
for i in tqdm(range(count), desc='7자리 이전 번호판'):
    front = f'{random.randint(10, 99)}'
    middle = random.choice(korean)
    back = f' {random.randint(1000, 9999)}'
    full_name = front + middle + back

    path = 'license_plate.png'

    image_pil = Image.open(path)
    draw = ImageDraw.Draw(image_pil)
    draw.text((65, -20), front, 'black', font)  # (x,y), 번호판 문자열, 폰트 색, 위에서 설정한 폰트
    draw.text((205, 30), middle, 'black', ko_font)
    draw.text((315, -20), back, 'black', font)

    image_pil.save('virtual/old7/' + full_name + '.png', 'PNG')
