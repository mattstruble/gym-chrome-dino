#!/usr/bin/env python
#
# Copyright (C) 2019 Matt Struble
# Licensed under the MIT License - https://opensource.org/licenses/MIT

import os

from gym.envs.registration import register

register(
    id='ChromeDino-v0',
    entry_point='gym_chrome_dino.envs:ChromeDinoEnv',
    kwargs={'render': True, 'chrome_driver_path': os.environ.get('CHROME_DRIVER_PATH')}
)