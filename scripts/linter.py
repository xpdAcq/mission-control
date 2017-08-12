import os
from .copyright_linter import lint_for_copyright

linters = [lint_for_copyright]

def main():
    lint = []
    blacklist = open('.linter_ignore', 'r').readlines()
    whitelist = open('.linter_include', 'r').readlines()
    files = [f for f in os.listdir('.') if f.endswith('.py') and f not in blacklist]
    files += whitelist
    for file in files:
        with open(file, 'r') as f:
            for linter in linters:
                lines = f.readlines()
                lint.append(linter(lines))

if __name__ == '__main__':
    main()