import numpy as np
import matplotlib.pyplot as plt

def plot_cuboid(center, size, package):

    # suppose axis direction: x: to left; y: to inside; z: to upper
    # get the (left, outside, bottom) point

    ox, oy, oz = center
    l, w, h = size

    x = np.linspace(ox-l/2, ox+l/2, num=2)
    y = np.linspace(oy-w/2, oy+w/2, num=2)
    z = np.linspace(oz-h/2, oz+h/2, num=2)
    x1, z1 = np.meshgrid(x, z)
    y11 = np.ones_like(x1)*(oy-w/2)
    y12 = np.ones_like(x1)*(oy+w/2)
    x2, y2 = np.meshgrid(x, y)
    z21 = np.ones_like(x2)*(oz-h/2)
    z22 = np.ones_like(x2)*(oz+h/2)
    y3, z3 = np.meshgrid(y, z)
    x31 = np.ones_like(y3)*(ox-l/2)
    x32 = np.ones_like(y3)*(ox+l/2)

    # outside surface
    ax.plot_wireframe(x1, y11, z1, color='b', rstride=1, cstride=1, alpha=0.6)
    # inside surface
    ax.plot_wireframe(x1, y12, z1, color='b', rstride=1, cstride=1, alpha=0.6)
    # bottom surface
    ax.plot_wireframe(x2, y2, z21, color='b', rstride=1, cstride=1, alpha=0.6)
    # upper surface
    ax.plot_wireframe(x2, y2, z22, color='b', rstride=1, cstride=1, alpha=0.6)
    # left surface
    ax.plot_wireframe(x31, y3, z3, color='b', rstride=1, cstride=1, alpha=0.6)
    # right surface
    ax.plot_wireframe(x32, y3, z3, color='b', rstride=1, cstride=1, alpha=0.6)
    ax.text(ox, oy, oz, s=str(package), clip_on=True, size=6, fontweight='bold')
    ax.set_xlabel('length')
    ax.set_xlim(-1, 30)
    ax.set_ylabel('width')
    ax.set_ylim(-1, 30)
    ax.set_zlabel('height')
    ax.set_zlim(-1, 20)
    #plt.show()

def plot_cuboid1(center, size):

    # suppose axis direction: x: to left; y: to inside; z: to upper
    # get the (left, outside, bottom) point

    ox, oy, oz = center
    l, w, h = size

    x = np.linspace(ox-l/2, ox+l/2, num=2)
    y = np.linspace(oy-w/2, oy+w/2, num=2)
    z = np.linspace(oz-h/2, oz+h/2, num=2)
    x1, z1 = np.meshgrid(x, z)
    y11 = np.ones_like(x1)*(oy-w/2)
    y12 = np.ones_like(x1)*(oy+w/2)
    x2, y2 = np.meshgrid(x, y)
    z21 = np.ones_like(x2)*(oz-h/2)
    z22 = np.ones_like(x2)*(oz+h/2)
    y3, z3 = np.meshgrid(y, z)
    x31 = np.ones_like(y3)*(ox-l/2)
    x32 = np.ones_like(y3)*(ox+l/2)

    # outside surface
    ax.plot_wireframe(x1, y11, z1, color='b', rstride=1, cstride=1, alpha=0.6)
    # inside surface
    ax.plot_wireframe(x1, y12, z1, color='b', rstride=1, cstride=1, alpha=0.6)
    # bottom surface
    ax.plot_wireframe(x2, y2, z21, color='b', rstride=1, cstride=1, alpha=0.6)
    # upper surface
    ax.plot_wireframe(x2, y2, z22, color='b', rstride=1, cstride=1, alpha=0.6)
    # left surface
    ax.plot_wireframe(x31, y3, z3, color='b', rstride=1, cstride=1, alpha=0.6)
    # right surface
    ax.plot_wireframe(x32, y3, z3, color='b', rstride=1, cstride=1, alpha=0.6)
    ax.set_xlabel('length')
    ax.set_xlim(-1, 30)
    ax.set_ylabel('width')
    ax.set_ylim(-1, 30)
    ax.set_zlabel('height')
    ax.set_zlim(-1, 20)
    #plt.show()

def plot_cuboid_floor(center, size, package):

    # suppose axis direction: x: to left; y: to inside; z: to upper
    # get the (left, outside, bottom) point

    ox, oy, oz = center
    l, w, h = size

    x = np.linspace(ox-l/2, ox+l/2, num=2)
    y = np.linspace(oy-w/2, oy+w/2, num=2)
    z = np.linspace(oz-h/2, oz+h/2, num=2)
    x1, z1 = np.meshgrid(x, z)
    y11 = np.ones_like(x1)*(oy-w/2)
    y12 = np.ones_like(x1)*(oy+w/2)
    x2, y2 = np.meshgrid(x, y)
    z21 = np.ones_like(x2)*(oz-h/2)
    z22 = np.ones_like(x2)*(oz+h/2)
    y3, z3 = np.meshgrid(y, z)
    x31 = np.ones_like(y3)*(ox-l/2)
    x32 = np.ones_like(y3)*(ox+l/2)

    # outside surface
    ax.plot_wireframe(x1, y11, z1, color='r', rstride=1, cstride=1, alpha=0.6)
    # inside surface
    ax.plot_wireframe(x1, y12, z1, color='r', rstride=1, cstride=1, alpha=0.6)
    # bottom surface
    ax.plot_wireframe(x2, y2, z21, color='r', rstride=1, cstride=1, alpha=0.6)
    # upper surface
    ax.plot_wireframe(x2, y2, z22, color='r', rstride=1, cstride=1, alpha=0.6)
    # left surface
    ax.plot_wireframe(x31, y3, z3, color='r', rstride=1, cstride=1, alpha=0.6)
    # right surface
    ax.plot_wireframe(x32, y3, z3, color='r', rstride=1, cstride=1, alpha=0.6)
    ax.text(ox, oy, oz, s=str(package), clip_on=True, size=6, fontweight='bold')
    ax.set_xlabel('length')
    ax.set_xlim(-1, 30)
    ax.set_ylabel('width')
    ax.set_ylim(-1, 30)
    ax.set_zlabel('height')
    ax.set_zlim(-1, 20)
    #plt.show()

fig = plt.figure()
ax = fig.add_subplot(projection='3d')










