# 文件名：src/spring_block.py
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def solve_ode_euler(step_num):
    """
    使用显式欧拉法求解弹簧-质点系统的常微分方程。
    
    参数:
        step_num (int): 模拟的总步数，步数越多精度越高但计算量越大
    
    返回:
        tuple: 包含三个元素的元组：
            - time_points (np.ndarray): 时间点数组，形状为(step_num+1,)
            - position (np.ndarray): 位置数组，形状同时间数组
            - velocity (np.ndarray): 速度数组，形状同时间数组
    
    说明:
        - 总模拟时间固定为2π，对应简谐振动的自然周期
        - 系统方程为 d²x/dt² = -x (已归一化k/m=1)
        - 欧拉法为显式一阶方法，长期模拟可能出现能量漂移
    """
    position = np.zeros(step_num + 1)
    velocity = np.zeros(step_num + 1)
    time_step = 2 * np.pi / step_num  # 固定总时间为2π
    
    # 初始条件：x(0)=0, v(0)=1
    position[0] = 0
    velocity[0] = 1
    
    # 欧拉法显式迭代
    for i in range(step_num):
        position[i+1] = position[i] + velocity[i] * time_step
        velocity[i+1] = velocity[i] - position[i] * time_step  # 加速度a=-x
    
    time_points = np.arange(step_num + 1) * time_step
    return time_points, position, velocity

def spring_mass_ode_func(state, t):
    """
    定义弹簧-质点系统的常微分方程组
    
    参数:
        state (list): 当前状态量 [位置x, 速度v]
        t (float): 当前时间（方程不显含时间，此处为兼容odeint接口）
    
    返回:
        list: 导数向量 [dx/dt, dv/dt]
    
    说明:
        - 系统方程转换为两个一阶ODE：
            dx/dt = v
            dv/dt = -x
        - 该函数将被odeint调用用于计算导数
    """
    x, v = state
    return [v, -x]

def solve_ode_odeint(step_num):
    """
    使用scipy的odeint求解器进行高精度求解
    
    参数:
        step_num (int): 时间点数量（实际步数由求解器自动控制）
    
    返回:
        tuple: 包含三个元素的元组，格式同solve_ode_euler
    
    说明:
        - 使用LSODA算法，自动在Adams（非刚性）和BDF（刚性）方法间切换
        - 结果精度显著高于显式欧拉法，适合作为基准解
    """
    time_points = np.linspace(0, 2 * np.pi, step_num + 1)  # 等间距时间点
    y0 = [0, 1]  # 初始条件
    # 调用odeint求解，结果形状为(step_num+1, 2)
    sol = odeint(spring_mass_ode_func, y0, time_points)
    return time_points, sol[:, 0], sol[:, 1]

def plot_comparison(euler_data, odeint_data, save_path=None):
    """
    绘制欧拉法与odeint结果的对比图表
    
    参数:
        euler_data (tuple): 欧拉法的(time, position, velocity)数据
        odeint_data (tuple): odeint的对应数据
        save_path (str/None): 图片保存路径，None时显示窗口
    
    生成图表:
        1. 位置-时间曲线对比
        2. 速度-时间曲线对比
        3. 相空间轨迹（x-v图）
        4. 能量时间演化对比
    """
    t_euler, x_euler, v_euler = euler_data
    t_ode, x_ode, v_ode = odeint_data
    
    plt.figure(figsize=(12, 10))
    
    # 位置-时间图
    plt.subplot(2, 2, 1)
    plt.plot(t_euler, x_euler, 'r--', label='Euler Method', alpha=0.7)
    plt.plot(t_ode, x_ode, 'b-', label='ODEINT', linewidth=1)
    plt.xlabel('Time (s)')
    plt.ylabel('Position (m)')
    plt.title('Position vs Time')
    plt.legend()
    
    # 速度-时间图
    plt.subplot(2, 2, 2)
    plt.plot(t_euler, v_euler, 'r--', alpha=0.7)
    plt.plot(t_ode, v_ode, 'b-', linewidth=1)
    plt.xlabel('Time (s)')
    plt.ylabel('Velocity (m/s)')
    plt.title('Velocity vs Time')
    
    # 相空间图
    plt.subplot(2, 2, 3)
    plt.plot(x_euler, v_euler, 'r--', alpha=0.7, label='Euler')
    plt.plot(x_ode, v_ode, 'b-', linewidth=1, label='ODEINT')
    plt.xlabel('Position (m)')
    plt.ylabel('Velocity (m/s)')
    plt.title('Phase Space Trajectory')
    plt.legend()
    
    # 能量图（总机械能应为常数0.5）
    plt.subplot(2, 2, 4)
    energy_euler = 0.5 * (v_euler**2 + x_euler**2)
    energy_ode = 0.5 * (v_ode**2 + x_ode**2)
    plt.plot(t_euler, energy_euler, 'r--', alpha=0.7, label='Euler')
    plt.plot(t_ode, energy_ode, 'b-', linewidth=1, label='ODEINT')
    plt.xlabel('Time (s)')
    plt.ylabel('Total Energy (J)')
    plt.title('Energy Conservation')
    plt.ylim(0.4, 0.6)  # 放大观察能量变化
    
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=150)
        print(f"图表已保存至 {save_path}")
    else:
        plt.show()

# 示例用法
if __name__ == "__main__":
    # 使用100步的欧拉法（低精度）和1000步的odeint（高精度）
    euler_data = solve_ode_euler(100)
    odeint_data = solve_ode_odeint(1000)
    
    # 生成对比图表并保存
    plot_comparison(euler_data, odeint_data, save_path="spring_mass_comparison.png")
