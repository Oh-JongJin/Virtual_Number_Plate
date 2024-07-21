# Virtual Number Plate of South Korea

### [Kor](README.md) | [Eng](README_eng.md)



**가상 차량 번호판 생성 프로그램**으로 AI 번호판 인식 데이터셋 생산을 위해 작성하였다.



## 사용 환경

- **Python==3.9.13**

- **tqdm==4.66.1**: 진행상황 시각화 용도 
- **PIL==10.1.0**: 번호판 이미지 처리 용도
- **urllib.request**: 번호판 배경 이미지 다운로드 용도
- **colorama==0.4.6**: 콘솔 출력 가시성 향상 용도



```bash
pip install tqdm pillow
```





## 실행법

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





## TODO

`Stable Diffusion` 사용하여 가상의 차량 이미지 생성 후, 위의 가상 번호판 삽입.

차량 이미지 생성에 필요한 Model, LoRA 필요.

 

- [ ] 2024/03/28 ~ : SD 사용 가상 차량 이미지 생성. 하지만 차량 구현율 낮음
- [x] 2024/03/29 : LP Segmentation Dataset 제작 ([Roboflow workspace](https://app.roboflow.com/jongjin-ohknife/lpr_seg/1))
- [x] 2024/07/21 : 다운로드 작업 제외 및 초기 설정 자동화
