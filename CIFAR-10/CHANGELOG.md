# CIFAR-10 Unsupervised clustering

## Dataset
https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz

## 21/03/2025
Made start
![First implementation](image.png)

## 22/03/2025
- Experimented with different encoder and decoder structures
- Added a classifier head on top of the encoder for multitask learning

## 23/03/2025 
- Changed latent size 512 to 1024 for better details retention 
- Replaced UpSampling2D with Conv2DTranspose as it was too blocky
- Added BatchNormalization() for better convergence
- Switched to tanh rather than sigmoid and has improved performance

Current results:
![Latest output](image-1.png)

Decoded images are coming out more blurry but less blocky

Before:
![Previous version](image-2.png)

After:
![Current version](image-3.png)

## 24/03/2025
With ChatGPT:
- Replaced TensorFlow implementation with PyTorch to resolve GPU compatibility issues and improve training stability
- Converted two deep learning models from `tf.keras` to `torch.nn.Module`, retaining original architectures and training logic

![alt text](image-4.png)

began markdown
