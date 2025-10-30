# 3D-Scene-Former [[Paper]](https://link.springer.com/article/10.1007/s00371-024-03573-2)

### 3D-Scene-Former: 3D scene generation from a single RGB image using Transformers
Jit Chatterjee, Maria Torres Vega


![pipeline](figures/Pipeline.png)


## Introduction

This repo contains training, testing, evaluation, visualization code of our published journal paper (The Visual Computer, Springer Nature).
Specially, the repo contains our Transformer implementation of the Contextual Refinement Network (CRN).

## Install

Please make sure to install CUDA NVCC on your system first. then run the following:
```
sudo apt install xvfb ninja-build freeglut3-dev libglew-dev meshlab
conda env create -f environment3D.yml
conda activate Env3D
python project.py build
```
When running ```python project.py build```, the script will run ```external/build_gaps.sh``` which requires password for sudo privilege for ```apt-get install```.
Please make sure you are running with a user with sudo privilege.


## Demo
1. Download the [pretrained checkpoint](https://drive.google.com/file/d/1pIezc6QCZxWEm7J7d2KjlWNm12o1Iz6R/view?usp=sharing)
and unzip it into ```out/total3d/transformer_enc_dec/24100215400096/```

2. Change current directory to ```3D_Scene_Former/``` and run the demo, which will generate 3D detection result and rendered scene mesh to ```demo/output/1/```
    ```
    CUDA_VISIBLE_DEVICES=0 python main.py out/total3d/transformer_enc_dec/24100215400096/out_config.yaml --mode demo --demo_path demo/inputs/1
    ```
   
3. In case you want to run it off screen (for example, with SSH)
    ```
    CUDA_VISIBLE_DEVICES=0 xvfb-run -a -s "-screen 0 800x600x24" python main.py out/total3d/transformer_enc_dec/24100215400096/out_config.yaml --mode demo --demo_path demo/inputs/1
    ```
   
4. If you want to run it interactively, change the last line of demo.py
    ```
    scene_box.draw3D(if_save=True, save_path = '%s/recon.png' % (save_path))
    ```
    to
    ```
    scene_box.draw3D(if_save=False, save_path = '%s/recon.png' % (save_path))
    ```


## Citation

If you find our work and code helpful, please cite:
```
Chatterjee, J., Torres Vega, M. 3D-Scene-Former: 3D scene generation from a single RGB image using Transformers. Vis Comput (2024). https://doi.org/10.1007/s00371-024-03573-2
```

We thank the following great works:
- [Implicit3DUnderstanding](https://github.com/chengzhag/Implicit3DUnderstanding) for their well-structured code. We construct our network based on their well-structured code.
- [Total3DUnderstanding](https://github.com/yinyunie/Total3DUnderstanding) for their well-structured code. 
- [Coop](https://github.com/thusiyuan/cooperative_scene_parsing) for their dataset. We used their processed dataset with 2D detector prediction using DETR.
- [LDIF](https://github.com/google/ldif) for their novel representation method. We ported their LDIF decoder from Tensorflow to PyTorch.
- [Transformer](https://github.com/huggingface/transformers) for capturing the scene contextual information. We adopted their Transformer implemention to construct our Contexual Refinement Network(CRN).
- [Occupancy Networks](https://github.com/autonomousvision/occupancy_networks) for their modified version of [mesh-fusion](https://github.com/davidstutz/mesh-fusion) pipeline.

If you find them helpful, please cite:
```
@InProceedings{Zhang_2021_CVPR,
    author    = {Zhang, Cheng and Cui, Zhaopeng and Zhang, Yinda and Zeng, Bing and Pollefeys, Marc and Liu, Shuaicheng},
    title     = {Holistic 3D Scene Understanding From a Single Image With Implicit Representation},
    booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
    month     = {June},
    year      = {2021},
    pages     = {8833-8842}
}
@InProceedings{Nie_2020_CVPR,
    author = {Nie, Yinyu and Han, Xiaoguang and Guo, Shihui and Zheng, Yujian and Chang, Jian and Zhang, Jian Jun},
    title = {Total3DUnderstanding: Joint Layout, Object Pose and Mesh Reconstruction for Indoor Scenes From a Single Image},
    booktitle = {IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
    month = {June},
    year = {2020}
}
@inproceedings{huang2018cooperative,
    title={Cooperative Holistic Scene Understanding: Unifying 3D Object, Layout, and Camera Pose Estimation},
    author={Huang, Siyuan and Qi, Siyuan and Xiao, Yinxue and Zhu, Yixin and Wu, Ying Nian and Zhu, Song-Chun},
    booktitle={Advances in Neural Information Processing Systems},
    pages={206--217},
    year={2018}
}	
@inproceedings{genova2020local,
    title={Local Deep Implicit Functions for 3D Shape},
    author={Genova, Kyle and Cole, Forrester and Sud, Avneesh and Sarna, Aaron and Funkhouser, Thomas},
    booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
    pages={4857--4866},
    year={2020}
}
@inproceedings{transformer,
    title = {Attention is all you need},
    author = {Vaswani, Ashish and Shazeer, Noam and Parmar, Niki and Uszkoreit, Jakob and Jones, Llion and Gomez, Aidan N. and Kaiser, \L{}ukasz and Polosukhin, Illia},
    year = {2017},
    booktitle = {Proceedings of the 31st International Conference on Neural Information Processing Systems},
    pages = {6000–6010},
    numpages = {11},
    series = {NIPS'17}
}
@inproceedings{mescheder2019occupancy,
    title={Occupancy networks: Learning 3d reconstruction in function space},
    author={Mescheder, Lars and Oechsle, Michael and Niemeyer, Michael and Nowozin, Sebastian and Geiger, Andreas},
    booktitle={Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition},
    pages={4460--4470},
    year={2019}
}
```




