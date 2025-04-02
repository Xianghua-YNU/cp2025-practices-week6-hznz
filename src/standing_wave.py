import numpy as np 
import matplotlib.pyplot as plt
from matplotlib import animation

def sineWaveZeroPhi(x, t, A, omega, k):
    """
    计算简谐波的瞬时位移
    参数:
        x (np.ndarray): 空间坐标数组
        t (float): 时间
        A (float): 振幅
        omega (float): 角频率
        k (float): 波数
    返回:
        np.ndarray: 波的位移值数组
    """
    return A * np.sin(k * x - omega * t)

# 初始化画布
fig = plt.figure(figsize=(10, 6))
ax = plt.axes(xlim=(0, 10), ylim=(-2.5, 2.5))
ax.set_xlabel("Position (m)", fontsize=12)
ax.set_ylabel("Displacement (m)", fontsize=12)
ax.set_title("Standing Wave Formation", fontsize=14)

# 初始化三条曲线：正向波、反向波、驻波
line1, = ax.plot([], [], 'r--', lw=1.5, label="Forward Wave")
line2, = ax.plot([], [], 'b--', lw=1.5, label="Backward Wave")
line3, = ax.plot([], [], 'k-', lw=2, label="Standing Wave")
plt.legend()

def init():
    """初始化动画，清空曲线数据"""
    line1.set_data([], [])
    line2.set_data([], [])
    line3.set_data([], [])
    return line1, line2, line3

def animate(i):
    """更新动画帧"""
    # 波参数设置
    A = 1.0
    omega = 2 * np.pi
    k = np.pi / 2
    t = 0.05 * i  # 时间步长
    
    # 空间坐标（0到10米，1000个点）
    x = np.linspace(0, 10, 1000)
    
    # 计算正向波和反向波
    y_forward = sineWaveZeroPhi(x, t, A, omega, k)
    y_backward = sineWaveZeroPhi(x, t, A, -omega, k)
    y_standing = y_forward + y_backward  # 驻波
    
    # 更新曲线数据
    line1.set_data(x, y_forward)
    line2.set_data(x, y_backward)
    line3.set_data(x, y_standing)
    
    return line1, line2, line3

if __name__ == "__main__":
    # 创建动画对象
    anim = animation.FuncAnimation(
        fig, animate, init_func=init,
        frames=200, interval=50, blit=True
    )
    
    # 保存动画为GIF（可选）
    anim.save("results/standing_wave.gif", writer="pillow")
    plt.show()
