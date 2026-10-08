# diffusion_demo

围绕**扩散模型（Diffusion Models）**的学习仓库：论文精读笔记 ＋ LaTeX 学习报告 + diffusion model 复现。

当前重点：**Tree-Ring Watermarks**——在扩散模型的初始噪声空间嵌入不可见水印，使水印随生成过程传播到最终图像中。

## 仓库内容

| 路径      | 说明                                                         |
| --------- | ------------------------------------------------------------ |
| `notes/`  | 论文精读笔记（Markdown），当前有 `00.md`——Tree-Ring 论文笔记 |
| `report/` | 学习报告。`main.tex` 是 LaTeX 源文件，`main.pdf` 是编译产物  |
| `demo.py` | 环境自检脚本：检查 PyTorch / CUDA 是否可用，并打印 GPU 型号与显存 |

## 环境要求

- **Python 3.11**
- **依赖管理**：`uv`
- **GPU**：PyTorch / TorchVision 走 CUDA 12.8 构建（来自 `pytorch-cu128` 索引）

## 快速开始

安装依赖：

```bash
uv sync
```

运行环境自检，确认 GPU 可用：

```bash
uv run demo.py
```

预期输出包含 PyTorch 版本、CUDA 运行时版本、`CUDA available: True`，以及 GPU 型号与显存大小。

## 编译报告

`report/main.pdf` 由 `report/main.tex` 编译生成，需要本地 LaTeX 环境（含 `ctex` 中文支持）。

```bash
cd report

xelatex main.tex
```

## 说明

本仓库目前只有笔记与报告，**尚无实验代码**。可运行的实验部分计划在后续补充（从零实现 PCA → 经典 ML → 神经网络）。