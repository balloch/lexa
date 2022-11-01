from envs.base_envs import BenchEnv

class MiniGrid(BenchEnv):

    def __init__(self, action_repeat=1, use_goal_idx=False, log_per_goal=False, width=64) -> None:
        super().__init__(action_repeat, width)
        
        self.use_goal_idx = use_goal_idx
        self.log_per_goal = log_per_goal

        with self.LOCK:
            pass
    