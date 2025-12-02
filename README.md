<h1 align="center">🎯 OpenCV Practice Lab</h1>

<p align="center">
  <img src="https://img.shields.io/badge/OpenCV-27338e?style=for-the-badge&logo=OpenCV&logoColor=white" alt="OpenCV">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy">
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="License">
</p>

<p align="center">
  <em>🚀 A hands-on journey through Computer Vision fundamentals with OpenCV 🔍</em>
</p>

---

## 📚 What's Inside

> **A comprehensive, structured learning path** covering essential OpenCV techniques - from basic image operations to advanced contour detection. Each module builds upon the previous one, creating a solid foundation in computer vision.

### 🗂️ Module Overview

```
📦 OpenCV Practice Lab
├─ 📁 001 Getting Ready for OpenCV      → Setup & basics
├─ 📁 002 Image Transformations         → Resize, crop, rotate, flip
├─ 📁 003 Basic Image Drawing           → Shapes, lines, text
├─ 📁 004 Video Function                → Video capture & saving
├─ 📁 005 Image Filtering & Blurring    → Gaussian, median, sharpening
├─ 📁 006 Edge Detection & Thresholding → Canny, thresholding, bitwise ops
└─ 📁 007 Contours & Shape Detection    → Shape recognition & analysis
```

### 🎨 Key Skills Covered

<table>
<tr>
<td width="50%">

**🖼️ Image Processing**

- ✅ Read, write, display images
- ✅ Color space conversions
- ✅ Resize, crop, rotate, flip
- ✅ Drawing shapes & text overlay

</td>
<td width="50%">

**🔬 Advanced Techniques**

- ✅ Gaussian & median blur
- ✅ Image sharpening
- ✅ Canny edge detection
- ✅ Thresholding & bitwise operations

</td>
</tr>
<tr>
<td width="50%">

**🎥 Video Processing**

- ✅ Camera capture
- ✅ Video reading & writing
- ✅ Real-time processing

</td>
<td width="50%">

**🎯 Shape Detection**

- ✅ Contour detection
- ✅ Shape recognition
- ✅ Polygon approximation

</td>
</tr>
</table>

---

## 🚀 Quick Start

### Prerequisites

```bash
pip install opencv-python numpy
```

### Run Any Example

```bash
python "001 Getting Ready for OpenCV/main.py"
python "007 Contours & Shape Detection/contour_fun.py"
```

---

## 💡 Sample Code Snippets

<details>
<summary><b>🖼️ Load & Display Image</b></summary>

```python
import cv2

img = cv2.imread("image.jpg")
cv2.imshow("Window", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

</details>

<details>
<summary><b>🔄 Image Transformation</b></summary>

```python
# Resize
resized = cv2.resize(img, (800, 600))

# Rotate
center = (w//2, h//2)
matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(img, matrix, (w, h))

# Flip
flipped = cv2.flip(img, 1)  # horizontal flip
```

</details>

<details>
<summary><b>🎭 Shape Detection</b></summary>

```python
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150)
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.03 * cv2.arcLength(contour, True), True)
    corners = len(approx)
    # Identify shape based on corners
```

</details>

---

## 🎓 Learning Path

<div align="center">

```mermaid
graph LR
    A[🎬 Start] --> B[001 Setup & Basics]
    B --> C[002-003 Transformations & Drawing]
    C --> D[004-005 Video & Filtering]
    D --> E[006-007 Edge Detection & Contours]
    E --> F[🎉 Computer Vision Pro!]

    style A fill:#27338e,stroke:#fff,color:#fff
    style F fill:#00D26A,stroke:#fff,color:#fff
```

</div>

**💡 Pro Tips:**

- 🔹 Work through modules sequentially for best results
- 🔹 Experiment with different parameters and images
- 🔹 Break things and learn from errors!
- 🔹 Build your own projects using learned techniques

---

## 🛠️ Tech Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,opencv,numpy,vscode,git" alt="Tech Stack" />
</p>

<div align="center">

|   Technology   | Purpose                               |
| :------------: | :------------------------------------ |
| **Python 3.x** | Core programming language             |
|   **OpenCV**   | Computer vision & image processing    |
|   **NumPy**    | Numerical operations & array handling |
|  **VS Code**   | Development environment               |

</div>

---

## 📖 Resources

- [OpenCV Documentation](https://docs.opencv.org/)
- [OpenCV Python Tutorials](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html)

---

## 🤝 Connect With Me

<p align="center">
  <a href="https://www.linkedin.com/in/gauravky/">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn">
  </a>
  <a href="https://github.com/ggauravky">
    <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
  </a>
  <a href="https://www.instagram.com/the_gau_rav/">
    <img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white" alt="Instagram">
  </a>
</p>

---

## 📄 License

<p align="center">
  This project is licensed under the <b>MIT License</b> - see the <a href="LICENSE">LICENSE</a> file for details.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge" alt="License: MIT">
</p>

---

<div align="center">

### ⭐ If you find this helpful, give it a star

**Made with ❤️ and lots of ☕**

_Happy Coding! 🚀_

</div>
