#!/usr/bin/env python
#
# Copyright (C) 2019 Matt Struble
# Licensed under the MIT License - https://opensource.org/licenses/MIT

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

class ChromeDino():

    def __init__(self, chrome_driver_path=None, render=False):
        self.webdriver = webdriver.Chrome(executable_path=chrome_driver_path, options=self._get_options(render))
        self.webdriver.get('chrome://dino')

    def _get_options(self, render):
        options = Options()

        options.add_argument('--disable-infobars')
        options.add_argument('--mute-audio')
        options.add_argument('--no-sandbox')
        options.add_argument('--window-size=800,600')

        if not render:
            options.add_argument('--headless')

        return options

    def jump(self):
        return self.webdriver.find_element_by_tag_name('body').send_keys(Keys.SPACE)

    def duck(self):
        return self.webdriver.find_element_by_tag_name('body').send_keys(Keys.DOWN)

    def start(self):
        return self.jump()

    def restart(self):
        self.webdriver.get('chrome://dino')
        return self.start()

    def get_canvas(self):
        return self.webdriver.execute_script('return document.getElementsByClassName("runner-canvas")[0].toDataURL().substring(22);')

    def close(self):
        self.webdriver.close()