# CartPole with DQN

## 23/03/2025

I prompted GPT-4 for ideas on a reinforcement learning model and decided to implement the CartPole environment.

Initially, I used TensorFlow, but due to issues with GPU recognition, I switched to PyTorch. After that, I asked GPT to generate a test script, which became `test.py`. The training script was also updated to save the model, and the test script now loads it successfully.

The model achieved the maximum possible score during testing.

![alt text](image.png)

The CartPole environment is a classic reinforcement learning problem where an agent must learn to balance a pole on a moving cart by applying forces to the cart. It provides a good starting point for experimenting with Deep Q-Networks (DQNs) due to its simplicity and well-defined reward structure.

After completing CartPole, I asked GPT to suggest a more complex environment. It recommended LunarLander. Initially, the code used version `v2`, which is now deprecated, so I updated it to `v3`. After installing the required dependencies and resolving a few runtime errors (which GPT helped fix), the environment ran successfully.

The LunarLander environment is a more advanced task that requires the agent to control a lander to safely reach the surface, using discrete actions like firing left, right, or main engines. It introduces more complex state dynamics and rewards, making it suitable for testing more robust reinforcement learning algorithms. This simualtion took notably longer to run due to more complexity. The model first had to leanr to to instantly crash but then learn how to levate and then slowly come to a land.

Above environments use OpenAI Gymnasium as the simulation platform. The models are implemented using PyTorch, a popular deep learning library that provides GPU acceleration and flexible model building for neural networks.

## 24/03/2025

began markdown


