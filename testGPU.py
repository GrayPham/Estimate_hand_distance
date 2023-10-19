import torch
import tensorflow as tf

# Kiểm tra PyTorch
if torch.cuda.is_available():
    print("PyTorch sử dụng GPU.")
else:
    print("PyTorch không sử dụng GPU.")

# Kiểm tra TensorFlow
if tf.test.is_gpu_available():
    print("TensorFlow sử dụng GPU.")
else:
    print("TensorFlow không sử dụng GPU.")
