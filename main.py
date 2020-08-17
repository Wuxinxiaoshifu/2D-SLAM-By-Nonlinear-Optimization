# coding:utf-8
import numpy as np
from numpy import linspace
import matplotlib.pyplot as plt

# 自己的类
from movemodel import MoveModel
from draw import Draw
from landmark import Landmark
from measure import Measure
from solver import Solver

# 运动模型类
init_pose = np.array([[12.0], [3.0], [0.0]])
move_model = MoveModel(init_pose)
# 路标点类
landmarks = Landmark()
# 绘图类
draw = Draw()
# 测量类
measure = Measure(move_model)
# 优化类
solver = Solver()

# 循环计数
n = 0
sum = 1000

# 传感器参数
r = 3.0

while n != sum:
    measure.GetMeasure(landmarks._landmarks, r)

    if n == 0:
        solver.Init()
    else:
        solver.Update_slidewindow_graph()
    draw.Show_Result(move_model._currentpose, r, landmarks._landmarks)
    move_model.updatepose()
    n = n + 1