## Requirements

- Python
- pipenv

## Setup

1. Copy the folders `mod_gun`, `mod_knive`, and `__custom_skin` to the CS:GO root folder, usually `C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Global Offensive`
2. Run `pipenv install` to install our Python dependencies

## Usage

1. Run `pipenv shell` to use the subshell in virtual environment
2. Run `python skin_screenshot.py <inputConfigFilePath> <screenshotOutputDirectoryPath>`, for example `python skin_screenshot.py C:\Users\Anon\Downloads\screenshots\tmp\screenshots\base_guns.txt C:\Users\Anon\Downloads\screenshots\tmp\output`
