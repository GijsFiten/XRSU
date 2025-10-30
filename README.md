# XR-Scene-Understanding (XRSU)

This is the repository accompanying 'XR-Scene-Understanding: Distributed Deep Learning Based Holistic Scene Understanding for Extended Reality Applications' 

## Install

Please make sure to install CUDA NVCC on your system first. then run the following:
```
sudo apt install xvfb ninja-build freeglut3-dev libglew-dev meshlab
conda env create -f environment.yaml
conda activate hsu
chmod +x ./build.sh
./build.sh
```
When running ```build.sh```, the script will run ```external/build_gaps.sh``` which requires password for sudo privilege for ```apt-get install```.
Please make sure you are running with a user with sudo privilege.

Should you run into build errors, check that the correct NVIDIA compute capability is set in the CMakeLists.txt file in each of the external/ldif folders.
This repository contains a few submodules, which I have just added as files here, this is not ideal but it makes the build stable. Please manually setup the file structure if you want to use this repository in a serious setting.

## Data

The model checkpoints and nevessary data is provided on [Google Drive](https://drive.google.com/file/d/19FCQY0RVHrqbT7aR5_y30POhe3Z-v6iF/view?usp=sharing). Extract XRSU.zip in the root of this project, everything should then be placed in the correct subdirectories.

## Run

The server runs on a basic Flask implemetation. Only two parameters are accepted, --hsu_model and --bb_model to select the HSU mdoel and 2D Bounding Box detector respectively.
It will start a server bound to port 5000, accepting connections from localhost. This implementation works as a proof of concept, but should not be implemented as is in a production environment.

Accepted HSU models: ThreeDSceneFormer, Total3DUnderstanding, Implicit3DUnderstanding
Accepted 2D bounding box detectors: Resnet50, Mobilenetv2, DETR

```
conda activate hsu
python server.py --hsu_model ThreeDSceneFormer --bb_model Resnet50
```

Supported endpoints:
- ```/health``` : GET or HEAD - Always returns 200 of the server is running
- ```/upload``` : POST - Checks for the presence of the correct files, runs through the pipeline, return the resulting files and 200 in case of no errors.

## Client

The client will run over the 100 images provided in sample_images to test the performance of the system. This python file is not necessary, any POST request containing the image and a cam_k file will do.

## Unity

A unity proof of concept program is provided using Sharepoint. Make sure to configure the server IP and port in the orchestrator GameObject.

