import os
# os.chdir(os.path.dirname(os.path.abspath(__file__)))

from libs import *
from train import *
from net import *
from heat import *
from demo import *

net = Net(n_layer = 3, n_hidden = 25, dim = 2)
print(net)

te = 4
xe = 1

heatequation = Heat1D(net, te, xe)

train = Train(net, heatequation, BATCH_SIZE = 2**10)

train.train(epoch = 10**4, lr = 0.002)

train.plot_kpi()


demo = Demo(net, heatequation, nt = 100, nx = 100)
demo.get_solution()
demo.plot_mesh()


