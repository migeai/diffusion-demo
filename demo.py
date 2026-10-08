"""
用来检测显卡加速是否可用
"""

import torch
import torchvision

print("PyTorch version:", torch.__version__)
print("Torchvision version:", torchvision.__version__)
print("PyTorch CUDA runtime:", torch.version.cuda)
print("CUDA available:", torch.cuda.is_available())

if torch.cuda.is_available():
    print("GPU:", torch.cuda.get_device_name(0))
    print(
        "GPU memory:",
        round(torch.cuda.get_device_properties(0).total_memory / 1024**3, 2),
        "GB",
    )

    x = torch.randn(1024, 1024, device="cuda")
    y = x @ x
    print("Tensor device:", y.device)
    print("Calculation succeeded:", y.shape)

