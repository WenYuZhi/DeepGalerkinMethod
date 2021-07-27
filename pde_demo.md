## 1d PDE benchmark 
$$
\frac{\partial T}{\partial t}-\frac{\partial ^2T}{\partial x^2}=
\cos \pi x\cos t+\pi ^2\cos \pi x\sin t,\ \left( x,t \right) \in \left[ 0,1 \right] \times \left[ 0,10 \right] 
$$

$$
T\left( x,0 \right) = 0 ,\ x\in \left[ 0,1 \right] 
$$

$$
T\left( 0,t \right) =\sin t,\ t\in \left[ 0,10 \right] 
$$

$$
T\left( 1,t \right) =-\sin t,\ t\in \left[ 0,10 \right] 
$$

解析解为
$$
T\left( x,t \right) =-\pi ^2\cos \pi x\sin t
$$

## 2d PDE benchmark 
$$
\frac{\partial T}{\partial t}-\frac{\partial ^2T}{\partial x^2}-\frac{\partial ^2T}{\partial y^2}=\left( \pi +2\pi ^2 \right) \left( \cos \left( \pi t \right) +\sin \left( \pi t \right) \right) \sin \left( \pi x \right) \sin \left( \pi y \right) ,\,\,\,\,\left( x,y,t \right) \in \left[ 0,1 \right] \times \left[ 0,1 \right] \times \left[ 0,4 \right] 
$$

$$
T\left( x,y,0 \right) =0,\ \left( x,y \right) \in \left[ 0,1 \right] \times \left[ 0,1 \right] 
$$


$$
T\left( 0,y,t \right) =T\left( 1,y,t \right) =0,\ \left( y,t \right) \in \left[ 0,1 \right] \times \left[ 0,4 \right] 
$$

$$
T\left( x,0,t \right) =T\left( x,1,t \right) =0,\ \left( x,t \right) \in \left[ 0,1 \right] \times \left[ 0,4 \right] 
$$

解析解为
$$
T\left( x,y,t \right) =\sin \left( \pi t \right) \sin \left( \pi x \right) \sin \left( \pi y \right) 
$$

