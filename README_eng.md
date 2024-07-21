# Virtual Number Plate of South Korea

### [Kor](README.md) | [Eng](README_eng.md)


This project is created for production of AI license plate recognition datasets as a virtual license plate generation program.



## Environments

- **Python==3.9.13**

- **tqdm==4.66.1**: Progress visualization usage
- **pillow==10.1.0**: License plate image processing usage
- **urllib.request**
- **colorama**



```bas
pip install tqdm pillow
```





## Run

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





## TODO

Create a virtual vehicle image using `Stable Diffusion` and insert the virtual license plate above.

Model, LoRA required for vehicle image generation.



2024/03/28 - Generate virtual vehicle images using Stable Diffusion. The fidelity of the vehicle implementation is low.
2024/03/29 - Creating an LP Segmentation Dataset.





- [ ] 2024/03/28 ~ : Generate virtual vehicle images using Stable Diffusion. The fidelity of the vehicle implementation is low.
- [x] 2024/03/29 : Creating an LP Segmentation Dataset ([Roboflow workspace](https://app.roboflow.com/jongjin-ohknife/lpr_seg/1))
- [x] 2024/07/21 : Exclude download task and automate initial setup
