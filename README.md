# Virtual Number Plate of South Korea

### [Kor](README.md) | [Eng](README_eng.md)



**가상 차량 번호판 생성 프로그램**으로 AI 번호판 인식 데이터셋 생산을 위해 작성하였다.



## 사용 라이브러리

- **tqdm**: 진행상황 시각화 용도 
   `pip install tqdm `
- **PIL**: 번호판 이미지 처리 용도
  `pip install pillow`
- **argparse**: 이미지 경로, 갯수, 설정 용도
  `pip install argparse`



## 실행법

1. 한길체 폰트 [다운로드](https://www.juso.go.kr/notice/NoticeBoardDetail.do?mgtSn=44&currentPage=11&searchType=&keyword=)
2. Noto Sans KR [다운로드](https://fonts.google.com/noto/specimen/Noto+Sans+KR) (NotoSansKR-Medium 사용)
3. 번호판 템플릿 이미지를 다운받아 `image` 폴더에 저장
   [`number_plate_old.png`](https://github.com/Oh-JongJin/Virtual_Number_Plate/releases/download/v0.1/number_plate_old.png) [`number_plate_new.png`](https://github.com/Oh-JongJin/Virtual_Number_Plate/releases/download/v0.1/number_plate_new.png)

---

기본 실행 형태 -

```bash
python run.py
```

위 실행 결과는 3종류의 번호판이 `result` 폴더에 각각 100개씩 저장된다.



Argparse를 사용한 실행 형태 - 

```bash
python run.py --count 50 --save-path output_images
```

`count`를 통해 저장되는 이미지 갯수를 조절할 수 있으며, `save-path`로 저장할 폴더 이름을 설정 할 수 있다.



## 결과 이미지

`run.py` 실행 시 해당 경로에 결과 이미지 저장 폴더가 생성되며, 그 내부에 각각 종류별로 랜덤한 번호를 가진 번호판 이미지가 저장된다.

| ![539보 2556](https://user-images.githubusercontent.com/45455262/234182656-eb640ab9-f48d-474b-9432-868a9c1b6ac8.png) | ![10구 4730](https://user-images.githubusercontent.com/45455262/234182518-3220eb12-6ffa-4e67-bac8-92aeb5d188c5.png) | ![147허 8450](https://user-images.githubusercontent.com/45455262/234182677-c3e624ed-cf1f-4d37-a539-99c5b31627e0.png) |
| :--------------------------------------: | :--------------------------------------: | :--------------------------------------: |
|                신형 8자리 번호판                |                구형 7자리 번호판                |                구형 8자리 번호판                |
