import shutil
from pathlib import Path

home_dir = Path.home()
bin_dir = Path(f'{home_dir}/.local/bin')
bin_dir.mkdir(exist_ok=True, parents=True)

shutil.copy('ubuntu_webapp_creator.py', f'{bin_dir}/ubuntu_webapp_creator.py')


with open(f'{home_dir}/.bashrc', 'a', encoding='utf-8') as fp:
    fp.write(f'\nalias ubuntu_webapp_creator="python {bin_dir}/ubuntu_webapp_creator.py"\n')
