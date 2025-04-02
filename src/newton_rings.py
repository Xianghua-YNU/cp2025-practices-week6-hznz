import numpy as np
import matplotlib.pyplot as plt
import os

def setup_parameters():
    """
    设置模拟牛顿环所需的参数。

    返回:
    tuple: 包含激光波长（单位：米）、透镜曲率半径（单位：米）的元组
    """
    # 氦氖激光波长，转换为米
    lambda_light = 632.8e-9
    # 透镜曲率半径，单位米
    R_lens = 0.1
    return lambda_light, R_lens

def generate_grid():
    """
    生成模拟所需的网格坐标。

    返回:
    tuple: 包含网格坐标 X、Y 以及径向距离 r 的元组
    """
    # 空间范围 ±1 mm，转换为米
    x = np.linspace(-0.001, 0.001, 1000)
    y = np.linspace(-0.001, 0.001, 1000)
    X, Y = np.meshgrid(x, y)
    # 计算各点的径向距离
    r = np.sqrt(X**2 + Y**2)
    return X, Y, r

def calculate_intensity(r, lambda_light, R_lens):
    """
    计算牛顿环的干涉强度分布。

    参数:
    r (np.ndarray): 各点的径向距离数组，单位米
    lambda_light (float): 光波长，单位米
    R_lens (float): 透镜曲率半径，单位米

    返回:
    np.ndarray: 各点的干涉强度，无量纲
    """
    # 计算空气膜厚度d
    d = R_lens - np.sqrt(R_lens**2 - r**2)
    # 根据公式计算干涉强度
    intensity = 4 * (np.sin(2 * np.pi * d / lambda_light))**2
    return intensity

def plot_newton_rings(intensity):
    """
    绘制并保存牛顿环干涉图样。

    参数:
    intensity (np.ndarray): 干涉强度分布数组
    """
    plt.figure(figsize=(10, 10))
    # 绘制强度图，设置颜色映射为灰度，范围0到4
    plt.imshow(intensity, cmap='gray', 
               extent=(-0.001, 0.001, -0.001, 0.001), 
               vmin=0, vmax=4)
    plt.colorbar(label='Intensity')
    plt.title("Newton's Rings Interference Pattern")
    plt.xlabel("x (m)")
    plt.ylabel("y (m)")
    # 确保results目录存在
    os.makedirs('results', exist_ok=True)
    # 保存图像到results目录
    plt.savefig('results/newton_rings.png')
    plt.close()  # 关闭图形，避免在交互模式下显示

if __name__ == "__main__":
    # 设置参数
    lambda_light, R_lens = setup_parameters()
    # 生成网格
    X, Y, r = generate_grid()
    # 计算强度
    intensity = calculate_intensity(r, lambda_light, R_lens)
    # 绘制并保存图像
    plot_newton_rings(intensity)
    print("牛顿环图样已保存至results/newton_rings.png")
