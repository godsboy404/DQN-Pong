import matplotlib.pyplot as plt
import numpy as np

def main():
    plt.rc("font", family='Microsoft YaHei')
    rewards_dqn_nature = np.loadtxt('rewards_per_episode_dqn_nature.csv', delimiter=',')
    rewards_dqn_lonely = np.loadtxt('rewards_per_episode.csv', delimiter=',')
    plt.plot(rewards_dqn_nature,label='Nature版')
    plt.plot(rewards_dqn_lonely,label='自训练版')

    plt.xlabel('Episode')
    plt.ylabel('Reward')
    plt.title('Atari-Pong 每轮奖励（Nature版 Vs. 自训练版）')
    plt.legend()
    plt.savefig('results_per_episode.png')
    plt.show()

if __name__== "__main__":
  main()

