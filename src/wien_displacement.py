"""维恩位移定律计算模块

本模块实现了维恩位移定律相关的计算功能，包括：
1. 维恩方程的图像绘制
2. 维恩位移常数的计算
3. 基于维恩位移定律的温度估算

主要函数：
- plot_wien_equation: 绘制维恩方程的图像
- solve_wien_constant: 计算维恩位移常数
- calculate_temperature: 根据波长估算温度
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
from scipy import constants

def wien_equation(x):
    """定义维恩位移方程 5e^{-x} + x - 5 = 0
    
    参数:
        x (float): 方程变量
        
    返回:
        float: 方程计算结果
    """
    return 5 * np.exp(-x) + x - 5

def plot_wien_equation(x_range=(-1, 6), solution=None):
    """可视化维恩方程求解过程
    
    参数:
        x_range (tuple): 绘图范围，默认(-1, 6)
        solution (float): 方程解的标记位置，可选
    """
    x = np.linspace(x_range[0], x_range[1], 400)
    y1 = 5 * np.exp(-x)
    y2 = 5 - x
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y1, 'r-', lw=2, label='$y = 5e^{-x}$')
    plt.plot(x, y2, 'b--', lw=2, label='$y = 5 - x$')
    
    if solution is not None:
        plt.scatter(solution, 5 * np.exp(-solution), 
                   c='green', s=100, zorder=5,
                   label=f'Solution $x={solution:.3f}$')
    
    plt.title("Graphical Solution of Wien's Displacement Law Equation", fontsize=14)
    plt.xlabel("x", fontsize=12)
    plt.ylabel("y", fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()

def solve_wien_constant(x0=5.0):
    """求解维恩位移方程并计算位移常数
    
    参数:
        x0 (float): 初始猜测值，默认5.0
        
    返回:
        tuple: (方程解x, 维恩位移常数b) 单位: (无量纲, m·K)
    """
    # 数值求解非线性方程
    x_solution = fsolve(wien_equation, x0)[0]
    
    # 使用国际标准物理常数
    h = constants.h       # 普朗克常数 (J·s)
    c = constants.c       # 光速 (m/s)
    k_B = constants.k     # 玻尔兹曼常数 (J/K)
    
    # 计算维恩位移常数
    b = (h * c) / (k_B * x_solution)
    return x_solution, b

# 预计算维恩常数(使用标准初始值)
WIEN_CONSTANT = solve_wien_constant()[1]

def calculate_temperature(wavelength):
    """根据峰值波长计算黑体温度
    
    参数:
        wavelength (float): 峰值波长，单位：米
        
    返回:
        float: 黑体温度，单位：K
        
    示例:
        >>> calculate_temperature(502e-9)  # 计算太阳表面温度
        5778.0
    """
    return WIEN_CONSTANT / wavelength

if __name__ == "__main__":
    # 绘制方程图像
    plot_wien_equation()
    
    # 从键盘输入初值
    try:
        x0 = float(input("请根据图像输入方程求解的初始值（建议值为4-6）："))
    except ValueError:
        print("输入无效，将使用默认值 5")
        x0 = 5
    
    # 计算维恩位移常数
    x, b = solve_wien_constant(x0)
    print(f"\n使用初值 x0 = {x0}")
    print(f"方程的解 x = {x:.6f}")
    print(f"维恩位移常数 b = {b:.6e} m·K")
    
    # 计算太阳表面温度
    wavelength_sun = 502e-9  # 502 nm 转换为米
    temperature_sun = calculate_temperature(wavelength_sun, x0)
    print(f"\n太阳表面温度估计值：{temperature_sun:.0f} K")
