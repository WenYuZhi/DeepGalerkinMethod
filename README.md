# Deep Galerkin Method  for Solving Partial Differential Equations
采用深度伽辽金方法求解偏微分方程。深度神经网络部分采用Pytorch实现。在pde_demo里构造了2个有解析解的偏微分方程以便于验证本算法的有效性。本算法的理论主要依据以下文章：https://zhuanlan.zhihu.com/p/359328643
主干代码也来自于这篇文章，并对这篇文章的代码进行了修改。
1 添加了1维，2维 热传导方程的求解
2 对heat.py进行了重写，按照偏微分方程的习惯 定义方程，边界条件和初始条件来构成。
3 添加了一组解析解便于验证偏微分方程的求解
4 测试了多种激活函数对训练效果的影响
