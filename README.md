# 🐱 vs 🐶 Classifier: A Deep Learning Adventure

![CNN Architecture](https://miro.medium.com/max/1400/1*uAeANQIOQPqWZnnuH-VEyw.jpeg)  
*Classifying cats and dogs with the power of Convolutional Neural Networks!*

## 🚀 Overview
This project is a deep learning-powered image classifier that can distinguish between our furry friends - cats and dogs! Built using TensorFlow and Keras, this CNN model achieves impressive accuracy in classifying these adorable creatures. The model utilizes transfer learning and modern CNN architectures to provide robust classification capabilities.

## ✨ Features
- 🖼️ Image preprocessing with data augmentation (rotation, scaling, flipping)
- 🧠 Advanced CNN architecture with transfer learning
- 📊 Real-time training and validation metrics tracking
- 🔍 Interactive single image prediction with Streamlit UI
- 📈 Detailed performance visualization (confusion matrix, ROC curves)
- 🚀 Easy-to-use web interface for instant predictions
- 💾 Pre-trained model weights for quick deployment

## 🛠️ Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/SouryaS/cat-dog-classifier.git
   cd cat-dog-classifier
   ```
2. Set up the environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

### 📦 Dependencies
- TensorFlow 2.13.0 - Deep learning framework
- Streamlit 1.24.0 - Web interface
- NumPy 1.24.3 - Numerical computations
- Matplotlib 3.7.1 - Visualization
- Pillow 9.5.0 - Image processing
- TensorFlow Hub 0.14.0 - Transfer learning

### 💻 System Requirements
- Python 3.7 or higher
- 4GB RAM minimum (8GB recommended)
- NVIDIA GPU (optional, for faster training)

## 🏃‍♂️ Usage

### 🗂️ Dataset Organization
```
dataset/
├── training_set/
│   ├── cats/
│   └── dogs/
├── test_set/
│   ├── cats/
│   └── dogs/
└── single_prediction/
    └── cat_or_dog_*.jpg
```

### 🎯 Training the Model
1. Launch the Jupyter notebook:
   ```bash
   jupyter notebook CNNCATDOG.ipynb
   ```
2. Follow the notebook cells to:
   - 🏋️‍ Train the model with your dataset
   - 🧪 Evaluate performance metrics
   - 💾 Save the trained model

### 🚀 Using the Web Interface
1. Start the Streamlit app:
   ```bash
   streamlit run streamlit_app.py
   ```
2. Upload an image through the web interface
3. Get instant predictions with confidence scores

## 📊 Model Architecture & Performance

### 🧠 CNN Architecture
- Input Layer: 224x224x3 RGB images
- Feature Extraction: Transfer learning with pre-trained model
- Custom Layers:
  - Dense layers with ReLU activation
  - Dropout for regularization
  - Binary classification output

### 📈 Performance Metrics
- 🎯 Training accuracy: ~88%
- 🧪 Validation accuracy: ~81%
- 📊 F1-Score: 0.84
- ⚖️ Balanced performance on both classes

## 🤝 Contributing
We welcome contributions! Please follow these steps:
1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📜 License
Distributed under the MIT License. See `LICENSE` for more information.

## 🙏 Acknowledgments
- TensorFlow and Keras for the deep learning framework
- The open-source community for inspiration and support
- All the cats and dogs who unknowingly contributed to this project 🐾