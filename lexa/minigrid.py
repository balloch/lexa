from envs.base_envs import BenchEnv
import gym_minigrid
import gym


class MiniGrid(BenchEnv):

    def __init__(self, env_name, action_repeat=1, use_goal_idx=False, log_per_goal=False, width=64) -> None:
        super().__init__(action_repeat, width)
        
        self.use_goal_idx = use_goal_idx
        self.log_per_goal = log_per_goal

        with self.LOCK:
            env = gym.make(env_name)
            self._env = gym_minigrid.wrappers.RGBImgObsWrapper(env, tile_size=8)
    
        self._env.reset()
        self.goal_idx = 0

    def set_goal_idx(self, idx):
        self.goal_idx = idx

    def get_goal_idx(self):
        return self.goal_idx

    def get_goals(self):
        return []

    def _get_obs(self, state):
        