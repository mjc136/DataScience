import gymnasium as gym
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import random
from collections import deque

# Set random seeds for reproducibility
seed = 42
np.random.seed(seed)
torch.manual_seed(seed)
random.seed(seed)

# Check for GPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Define the Q-network class
class QNetwork(nn.Module):
    def __init__(self, input_dim, output_dim):
        super(QNetwork, self).__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, 24),
            nn.ReLU(),
            nn.Linear(24, 24),
            nn.ReLU(),
            nn.Linear(24, output_dim)
        )

    def forward(self, x):
        return self.net(x)

# Create the CartPole environment
env = gym.make("CartPole-v1", render_mode="human")
input_dim = env.observation_space.shape[0]
output_dim = env.action_space.n

# Initialise networks
model = QNetwork(input_dim, output_dim).to(device)
target_model = QNetwork(input_dim, output_dim).to(device)
target_model.load_state_dict(model.state_dict())
target_model.eval()

# Hyperparameters
gamma = 0.99
epsilon = 1.0
epsilon_min = 0.1
epsilon_decay = 0.995
batch_size = 64
max_memory_length = 100000
update_target_every = 5
learning_rate = 0.001
episodes = 500

# Optimiser and loss function
optimizer = optim.Adam(model.parameters(), lr=learning_rate)
criterion = nn.MSELoss()

# Replay memory
memory = deque(maxlen=max_memory_length)

# Main training loop
for episode in range(episodes):
    state, _ = env.reset()
    state = torch.tensor(state, dtype=torch.float32).to(device)
    total_reward = 0
    done = False

    while not done:
        if np.random.rand() < epsilon:
            action = np.random.randint(output_dim)
        else:
            with torch.no_grad():
                q_values = model(state.unsqueeze(0))
                action = torch.argmax(q_values).item()

        next_state, reward, terminated, truncated, _ = env.step(action)
        done = terminated or truncated
        next_state_tensor = torch.tensor(next_state, dtype=torch.float32).to(device)

        memory.append((state, action, reward, next_state_tensor, done))
        state = next_state_tensor
        total_reward += reward

        if len(memory) >= batch_size:
            minibatch = random.sample(memory, batch_size)
            states, actions, rewards, next_states, dones = zip(*minibatch)

            states = torch.stack(states)
            next_states = torch.stack(next_states)
            actions = torch.tensor(actions).to(device)
            rewards = torch.tensor(rewards).to(device)
            dones = torch.tensor(dones).to(device)

            q_values = model(states)
            q_values = q_values.gather(1, actions.unsqueeze(1)).squeeze(1)

            with torch.no_grad():
                next_q_values = target_model(next_states).max(1)[0]
                target_q = rewards + gamma * next_q_values * (~dones)

            loss = criterion(q_values, target_q)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

    if episode % update_target_every == 0:
        target_model.load_state_dict(model.state_dict())

    if epsilon > epsilon_min:
        epsilon *= epsilon_decay

    print(f"Episode {episode+1}/{episodes} - Reward: {total_reward}, Epsilon: {epsilon:.3f}")

env.close()

torch.save(model.state_dict(), "ReinforcementLearning/CartPole/dqn_cartpole.pth")
print("Model saved as ReinforcementLearning/CartPole/dqn_cartpole.pth")


