import numpy as np
import random

alpha = 0.05
gamma = 0.9
h, w = 5, 8
# h, w = 4, 4
start = [0, 0]
agent = start
state = 1
goal = [h-1, w-1]
# actions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
actions = [(1,0), (-1,0), (0,-1), (0,1)]



#q = np.random.randint(0, len(actions), size = (len(actions), h, w))
q = np.zeros((len(actions), h, w), dtype=float)
r = np.ones((len(actions), h, w), dtype=float) * -1
r[:,*goal] = 0

# grid[agent[0], agent[1]] = 1
# r[goal[0],goal[1]] = 1

np.set_printoptions(precision=4, suppress=True)

def pick_action_random(s):
    ai = random.randint(0, len(actions)-1)
    dy,dx = actions[ai]
    print("action = ", dy, dx)
    ns = s
    ny,nx = (s[0]+dy, s[1]+dx)
    if 0 <= ny < h:
        ns[0] = ny
    if 0 <= nx < w:
        ns[1] = nx
    print("s       = ", s)
    print("s_next  = ", ns)
    return (ai, ns) # (action-index, next state) pair

def policy_random(s):
    global q
    print("s = ", s)
    ai = random.randint(0, len(actions)-1)
    dy,dx = actions[ai]
    print("action = ", dy, dx)
    ns = s
    ny,nx = (s[0]+dy, s[1]+dx)
    if 0 <= ny < h:
        ns[0] = ny
    if 0 <= nx < w:
        ns[1] = nx
    print("s       = ", s)
    print("s_next  = ", ns)

    reward = r[ai][*s]
    av = q[ai][*s]
    av_next = q[ai][*ns]
    print("reward  = ", reward)
    print("av      = ", av)
    print("av_next = ", av_next)
    q_upd = av + alpha * (reward + gamma * av_next - av)
    print("q_upd   = ", q_upd)
    q[ai][*s] = q_upd
    return ns

def policy_greedy(s):
    global q
    print("s = ", s)

    # chose the action
    action = None
    av_max = (0,0,0) # (action-value, action-index, next state) tuple
    for ai in range(len(actions)):
        dy,dx = actions[ai]
        print("action = ", dy, dx)
        ns = s
        ny,nx = (s[0]+dy, s[1]+dx)
        if 0 <= ny < h:
            ns[0] = ny
        if 0 <= nx < w:
            ns[1] = nx
        print("s       = ", s)
        print("s_next  = ", ns)
        av_next = q[ai][*ns]
        print("av_max  = ", av_max)
        av_max = (av_next, ai, ns) if (av_next > av_max[0]) else av_max

    # if no action is better, pick at random
    if av_max[2] == None:
        ai, ns = pick_action_random(s)
        reward = r[ai][*s]
        av_next = q[ai][*ns]
    else:
        av_next, ai, ns = av_max

    # update Q for the chosen action
    av = q[ai][*s]
    print("ai  = ", av_max)

    q_upd = av + alpha * (reward + gamma * av_next - av)
    print("q_upd   = ", q_upd)
    print("s       = ", s)
    print("s_next  = ", ns)
    q[ai][*s] = q_upd

    return ns


def step(agent):
    print("q = ")
    print(q)
    # s = policy_random(agent)
    s = policy_greedy(agent)
    print("s' = ", s)
    x = np.zeros((h, w), dtype=float)
    x[*s] = 666
    print(x)

    return s

# init Q(s,a)


while True:
    print("r = ")
    print(r)
    agent = step(agent)
    if agent == goal:
        exit(0)
    x = input()
    print(x)

