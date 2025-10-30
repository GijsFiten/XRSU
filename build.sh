#!/bin/bash

# This scripts calls the build scripts for both Implicit3DUnderstanding and ThreeDSceneFormer which were already provided
# It's also possible to share the LDIF build between both projects to avoid building it twice, but for simplicity we just build both here.

cd Implicit3DUnderstanding
python project.py build

cd ../ThreeDSceneFormer
python project.py build