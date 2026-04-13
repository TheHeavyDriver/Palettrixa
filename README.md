# 🎨 Palettrixa — Color Palette Generator from Images

Palettrixa is a full-stack web application that extracts dominant color palettes from images and analyzes their accessibility. Upload an image to instantly generate a palette along with contrast information for design usability.

## 💻 Screenshots
<img width="1866" height="998" alt="image" src="https://github.com/user-attachments/assets/369bf684-1695-4bce-a823-c5a4d2744a66" />
<img width="1866" height="1002" alt="image" src="https://github.com/user-attachments/assets/8d6b0e72-8d29-4882-962b-752a8b7591ed" />


## ✨ Features

- Upload images (drag & drop or file upload)

- Extract dominant colors using LAB color clustering

- Sort colors by dominance

- WCAG contrast analysis for accessibility

- Copy HEX colors instantly

- Fast image processing using FastAPI

## 🛠 Tech Stack

### Frontend

- Next.js

- React

- TailwindCSS

- TypeScript

- Backend

- FastAPI

- Python

- NumPy

- Pillow

### Deployment

- Frontend: Vercel

- Backend: Render

## 🧠 How It Works

- User uploads an image.

- The image is sent to the FastAPI backend.

- Pixels are converted from RGB → LAB color space.

- K-Means clustering extracts dominant colors.

- Colors are sorted by frequency and returned to the frontend.

- The UI displays the palette along with contrast analysis and copy feature.

## 🚀 Live Demo

### Frontend

```
https://palettrixa.vercel.app/
```

### Backend API

```
https://palettrixa.onrender.com
```
## ⚙️ Local Setup
### Clone the repository
```
git clone https://github.com/yourusername/palettrixa.git
cd palettrixa
```
### Backend
```
cd backend
python -m venv venv
source venv/bin/activate

pip install -r requirements.txt

uvicorn main:app --reload
```
Backend runs on:

```
http://localhost:8000
```
### Frontend
```cd frontend
npm install
npm run dev
```

Frontend runs on:

```
http://localhost:3000
```
## 📂 Project Structure
```
color-palette-generator
│
├── frontend
│   ├── src/components
│   ├── src/utils
│   └── src/types
│
├── backend
│   ├── main.py
│   └── requirements.txt
```
