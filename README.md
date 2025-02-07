# python_course
## Course 1
[基本的openCV影像處理教學影片](https://www.youtube.com/watch?v=oXlwWbU8l2o&t=2801s&ab_channel=freeCodeCamp.org)

| 檔案名稱 .py      | 功能                                                       |
|----------------|--------------------------------------------------------------|
| basic          | 灰階、高斯模糊、Canny 邊緣偵測、侵蝕、膨脹、調整大小、影像裁切    |
| bitwise        | 兩張影像 (OR、AND、XOR、NOT)                                  |
| colorSpace     | 色彩空間轉換                                                  |
| contours       | 二值化                                                       |
| draw           | 在圖片上畫線、矩形、圓形，並可加入文字                       |
| gradients      | 影像梯度 (Laplace、Sobel、Canny)                             |
| masking        | 建立影像遮罩並應用於圖片                                     |
| rescale        | 影像及影片縮放                                               |
| smoothing      | 平滑影像 (Average、Gaussian、Median、Bilateral)               |
| splitmerge     | 分離彩色影像的 BGR 通道並合併回彩色影像                       |
| thresh         | 二值化方法 (threshold、adaptive、adaptive(Guassian))         |
| transformation | 影像的平移、旋轉、水平及垂直翻轉                             |
| histogram      | 影像直方圖                                                   |

## Course 2
opencv [臉部辨識](https://github.com/opencv/opencv/tree/4.x/data/haarcascades)

OpenCV臉部辨識模型為.xml格式
1. face_recognition -> 讀取訓練好的模型，開始辨識
2. faces_train -> 創建訓練資料(features, labels)，成.npy檔，並用模型訓練，訓練好的結果存成.yml檔
3. face_detect -> 使用openCV 開源模型讀取(.xml)、及模型使用

## Deep Learning

[Caer](https://gitcode.com/gh_mirrors/ca/caer/?utm_source=artical_gitcode&index=bottom&type=card&webUrl) 為開源資料庫，提供實用的功能，包括影像處理、影片處理、特徵提取、對象檢測

[canaro](https://github.com/jasmcaus/canaro)
Python庫，包括使用Keras框架建立的深度學習模型的支持


[kaggle](https://www.kaggle.com/)
為機器學習打造的網站(包含model、Datasets、notebook)
1. [新建notebook](https://www.kaggle.com/notebooks)
2. 辦理帳號並至Setting，手機認證
