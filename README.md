## Requirements

- Python
- pipenv
- MIGI

## Setup

1. Inside the `src` directory, run `pipenv install` to install our Python dependencies
2. Copy the folders inside `migi_addons` folder into the MIGI addons directory, usually `C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Global Offensive\migi\csgo\addons`
3. Copy the `__custom_skin` folder into the CS:GO base directory, usually `C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Global Offensive`

## Usage

1. Inside the `src` directory, run `pipenv shell` to use the subshell in virtual environment
2. Run `python skin_screenshot.py <inputConfigFilePath> <screenshotOutputDirectoryPath>`, for example `python skin_screenshot.py C:\Users\Anon\Downloads\screenshots\tmp\screenshots\base_knives.json C:\Users\Anon\Downloads\screenshots\tmp\output`
3. Open MIGI, build the addons (if you want to build without weapon modification, just delete the `m_workbench_weapon_replacement.vpk` before building), and launch the game
