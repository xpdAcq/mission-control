import os
from contextlib import contextmanager

import requests
from xonsh.lib.os import indir

git clone git@github.com:NSLS-II/lightsource2-recipes.git

pkgs = []
for f in ['../developed_pkgs.txt', '../maintained_pkgs.txt']:
    with open(f, 'r') as ff:
        pkgs.extend(ff.read().split('\n'))

with indir('lightsource2-recipes/recipes-tag'):
    t = 'https://raw.githubusercontent.com/conda-forge/{}-feedstock/' \
        'master/recipe/meta.yaml'
    for b in pkgs:
        os.makedirs(b, exist_ok=True)
        with indir(b):
            url = t.format(b)
            request = requests.get(url)
            if request.status_code == 200:
                # TODO: pull all contents of the recipe folder
                # TODO: remove all contents of the recipe folder
                if 'meta.yaml' in g`*`:
                    rm meta.yaml
                wget @(url)
    git commit -am "update XPD pacakges"
print('Please push and PR these changes')
