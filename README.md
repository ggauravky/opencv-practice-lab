<div align="center">

# 🎯 OpenCV Practice Lab

![OpenCV](https://img.shields.io/badge/OpenCV-27338e?style=for-the-badge&logo=OpenCV&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-00D26A?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

**Master Computer Vision from Scratch to Advanced**

_A complete, hands-on journey through OpenCV fundamentals_

[🚀 Getting Started](#-getting-started) • [📚 Modules](#-course-modules) • [💻 Examples](#-code-examples) • [🤝 Connect](#-connect-with-me)

</div>

---

## 🎓 About This Course

This repository documents my complete journey learning **OpenCV** - from basic image operations to advanced real-time face detection. Each module contains practical examples and working code, progressing from fundamentals to production-ready computer vision applications.

**What's Inside:** 8 Modules • 19 Projects • Fully Completed ✨

---

## 📚 Course Modules

<table>
<tr>
<td width="50%" valign="top">

### 🔰 Fundamentals

- **Module 01** - Setup & Basics
- **Module 02** - Image Transformations
- **Module 03** - Drawing Techniques
- **Module 04** - Video Processing

</td>
<td width="50%" valign="top">

### 🚀 Advanced

- **Module 05** - Filtering & Blurring
- **Module 06** - Edge Detection & Thresholding
- **Module 07** - Contours & Shape Recognition
- **Module 08** - Face & Object Detection

</td>
</tr>
</table>

### 🎯 Skills Mastered

```
✅ Image I/O & Manipulation          ✅ Real-time Video Processing
✅ Geometric Transformations          ✅ Edge & Contour Detection
✅ Color Space Conversions            ✅ Shape Recognition Algorithms
✅ Filtering & Noise Reduction        ✅ Haar Cascade Classifiers
✅ Drawing & Text Overlay             ✅ Multi-feature Face Detection
```

---

## 🚀 Getting Started

### Prerequisites

```bash
pip install opencv-python numpy
```

### Quick Run

```bash
# Basic image processing
python "001 Getting Ready for OpenCV/main.py"

# Shape detection
python "007 Contours & Shape Detection/contour_fun.py"

# Face detection (with smile & eye detection)
python "008 Face & Object Detection/app.py"
```

---

## 💻 Code Examples

### 📸 Load & Display

```python
import cv2
img = cv2.imread("image.jpg")
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

### 🔄 Transform & Rotate

```python
# Resize
resized = cv2.resize(img, (800, 600))

# Rotate 45 degrees
center = (w//2, h//2)
matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(img, matrix, (w, h))
```

### 🎭 Detect Faces & Smiles

```python
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        roi_gray = gray[y:y+h, x:x+w]
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.8, 20)
        if len(smiles) > 0:
            cv2.putText(frame, "Smiling :)", (x, y+h+25),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

    cv2.imshow("Face Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

---

## 🗂️ Project Structure

```
📦 OpenCV Practice Lab
├─ 📁 001 Getting Ready for OpenCV      → Setup & basics
├─ 📁 002 Image Transformations         → Resize, crop, rotate, flip
├─ 📁 003 Basic Image Drawing           → Shapes, lines, text
├─ 📁 004 Video Function                → Video capture & saving
├─ 📁 005 Image Filtering & Blurring    → Gaussian, median, sharpening
├─ 📁 006 Edge Detection & Thresholding → Canny, thresholding, bitwise ops
├─ 📁 007 Contours & Shape Detection    → Shape recognition & analysis
├─ 📁 008 Face & Object Detection       → Haar cascades, smile & eye detection
├─ 📄 LICENSE                           → MIT License
└─ 📄 README.md                         → This file
```

---

## 🛠️ Tech Stack

<div align="center">

![Python](https://skillicons.dev/icons?i=python)
![OpenCV](https://skillicons.dev/icons?i=opencv)
![NumPy](https://skillicons.dev/icons?i=numpy)
![VS Code](https://skillicons.dev/icons?i=vscode)
![Git](https://skillicons.dev/icons?i=git)

|      Tool      | Purpose                                    |
| :------------: | :----------------------------------------- |
| **Python 3.x** | Core programming language                  |
|   **OpenCV**   | Computer vision & image processing library |
|   **NumPy**    | Numerical computing & array operations     |
|  **VS Code**   | Development environment                    |
|    **Git**     | Version control                            |

</div>

---

## 📖 Resources

- **OpenCV Docs**: [docs.opencv.org](https://docs.opencv.org/)
- **Python Tutorials**: [OpenCV Python Tutorials](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html)

---

## 🤝 Connect With Me

<div align="center">

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/gauravky/)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ggauravky)
[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/the_gau_rav/)

</div>

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**⭐ If this helped you learn OpenCV, give it a star!**

_Made with ❤️ and lots of ☕ | Course Completed December 2025_

**Happy Coding! 🚀**

</div>
