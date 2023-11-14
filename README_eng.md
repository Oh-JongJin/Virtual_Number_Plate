# Virtual Number Plate

### [Kor](README.md) | [Eng](README_eng.md)


When `virtual_plate.py` is executed, a `virtual` folder is created in the path, and license plate images with random numbers for each type are stored inside.



## 사용 라이브러리

- **tqdm**: 진행상황 시각화 용도 
   `pip install tqdm `
- **PIL**: 번호판 이미지 처리 용도
  `pip install pillow`
- **argparse**: 이미지 경로, 갯수, 설정 용도
  `pip install argparse`

## 실행법

[`number_plate_old.png`](https://github.com/Oh-JongJin/Virtual_Number_Plate/releases/download/v0.1/number_plate_old.png) [`number_plate_new.png`](https://github.com/Oh-JongJin/Virtual_Number_Plate/releases/download/v0.1/number_plate_new.png)

```
python virtual_plate.py --new-plate number_plate_new.png --old-plate number_plate_old.png --count 50
```

## 실행 결과
| ![539보 2556](https://user-images.githubusercontent.com/45455262/234182656-eb640ab9-f48d-474b-9432-868a9c1b6ac8.png) | ![10구 4730](https://user-images.githubusercontent.com/45455262/234182518-3220eb12-6ffa-4e67-bac8-92aeb5d188c5.png) | ![147허 8450](https://user-images.githubusercontent.com/45455262/234182677-c3e624ed-cf1f-4d37-a539-99c5b31627e0.png) |
| :--------------------------------------: | :--------------------------------------: | :--------------------------------------: |
|                신형 8자리 번호판                |                구형 7자리 번호판                |                구형 8자리 번호판                |
