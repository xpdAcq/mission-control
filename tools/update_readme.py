main_format=dict(
    build='[![Build Status](https://travis-ci.org/xpdAcq/{name}.svg?branch=master)](https://travis-ci.org/xpdAcq/{name})',
    coverage='[![codecov](https://codecov.io/gh/xpdAcq/{name}/branch/master/graph/badge.svg)](https://codecov.io/gh/xpdAcq/{name}) ',
    health='[![Code Health](https://landscape.io/github/xpdAcq/{name}/master/landscape.svg?style=flat)](https://landscape.io/github/xpdAcq/{name}/master)',
    version='[![Anaconda-Server Badge](https://anaconda.org/conda-forge/{name}/badges/version.svg)](https://anaconda.org/conda-forge/{name})',
    downloads='[![Anaconda-Server Badge](https://anaconda.org/conda-forge/{name}/badges/downloads.svg)](https://anaconda.org/conda-forge/{name})')

a = '''|{name}|{build}|{coverage}|{health}|{version}|{downloads}|\n'''
c = '''# mission-control
Releases, Installers, Specs, and more!

# Build status
| Repo | Build | Coverage | Health | Version | Downloads|
|:-------:|:-----:|:--------:|:------:|:------:|:------:|
'''
for b in ['xpdSim', 'streamz_ext', 'xpdtools', 'SHED', 'xpdAn', 'xpdAcq',
          'xpd-shadow']:
    z = a.format(**main_format, name=b)
    c += z.format(name=b)
print(c)
with open('../README.md', 'w') as f:
    f.write(c)
