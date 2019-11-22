# gym-chrome-dino
OpenAI gym for the Google Chrome Dino game.

## Installation

```bash
git clone https://github.com/mattstruble/gym-chrome-dino.git
cd gym-chrome-dino
pip install -e .
```

## Usage

```python
import gym
import gym_chrome_dino
env = gym.make('ChromeDino-v0')
```

### State, Actions, and Rewards

* The state is a RGB numpy array with shape of (150, 600, 3).
* The available actions are 0: _do nothing_, 1: _jump_, and 2: _duck_.
* A positive reward 1 is given when the dinosaur is alive; a negative penalty -10 is given when the dinosaur hits an obstacle.

## WebDriver

`gym-chrome-dino` runs the game via `selenium` in order to monitor and control the game.

Ensure you have the latest [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) that matches your chrome installation.

Add the full path to `chromedriver` to your system:

#### Windows:

Add a new system environment PATH equal to: `CHROME_DRIVER_PATH=path\to\chromedriver.exe`.

#### Linux:

Add the following to your `~/.bash_profile` (or `~/.zshrc`, or whatever profile you use):

```bash
export CHROME_DRIVER_PATH=path/to/chromedriver
```