import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.widgets as widgets
import numpy as np
import random

w, h = 10, 5
agent = [2, 0]
state = 1
goal = [2, 3]

fig, ax = plt.subplots()
grid = np.ones((h, w))
r = np.zeros((h, w))
r[goal[0],goal[1]] = 1
q = np.ones((h, w))
states = grid
grid[agent[0], agent[1]] = 0
im = ax.imshow(grid, cmap='gray', vmin=0, vmax=1)
ax.set_xticks([])
ax.set_yticks([])

ax_label_x = plt.axes([0.05, 0.05, 0.1, 0.075])
ax_label_y = plt.axes([0.3, 0.05, 0.1, 0.075])
label_x = widgets.TextBox(ax_label_x, 'X: ', initial=str(agent[1]))
label_y = widgets.TextBox(ax_label_y, 'Y: ', initial=str(agent[0]))

moves = [(-1,-1), (-1,0), (-1,1),
             (0,-1), (0,1),
             (1,-1), (1,0), (1,1)]

def policy(s):
    xy = moves[random.randint(1,7)]
    print(xy)
    return xy

def update_labels():
    label_x.set_val(str(agent[1]))
    label_y.set_val(str(agent[0]))

def update(frame):
    global states
    if state == 0:
        grid = np.ones((h, w))
        im.set_array(grid)
        return [im]

    print('up:', frame)
    print('grid:', states)
    global agent
    # dy, dx = random.choice(moves)
    dy, dx = policy(agent)
    ny, nx = agent[0] + dy, agent[1] + dx
    if 0 <= ny < h and 0 <= nx < w:
        agent = [ny, nx]
    if nx = 3 and ny = 2:
        print("goal reached, stop!")
        state == 0

    grid = states.copy()
    grid[agent[0], agent[1]] = 0
    states[agent[0], agent[1]] = states[agent[0], agent[1]] - 0.1

    im.set_array(grid)
    update_labels()
    return [im]


import itertools
# ani = animation.FuncAnimation(fig, update,
#                               frames=itertools.count(),
#                               interval=100,
#                               blit=True,
#                               cache_frame_data=False)



def step(event):
    print('step')
    update(0)

def start(event):
    print('start')
    global agent, state
    state = 1
    agent = [h//2, w//2]

def stop(event):
    print('stop')
    global agent, state
    state = 0
    agent = [h//2, w//2]

ax_button = plt.axes([0.6, 0.05, 0.1, 0.075])
button_step = widgets.Button(ax_button, 'Step')
button_step.on_clicked(step)

ax_button = plt.axes([0.7, 0.05, 0.1, 0.075])
button_start = widgets.Button(ax_button, 'Start')
button_start.on_clicked(start)
ax_button = plt.axes([0.8, 0.05, 0.1, 0.075])
button_stop = widgets.Button(ax_button, 'Stop')
button_stop.on_clicked(stop)


plt.show()

