# ONNX: Model Conversion and Efficient Deployment

## Overview

Machine learning and deep learning models can be developed using a variety of frameworks such as:

- TensorFlow
- Keras
- PyTorch
- Scikit-learn

Although these frameworks are excellent for model development and training, they are often large libraries that consume significant disk space and memory. For example, a TensorFlow installation can occupy around **1.5 GB**.

While this may not be a major issue during development, deployment introduces different priorities where two factors become especially important:

- **Memory consumption**
- **Inference speed**

This is where **ONNX (Open Neural Network Exchange)** becomes valuable.

ONNX is an open standard designed to make machine learning models portable across different frameworks and deployment environments. Instead of deploying a complete training framework such as TensorFlow, a model can be converted into the ONNX format and executed using **ONNX Runtime**, which is lightweight and optimized for high-performance inference.

In addition, ONNX acts as a bridge between different machine learning frameworks, allowing models trained in one framework to be used in another. For example:

```
TensorFlow / Keras
        │
        ▼
      ONNX
        │
        ▼
   ONNX Runtime
```

This approach enables faster inference, lower memory usage, and easier deployment across multiple platforms.

---

## Project Objective

The goal of this repository is to demonstrate a complete deployment workflow by:

- Training a CNN model on the MNIST dataset using TensorFlow/Keras.
- Saving the trained model.
- Converting the Keras model into the ONNX format.
- Running inference using ONNX Runtime.
- Comparing prediction accuracy between the original Keras model and the ONNX model.
- Measuring and comparing the inference time required to predict **1000 samples**.

---

## Repository Structure

```
.
├── mnist_keras.ipynb
├── mnist_onnx.ipynb
├── onnx_runtime.ipynb
├── main.py
├── number5.png
└── README.md
```

### 1. `mnist_keras.ipynb`

- Loads the MNIST dataset.
- Builds a custom Convolutional Neural Network (CNN).
- Trains the model.
- Saves the trained Keras model.

---

### 2. `mnist_onnx.ipynb`

- Loads the trained Keras model.
- Converts the model into the ONNX format.
- Saves the generated ONNX model.

---

### 3. `onnx_runtime.ipynb`

- Loads both the original Keras model and the ONNX model.
- Performs inference using ONNX Runtime.
- Verifies that both models produce identical (or nearly identical) predictions.
- Benchmarks inference speed by predicting **1000 MNIST images** using both implementations.

---

### 4. `main.py`

A simple deployment example that:

- Loads the ONNX model using ONNX Runtime.
- Reads an input image from the project directory.
- Performs digit classification.
- Displays the predicted digit.

---

### 5. `number5.png`

A sample handwritten digit image used to demonstrate inference with the deployed ONNX model.

---

## Workflow

```
Train CNN (Keras)
        │
        ▼
Save Keras Model
        │
        ▼
Convert to ONNX
        │
        ▼
Load with ONNX Runtime
        │
        ▼
Run Fast Inference
        │
        ▼
Compare Accuracy & Performance
```

---

## Technologies Used

- Python
- TensorFlow
- Keras
- ONNX
- ONNX Runtime
- tf2onnx
- NumPy
- OpenCV
- Matplotlib
- Jupyter Notebook

---

## Results

This project demonstrates that:

- ONNX models preserve prediction accuracy after conversion.
- ONNX Runtime provides efficient model execution.
- Deployment becomes lighter since the full TensorFlow framework is no longer required.
- ONNX offers a standardized format for sharing models across different machine learning frameworks.

---

## Learning Outcomes

After completing this project, you will understand how to:

- Train a CNN with TensorFlow/Keras.
- Save and export trained models.
- Convert Keras models to ONNX.
- Deploy models using ONNX Runtime.
- Benchmark inference performance.
- Compare prediction consistency between different inference engines.

---

## References

- ONNX
- ONNX Runtime
- TensorFlow
- Keras
- tf2onnx
