import matplotlib.pyplot as plt # pip install matplotlib
import numpy as np # pip install numpy
import time


def plot_route(cities,route,fig,ax,clf=True):

    l1 = ax.plot(cities[route,0], cities[route,1], 'k-o', markersize=10)
    l2 = ax.plot(cities[route[[0,-1]],0], cities[route[[0,-1]],1], 'k-o', markersize=10)

    fig.canvas.draw()

    time.sleep(0.1)

    if clf:
        l = l1.pop()
        l.remove()
        l = l2.pop()
        l.remove()

def generate_neighbor(route):

    city1 = np.random.randint(route.shape[0])
    city2 = np.random.randint(route.shape[0])

    neighbor = route.copy()
    neighbor[city1] = route[city2]
    neighbor[city2] = route[city1]

    return neighbor

def evaluate_route(route,cities):
    cost = 0
    route_c = cities[route,:]

    for i in range(route_c.shape[0]-1):
        cost += np.linalg.norm(route_c[i,:]-route_c[i+1,:])

    cost += np.linalg.norm(route_c[-1,:]-route_c[0,:])

    return cost


# Plot stuff
plt.ion()
fig = plt.figure()
plt.ylim(-0.1,10.1)
plt.xlim(-0.1,10.1)
ax = fig.add_subplot(111)

# Generating map
n = 20
cities = np.random.random((n,2))*10

# Generating initial solution
route = np.random.permutation(cities.shape[0])
best = evaluate_route(route,cities)


# Running local search
no_improvement = 0
counter = 0

while no_improvement < 100:
    counter += 1

    neighbor = generate_neighbor(route)

    cost = evaluate_route(neighbor,cities)

    if cost <= best:
        route = neighbor
        best = cost
        print('best: {} cost: {} iteration: {}'.format(best,cost,counter))
        if cost < best:
            no_improvement = 0
    else:
      no_improvement+=1  

    plot_route(cities,route,fig,ax)


plot_route(cities,route,fig,ax,clf=False)
input()