#!/bin/bash

echo "step 1: Download dataset"
curl -o iris.csv https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv

echo "step 2: Preprocessing (just preview for now)"
head -n 5 iris.csv

echo  "step 3: Train model"
python train.py

echo "Pipeline complete ✅"

