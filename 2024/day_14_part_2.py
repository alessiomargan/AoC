import sys
sys.path.insert(1, '..')
from aoc_utils import *

from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import functools

in_part_A = Input(14)
maxX,maxY = 101,103

regex = r"""p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)"""

class Robot(namedtuple('Robot','px py vx vy')):
    def __repr__(self) -> str:
        return f'<Robot{tuple.__repr__(self)}>'
    def move(self,sec:int,maxx:int,maxy:int):
        # Return a new instance of the named tuple replacing specified fields with new values
        return self._replace(px=(self.px+(self.vx*sec))%maxx ,py=(self.py+(self.vy*sec))%maxy)
    def quad(self,maxx:int,maxy:int):
        x1 = ((maxx-1)/2)-1
        x2 = ((maxx-1)/2)+1
        y1 = ((maxy-1)/2)-1
        y2 = ((maxy-1)/2)+1
        if self.px <= x1 and self.py <= y1 :
            return 1
        elif self.px >= x2 and self.py <= y1 :
            return 2
        elif self.px <= x1 and self.py >= y2 :
            return 3
        elif self.px >= x2 and self.py >= y2 :
            return 4
        else :
            return None

def move_robots(i,_robots):
    return [r.move(i,maxX,maxY) for r in _robots]

def robots_mat(_robots):
    Z = np.zeros([maxX, maxY], dtype=np.uint8)
    for r in _robots :
        Z[(r.px,r.py)] += 1
    return Z

def robots_img(_robots):
    Z = np.zeros([maxX, maxY, 3], dtype=np.uint8)
    for r in _robots :
        Z[(r.px,r.py)] = 255
    return Image.fromarray(Z)


pos_vel = mapt(lambda z: mapt(lambda y: int(y), z), [x[0] for x in [re.findall(regex, line) for line in in_part_A]])
robots = [Robot(*t) for t in pos_vel]
M = robots_mat(move_robots(0,robots))
sY,sX = M.sum(axis=0,),M.sum(axis=1)


# Setting up a random number generator with a fixed state for reproducibility.
rng = np.random.default_rng(seed=19680801)
# Fixing bin edges.
#HIST_BINS = np.linspace(-4, 4, 100)
HIST_BINS = 100

# Histogram our data with numpy.
data = rng.standard_normal(1000)
n, _ = np.histogram(data, HIST_BINS)
n, _ = np.histogram(sX, HIST_BINS)
#print(sX)

def animate(i, bar_container):
    # Simulate new data coming in.
    data = rng.standard_normal(1000)
    n, _ = np.histogram(data, HIST_BINS)
    M = robots_mat(move_robots(i,robots))
    sY,sX = M.sum(axis=0,),M.sum(axis=1)
    n, _ = np.histogram(sX, HIST_BINS)
    print(i,sX)
    for count, rect in zip(n, bar_container.patches):
        rect.set_height(count)

    return bar_container.patches


fig, ax = plt.subplots()
#_, _, bar_container = ax.hist(data, HIST_BINS, lw=1, ec="yellow", fc="green", alpha=0.5)
_, _, bar_container = ax.hist(sX, HIST_BINS, lw=1, ec="yellow", fc="green", alpha=0.5)
ax.set_ylim(top=100)  # set safe limit to ensure that all data is visible.

anim = functools.partial(animate, bar_container=bar_container)
ani = animation.FuncAnimation(fig, anim, 101*103, repeat=False, blit=True)
plt.show()
