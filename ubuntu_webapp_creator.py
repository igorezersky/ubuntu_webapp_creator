import argparse
import os
import shutil
from pathlib import Path

from ruamel.yaml import YAML

DESKTOP_FILE_TEMPLATE = """
[Desktop Entry]
Version=1.0
Type=Application
Terminal=false
Exec={exec}
Name={name}
Comment={name}
Icon={icon}
"""

NATIVEFIER_TEMPLATE = """
nativefier -p linux -a x64 --internal-urls ".*?.{domain}.*?" {others} --name "{name}" "{url}" --flash --maximize
"""


def create_argparser() -> argparse.ArgumentParser:
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        '--config', type=str, required=True,
        help='Path to config.yml file. Required fields: ["app_dir", "name", "url", "icon"]'
    )
    return argparser


if __name__ == '__main__':
    args = create_argparser().parse_args()

    yaml = YAML()
    with open(args.config, 'r', encoding='utf-8') as fp:
        configs = yaml.load(fp)

    app_dir_path = Path(configs['app_dir'])
    exec_path = Path(f'{app_dir_path}/{configs["name"]}-linux-x64/{configs["name"]}')
    icon_path = Path(f'{exec_path.parent}/resources/app/icon.png')
    app_dir_path.mkdir(exist_ok=True, parents=True)

    others = []
    shortcuts_path = Path(configs['shortcuts'])
    if shortcuts_path.exists():
        others.append(f'--global-shortcuts {shortcuts_path}')
    command = NATIVEFIER_TEMPLATE.format(
        name=configs['name'],
        url=configs['url'],
        domain=configs['domain'],
        others=' '.join(others)
    )
    os.system(f'cd {app_dir_path} && {command}')

    shutil.copy(configs['icon'], icon_path)
    os.system(f'convert {icon_path} -resize 600x600 {icon_path}')

    with open(f'{app_dir_path}/{configs["name"]}.desktop', 'w', encoding='utf-8') as fp:
        fp.write(
            DESKTOP_FILE_TEMPLATE.format(exec=exec_path.as_posix(), name=configs['name'], icon=icon_path.as_posix())
        )
