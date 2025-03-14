import gymnasium as gym  
import gym_anytrading
import numpy as np
import pandas as pd
from stable_baselines3 import PPO
from gymnasium import spaces
from gymnasium.wrappers import TimeLimit
from gym_anytrading.envs import StocksEnv  


df = pd.read_csv("sample_stock_data.csv")

window_size = 10
frame_bound = (window_size, len(df))

class CustomStocksEnv(StocksEnv):
    def __init__(self, df, window_size, frame_bound):
        super().__init__(df, window_size, frame_bound)
        self.action_space = spaces.Discrete(3)  
        self.observation_space = spaces.Box(low=-np.inf, high=np.inf, shape=(window_size, 2), dtype=np.float32)  

env = CustomStocksEnv(df=df, window_size=window_size, frame_bound=frame_bound)

env = TimeLimit(env, max_episode_steps=1000)

model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=10000)

def trade(env):
    obs, _ = env.reset() 
    while True:
        action, _states = model.predict(obs)
        obs, rewards, done, _, info = env.step(action)  
        print(f"Action: {action}, Reward: {rewards}")

        if done:
            print("Trade Execution Completed.")
            break


if __name__ == "__main__":
    trade(env)
