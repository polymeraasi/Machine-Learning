"""
To do: Q-learning with taxi-v3 environment

"""

# Load OpenAI Gym and other necessary packages
import gym
import random
import numpy
import time

# Environment
env = gym.make("Taxi-v3")

# Training parameters for Q learning
alpha = 0.9 # Learning rate
gamma = 0.9 # Future reward discount factor
num_of_episodes = 1000
num_of_steps = 500 # per each episode

epsilon = 0.1
decayRate = 0.005  #to decrease epsilon

# Could not get it to work with given tables so decided to put the table to zero
Q_reward = numpy.zeros([env.observation_space.n, env.action_space.n])

# Training w/ random sampling of actions
# YOU WRITE YOUR CODE HERE

for episode in range(num_of_episodes):
    state = env.reset()
    done = False

    for step in range(num_of_steps):

        if random.uniform(0,1) < epsilon:
            action = env.action_space.sample()
        else:
            action = numpy.argmax(Q_reward[state, :])


        new_state, reward, done, info = env.step(action)

        Q_reward[state,action] = Q_reward[state, action] + alpha * \
                                 (reward + gamma * numpy.max(Q_reward[new_state, :])- Q_reward[state, action])
        state = new_state

        if done == True:
            break

    epsilon = numpy.exp(-decayRate*episode)

# Testing

state = env.reset()
tot_reward = 0
num_actions = 0
for t in range(50):
    action = numpy.argmax(Q_reward[state,:])
    state, reward, done, info = env.step(action)
    tot_reward += reward
    num_actions += 1
    env.render()
    time.sleep(1)
    if done:
        print("Total reward %d" %tot_reward)
        print(f"Total actions: {num_actions}")
        break