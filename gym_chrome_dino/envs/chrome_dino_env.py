#!/usr/bin/env python
#
# Copyright (C) 2019 Matt Struble
# Licensed under the MIT License - https://opensource.org/licenses/MIT

import base64
import io
import os
import cv2
import gym
import numpy as np
from PIL import Image
from gym import spaces
from gym import utils

from gym_chrome_dino.game.chrome_dino import ChromeDino


class ChromeDinoEnv(gym.Env, utils.EzPickle):
    metadata = {'render.modes': ['rgb_array']}

    def __init__(self, chrome_driver_path, render):
        utils.EzPickle.__init__(
            self,
            chrome_driver_path,
            render
        )

        self.game = ChromeDino(chrome_driver_path=chrome_driver_path, render=render)

        self.observation_space = spaces.Box(
            low=0, high=255, shape=(150, 600, 3), dtype=np.uint8
        )

        self._action_set = [0, 1, 2]
        self.action_space = spaces.Discrete(len(self._action_set))

        self.reward = 1
        self.penalty = -10

        self.frame = self.observation_space.low
        self.template = cv2.imread(os.path.join(os.path.dirname(__file__),'game_over_template.png'))

    def step(self, action):
        if action not in self._action_set:
            raise ValueError("Invalid action: " + action)

        if action == 1:
            self.game.jump()
        elif action == 2:
            self.game.duck()

        state = self._update()

        if self._is_game_over():
            reward = self.penalty
            done = True
        else:
            reward = self.reward
            done = False

        return state, reward, done, {}

    def reset(self):
        self.game.restart()
        return self._update()

    def render(self, mode='rgb_array'):
        if mode is not 'rgb_array':
            raise ValueError("Only supports rgb_array mode")

        return self.frame

    def close(self):
        self.game.close()

    def _is_game_over(self):
        bgr = cv2.cvtColor(self.frame, cv2.COLOR_RGB2BGR)

        match = cv2.matchTemplate(bgr, self.template, cv2.TM_CCOEFF_NORMED)
        _, confidence, _, _ = cv2.minMaxLoc(match)

        return confidence >= 0.29

    def _update(self):
        bytearray = io.BytesIO(base64.b64decode(self.game.get_canvas()))
        rgba = Image.open(bytearray)

        # convert RGBA image into RBG
        rgb = Image.new("RGB", rgba.size, (255, 255, 255))
        rgb.paste(rgba, mask=rgba.split()[3])

        self.frame = np.array(rgb)
        return self.frame

    def get_action_meanings(self):
        return [ACTION_MEANING[i] for i in self._action_set]


ACTION_MEANING = {
    0 : "NOOP",
    1 : "JUMP",
    2 : "DUCK"
}
