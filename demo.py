from libs import *
from train import *
from net import *
from heat import *

def solution_f(t, x):
    return -(np.pi)**2 * np.cos(np.pi*x) * np.sin(t)

class Demo():
    def __init__(self, net, heatequation, nt, nx):
        self.net = net
        self.heatequation = heatequation
        self.nt, self.nx = nt, nx
        self.t_range, self.x_range = np.linspace(0, heatequation.te, nt), np.linspace(0, heatequation.xe, nx)
    
    def get_solution(self):
        data = np.empty((self.net.dim, 1))
        self.est_solution, self.solution = [], []
        for t in self.t_range:
            data[0] = t
            for x in self.x_range:
                data[1] = x
                in_data = torch.Tensor(data.reshape(1,-1))
                self.est_solution.append(self.net(in_data).detach().cpu().numpy())
                self.solution.append(solution_f(t, x))

        self.est_solution = np.reshape(self.est_solution, (self.nt, self.nx))
        self.solution = np.reshape(self.solution, (self.nt, self.nx))
    
    def evalution(self):
        pass

    def plot_mesh(self):
        t, x = np.meshgrid(self.t_range, self.x_range, indexing='ij')
        fig1 = plt.figure()
        ax1 = fig1.gca(projection = '3d')
        ax1.set_zlim([-5,5])
        ax1.plot_surface(t, x, self.est_solution, cmap=cm.RdYlBu_r, edgecolor='blue', linewidth=0.0003, antialiased=True)
        fig1.show()

        fig2 = plt.figure()
        ax2 = fig2.gca(projection = '3d')
        ax2.set_zlim([-5,5])
        ax2.plot_surface(t, x, self.est_solution - self.solution, cmap=cm.RdYlBu_r, edgecolor='blue', linewidth=0.0003, antialiased=True)
        fig2.show()




