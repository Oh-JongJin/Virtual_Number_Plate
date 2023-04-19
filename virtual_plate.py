# 참고: https://scorchingnraining.tistory.com/31

import os
import random
import time
import argparse

from tqdm import tqdm
from PIL import Image, ImageDraw, ImageFont


# 대한민국 자동차 번호판의 한글 분류
korean = '가나다라마' \
         '거너더러머버서어저' \
         '고노도로모보소오조' \
         '구누두루무부수우주' \
         '하허호'
korean_taxi = '바사아자'
korean_rental = '하허호'
korean_parcel = '배'

# 결과 이미지 저장할 폴더 생성
os.makedirs('virtual/new8', exist_ok=True)
os.makedirs('virtual/old8', exist_ok=True)
os.makedirs('virtual/old7', exist_ok=True)

# 한글 문자 폰트 정보
# https://www.juso.go.kr/notice/NoticeBoardDetail.do?mgtSn=44&currentPage=11&searchType=&keyword=
ko_font = ImageFont.truetype('C:/Users/user/AppData/Local/Microsoft/Windows/Fonts/한길체.ttf',
                             100, encoding='unic')
# 숫자 폰트 정보
# https://fonts.google.com/noto/specimen/Noto+Sans+KR
font = ImageFont.truetype('C:/Users/user/AppData/Local/Microsoft/Windows/Fonts/NotoSansKR-Medium.otf',
                          120, encoding='unic')


def run():
    new_img_path, old_img_path, count = opt.new_plate, opt.old_plate, opt.count
    
    # 소요 시간 체크
    start = time.time()

    # 8자리 신형 번호판
    for i in tqdm(range(count), desc='8자리 신형 번호판'):
        front = f'{random.randint(100, 999)}'
        middle = random.choice(korean)
        back = f' {random.randint(1000, 9999)}'
        full_name = front + middle + back

        image_pil = Image.open(new_img_path)
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

        image_pil = Image.open(old_img_path)
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

        image_pil = Image.open(old_img_path)
        draw = ImageDraw.Draw(image_pil)
        draw.text((65, -20), front, 'black', font)  # (x,y), 번호판 문자열, 폰트 색, 위에서 설정한 폰트
        draw.text((205, 30), middle, 'black', ko_font)
        draw.text((315, -20), back, 'black', font)

        image_pil.save('virtual/old7/' + full_name + '.png', 'PNG')

    print(f'Done. ({round(time.time() - start, 3)}s)')  # 소요 시간


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--new-plate', type=str, default='number_plate_new.png', help='New number plate image file')
    parser.add_argument('--old-plate', type=str, default='number_plate_old.png', help='Old number plate image file')
    parser.add_argument('--count', type=int, default=100, help='Number of images to store')
    opt = parser.parse_args()

    run()
