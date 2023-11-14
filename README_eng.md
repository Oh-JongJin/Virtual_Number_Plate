# Virtual Number Plate

### [Kor](README.md) | [Eng](README_eng.md)


When `virtual_plate.py` is executed, a `virtual` folder is created in the path, and license plate images with random numbers for each type are stored inside.



## Install

- **tqdm**: Progress visualization usage
   `pip install tqdm `
- **PIL**: License plate image processing usage
  `pip install pillow`
- **argparse**: Image path, numbers, and setting usage
  `pip install argparse`



## Usage

[`number_plate_old.png`](https://github.com/Oh-JongJin/Virtual_Number_Plate/releases/download/v0.1/number_plate_old.png) [`number_plate_new.png`](https://github.com/Oh-JongJin/Virtual_Number_Plate/releases/download/v0.1/number_plate_new.png)

```
python virtual_plate.py --new-plate number_plate_new.png --old-plate number_plate_old.png --count 50
```



## Results

| ![539보 2556](https://user-images.githubusercontent.com/45455262/234182656-eb640ab9-f48d-474b-9432-868a9c1b6ac8.png) | ![10구 4730](https://user-images.githubusercontent.com/45455262/234182518-3220eb12-6ffa-4e67-bac8-92aeb5d188c5.png) | ![147허 8450](https://user-images.githubusercontent.com/45455262/234182677-c3e624ed-cf1f-4d37-a539-99c5b31627e0.png) |
| :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
|         **8-digit** License plate<br />(holographic)         |                  **7-digit** License plate                   |                  **8-digit** License plate                   |

