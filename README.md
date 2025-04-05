[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/VbjIuRO4)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=18970371)
# 计算物理实验 - 第六周作业

本仓库包含计算物理实践课程第六周的编程作业，涵盖物理光学与经典力学的数值模拟与数据分析。

## 目录结构
```shell
cp2025-practice-week6/
├── src/                                 # 源代码目录（学生实现）
│   ├── wien_displacement.py             # 维恩位移定律计算
│   ├── maxwell_distribution.py          # 麦克斯韦速率分布计算
│   ├── beats_simulation.py              # 拍频现象数值模拟
│   ├── standing_wave.py                 # 驻波动画模拟
│   ├── spring_block.py                  # 弹簧物块运动模拟
│   └── newton_rings.py                  # 牛顿环干涉模拟
├── results/                             # 结果目录（学生填写）
│   ├── 维恩位移定律实验报告.md            # 维恩位移定律实验报告
│   ├── 麦克斯韦速率分布实验报告.md         # 麦克斯韦速率分布实验报告
│   ├── 拍频现象数值模拟实验报告.md         # 拍频现象实验报告
│   ├── 驻波动画模拟实验报告.md            # 驻波实验报告
│   ├── 弹簧物块运动模拟实验报告.md         # 弹簧物块实验报告
│   └── 牛顿环的干涉图样实验报告.md         # 牛顿环实验报告模板
├── solutions/                           # 参考解答目录
│   ├── wien_displacement_solution.py    # 维恩位移定律参考解答
│   ├── maxwell_distribution_solution.py # 麦克斯韦速率分布参考解答
│   ├── beats_simulation_solution.py     # 拍频现象参考解答
│   ├── standing_wave_solution.py        # 驻波参考解答
│   ├── spring_block_solution.py         # 弹簧物块参考解答
│   └── newton_rings_solution.py         # 牛顿环干涉参考解答
├── tests/                               # 测试文件目录
│   ├── test_wien_displacement.py        # 维恩位移定律测试
│   ├── test_maxwell_distribution.py     # 麦克斯韦速率分布测试
│   ├── test_beats_simulation.py         # 拍频现象测试
│   ├── test_standing_wave.py            # 驻波测试
│   ├── test_spring_block.py             # 弹簧物块测试
│   └── test_newton_rings.py             # 牛顿环干涉测试
├── docs/                                # 文档目录
│   ├── 维恩位移定律.md                   # 维恩位移定律实验说明
│   ├── 麦克斯韦速率分布律.md              # 麦克斯韦速率分布实验说明
│   ├── 拍频现象数值模拟与分析.md          # 拍频现象实验说明
│   ├── 驻波动画模拟项目.md               # 驻波实验说明
│   ├── 弹簧物块运动方程求解.md           # 弹簧物块实验说明
│   └── 牛顿环的干涉图样.md               # 牛顿环实验说明
├── requirements.txt                     # 项目依赖
└── README.md                            # 本文件
```


## 作业内容

本次作业包含六个独立的物理模拟实验：

1. **维恩位移定律计算**：研究黑体辐射的波长与温度关系
2. **麦克斯韦速率分布计算**：模拟气体分子速率分布
3. **拍频现象数值模拟**：研究两个相近频率叠加产生的拍频现象
4. **驻波动画模拟**：可视化弦上驻波的形成过程
5. **弹簧物块运动模拟**：研究简谐振动系统的动力学特性
6. **牛顿环的干涉图样**：研究薄膜干涉现象和光强分布规律

## 使用说明

### 环境配置
```bash
# 安装依赖
pip install -r requirements.txt

# 运行所有测试
python -m pytest tests/

# 运行自动评分
python .github/classroom/autograding.py
```
### 提交作业
1. 完成 src/ 目录下的所有实现文件
2. 确保所有测试通过
3. 提交到GitHub仓库
4. 在 results/ 目录下对应的markdown文件中上传程序运行结果，包括生成的图像文件和结果讨论
## 评分标准
每个实验模块占总分的六分之一，总分为60分。评分将通过自动测试完成，测试通过即得满分。

## 参考资料
- 《Python物理建模初学者指南》第六章
