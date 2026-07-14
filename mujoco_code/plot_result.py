import os
import numpy as np
import matplotlib.pyplot as plt

# ==========================
# Config
# ==========================
root = "../DDPG/Hopper-v4"
seeds = [1]

smooth_alpha = 0.05      # 越小越平滑，可尝试0.03~0.1

# ==========================
# EMA Smooth
# ==========================
def smooth(x, alpha=0.05):
    y = np.zeros_like(x)
    y[0] = x[0]
    for i in range(1, len(x)):
        y[i] = alpha * x[i] + (1 - alpha) * y[i-1]
    return y

# ==========================
# Load
# ==========================
rewards = []

for seed in seeds:
    r = np.load(os.path.join(root,
                             f"DDPG_seed{seed}",
                             "episode_rewards.npy"))
    rewards.append(r)

min_len = min(map(len, rewards))
rewards = np.array([r[:min_len] for r in rewards])

# ==========================
# Mean ± Std
# ==========================
mean = rewards.mean(axis=0)
std = rewards.std(axis=0, ddof=1)

# 再进行平滑（论文中较常见）
mean = smooth(mean, smooth_alpha)
std = smooth(std, smooth_alpha)

# ==========================
# Plot
# ==========================
episodes = np.arange(min_len)
plt.figure(figsize=(6,4.5))

plt.plot(
    episodes,
    mean,
    lw=2,
    label="DDPG",
)

plt.fill_between(
    episodes,
    mean-std,
    mean+std,
    alpha=0.25,
)

plt.xlabel("Episode")
plt.ylabel("Episode Return")

plt.grid(ls="--", alpha=0.4)
plt.legend(frameon=False)

plt.tight_layout()
plt.savefig("DDPG_mean_std.png", dpi=300)
plt.show()