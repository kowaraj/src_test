import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.widgets as widgets
import numpy as np
import random

w, h = 10, 5
start = [2, 0]
agent = start
state = 1
goal = [2, 3]

fig, ax = plt.subplots()
grid = np.ones((h, w))
r = np.zeros((h, w))
r[goal[0],goal[1]] = 1
q = np.ones((h, w))
states = grid
grid[agent[0], agent[1]] = 1
im = ax.imshow(grid, cmap='gray', vmin=0, vmax=1)
ax.set_xticks([])
ax.set_yticks([])

ax_label_x = plt.axes([0.05, 0.05, 0.1, 0.075])
ax_label_y = plt.axes([0.3, 0.05, 0.1, 0.075])
label_x = widgets.TextBox(ax_label_x, 'X: ', initial=str(agent[1]))
label_y = widgets.TextBox(ax_label_y, 'Y: ', initial=str(agent[0]))

moves = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

def policy(s):
    xy = moves[random.randint(1,7)]
    print(xy)
    return xy

def update_labels():
    label_x.set_val(str(agent[1]))
    label_y.set_val(str(agent[0]))

def update(frame):
    global state
    global states
    global agent
    print('grid:', states)
    print('agent:', agent)
    if state == 0:
        print('agent put on staart')
        agent = start
        state = 1
        return


    # dy, dx = random.choice(moves)
    dy, dx = policy(agent)
    ny, nx = agent[0] + dy, agent[1] + dx
    if 0 <= ny < h and 0 <= nx < w:
        agent = [ny, nx]
    if nx >= 3:
        print("goal reached, stop!")
        state = 0

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



def step_cb(event):
    print('step')
    update(0)

def start_cb(event):
    print('start')
    global agent, state
    state = 1
    agent = [h//2, w//2]

def stop_cb(event):
    print('stop')
    global agent, state
    state = 0
    agent = [h//2, w//2]

ax_button = plt.axes([0.6, 0.05, 0.1, 0.075])
button_step = widgets.Button(ax_button, 'Step')
button_step.on_clicked(step_cb)

ax_button = plt.axes([0.7, 0.05, 0.1, 0.075])
button_start = widgets.Button(ax_button, 'Start')
button_start.on_clicked(start_cb)
ax_button = plt.axes([0.8, 0.05, 0.1, 0.075])
button_stop = widgets.Button(ax_button, 'Stop')
button_stop.on_clicked(stop_cb)


plt.show()

