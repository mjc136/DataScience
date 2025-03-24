import gymnasium as gym
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import random
from collections import deque

# Set device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Define Q-network
class QNetwork(nn.Module):
    def __init__(self, input_dim, output_dim):
        super(QNetwork, self).__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, 128),
            nn.ReLU(),
            nn.Linear(128, 128),
            nn.ReLU(),
            nn.Linear(128, output_dim)
        )

    def forward(self, x):
        return self.net(x)

# Load environment
env = gym.make("LunarLander-v3", render_mode="human")
input_dim = env.observation_space.shape[0]
output_dim = env.action_space.n

# Load model
model = QNetwork(input_dim, output_dim).to(device)
model.load_state_dict(torch.load("ReinforcementLearning\LunarLander\lunarlander_dqn.pth"))
model.eval()

# Run one episode
state, _ = env.reset()
done = False
total_reward = 0

while not done:
    env.render()
    state_tensor = torch.tensor(state, dtype=torch.float32).unsqueeze(0).to(device)
    with torch.no_grad():
        q_values = model(state_tensor)
        action = torch.argmax(q_values).item()
    next_state, reward, terminated, truncated, _ = env.step(action)
    done = terminated or truncated
    total_reward += reward
    state = next_state

env.close()
print(f"LunarLander Test Run Total Reward: {total_reward}")