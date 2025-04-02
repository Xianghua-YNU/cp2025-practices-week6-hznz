import numpy as np 
import matplotlib.pyplot as plt
from matplotlib import animation

def sineWaveZeroPhi(x, t, A, omega, k):
    """
    计算简谐波的瞬时位移（无初始相位）
    
    参数:
        x (np.ndarray): 空间坐标数组（单位：米）
        t (float): 时间（单位：秒）
        A (float): 波的振幅（单位：米）
        omega (float): 波的角频率（单位：弧度/秒）
        k (float): 波数（单位：弧度/米，k = 2π/λ）
    
    返回:
        np.ndarray: 波在各空间点的位移值（单位：米）
    """
    return A * np.sin(k * x - omega * t)

# ------------------ 全局变量定义 ------------------
# 创建画布和坐标轴
fig = plt.figure()
ax = plt.axes(xlim=(0, 10), ylim=(-2, 2))  # 设置坐标范围
ax.set_xlabel("x (m)")                     # x轴标签
ax.set_ylabel("y (m)")                     # y轴标签

# 初始化三条曲线对象（正向波、反向波、驻波）
line1, = ax.plot([], [], lw=2, linestyle='--', color='r')  # 红色虚线：正向波
line2, = ax.plot([], [], lw=2, linestyle='--', color='b')  # 蓝色虚线：反向波
line3, = ax.plot([], [], lw=2, color='k')                 # 黑色实线：驻波
lines = [line1, line2, line3]  # 曲线对象列表（测试代码需要访问此变量）

# 空间坐标定义（全局作用域，测试代码需要访问）
x = np.linspace(0, 10, 1000)  # 生成0到10米之间的1000个点

# ------------------ 动画函数定义 ------------------
def init():
    """
    初始化动画帧，清空所有曲线的数据
    
    返回:
        list: 包含三个空曲线对象的列表
    """
    for line in lines:
        line.set_data([], [])
    return lines

def animate(i, A=1.0, omega=2*np.pi, k=np.pi/2):
    """
    更新动画帧，计算并绘制当前时刻的波形
    
    参数:
        i (int): 帧序号（自动递增）
        A (float): 波的振幅（默认1.0）
        omega (float): 角频率（默认2π）
        k (float): 波数（默认π/2）
    
    返回:
        list: 更新后的曲线对象列表
    """
    t = 0.05 * i  # 时间计算（每帧时间步长0.05秒）
    
    # 计算正向波和反向波的位移
    y_forward = sineWaveZeroPhi(x, t, A, omega, k)
    y_backward = sineWaveZeroPhi(x, t, A, -omega, k)  # 反向波通过负号实现
    
    # 计算驻波（两波叠加）
    y_standing = y_forward + y_backward
    
    # 更新曲线数据
    lines[0].set_data(x, y_forward)   # 更新正向波曲线
    lines[1].set_data(x, y_backward)  # 更新反向波曲线
    lines[2].set_data(x, y_standing)  # 更新驻波曲线
    
    return lines

# ------------------ 主程序入口------------------
if __name__ == "__main__":
    # 创建动画对象
    anim = animation.FuncAnimation(
        fig,           # 画布对象
        animate,       # 帧更新函数
        init_func=init, # 初始化函数
        frames=200,     # 总帧数（200帧）
        interval=50,   # 帧间隔时间（50毫秒，即20 FPS）
        blit=True      # 使用blit优化绘制
    )
    
    # 显示动画窗口
    plt.show()
