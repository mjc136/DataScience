import time
import torch
import gymnasium as gym

# Set device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Define the same architecture used during training
class QNetwork(torch.nn.Module):
    def __init__(self, input_dim, output_dim):
        super(QNetwork, self).__init__()
        self.net = torch.nn.Sequential(
            torch.nn.Linear(input_dim, 24),
            torch.nn.ReLU(),
            torch.nn.Linear(24, 24),
            torch.nn.ReLU(),
            torch.nn.Linear(24, output_dim)
        )

    def forward(self, x):
        return self.net(x)

# Load environment
env = gym.make("CartPole-v1", render_mode="human")
input_dim = env.observation_space.shape[0]
output_dim = env.action_space.n

# Load model and weights
model = QNetwork(input_dim, output_dim).to(device)
model.load_state_dict(torch.load("ReinforcementLearning/CartPole/dqn_cartpole.pth"))
model.eval()

# Run one test episode
state, _ = env.reset()
done = False
total_reward = 0

while not done:
    env.render()
    time.sleep(0.02)

    state_tensor = torch.tensor(state, dtype=torch.float32).unsqueeze(0).to(device)
    with torch.no_grad():
        action = torch.argmax(model(state_tensor)).item()

    next_state, reward, terminated, truncated, _ = env.step(action)
    done = terminated or truncated
    state = next_state
    total_reward += reward

env.close()
print(f"Test run reward: {total_reward}")
