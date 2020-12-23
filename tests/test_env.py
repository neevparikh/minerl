import gym
import minerl 
env = gym.make('MineRLTreechop-v0')
obs = env.reset()
steps = 0 
done = False
while steps < 1000 and not done:
    ret = env.step(env.action_space.sample())
    print(ret[-1])
    steps += 1
