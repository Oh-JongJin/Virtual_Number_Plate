# Virtual Number Plate

### [Kor](README.md) | [Eng](README_eng.md)


This project is created for production of AI license plate recognition datasets as a virtual license plate generation program.



## Install

- **tqdm**: Progress visualization usage
   `pip install tqdm `
- **PIL**: License plate image processing usage
  `pip install pillow`
- **argparse**: Image path, numbers, and setting usage
  `pip install argparse`



## Run

1. Hangil Font [Download](https://www.juso.go.kr/notice/NoticeBoardDetail.do?mgtSn=44&currentPage=11&searchType=&keyword=)
2. Noto Sans KR [Download](https://fonts.google.com/noto/specimen/Noto+Sans+KR) (Using NotoSansKR-Medium)
3. Download license plate template image and save it to the `image` folder

[`number_plate_old.png`](https://github.com/Oh-JongJin/Virtual_Number_Plate/releases/download/v0.1/number_plate_old.png) [`number_plate_new.png`](https://github.com/Oh-JongJin/Virtual_Number_Plate/releases/download/v0.1/number_plate_new.png)

---
Default execution - 
```bash
python run.py
```
As a result of the above execution, three types of license plates are stored in the `result` folder by 100 each.


Using Argparse execution - 
```bash
python run.py --count 50 --save-path output_images
```
The number of images stored through the `count` can be adjusted, and the folder name to be stored as the `save-path` can be set.


## Results

When `virtual_plate.py` is executed, a `virtual` folder is created in the path, and license plate images with random numbers for each type are stored inside.

| ![539보 2556](https://user-images.githubusercontent.com/45455262/234182656-eb640ab9-f48d-474b-9432-868a9c1b6ac8.png) | ![10구 4730](https://user-images.githubusercontent.com/45455262/234182518-3220eb12-6ffa-4e67-bac8-92aeb5d188c5.png) | ![147허 8450](https://user-images.githubusercontent.com/45455262/234182677-c3e624ed-cf1f-4d37-a539-99c5b31627e0.png) |
| :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
|         **8-digit** License plate<br />(holographic)         |                  **7-digit** License plate                   |                  **8-digit** License plate                   |

