from git import Repo
import os
from bibtexparser.bwriter import BibTexWriter, BibDatabase


def create_repo_dict(repo_path, authors=None,
                     base_url='https://github.com/xpdAcq/'):
    l = {}
    r = Repo(repo_path)
    tags = r.tags
    print(r, len(tags))
    for tag in tags:
        d = dict(title=os.path.split(repo_path)[-1],
                 version=str(tag),
                 year=str(tag.commit.committed_datetime.year),
                 month=str(tag.commit.committed_datetime.month),
                 url=base_url + os.path.split(repo_path)[-1],
                 ENTRYTYPE='software')
        if authors:
            d['author'] = ', '.join(authors)
        d['ID'] = d['title'] + '-' + d['version']
        d['grant'] = 'DMREF'
        l[str(tag)] = d
    return l


def track_repos(repo_path_list, authors_list, base_urls):
    l = {}
    for rp, authors, base_url in zip(repo_path_list, authors_list, base_urls):
        l[os.path.split(rp)[-1]] = (create_repo_dict(rp, authors, base_url))
    return l


if __name__ == '__main__':
    from pprint import pprint
    a = '/home/christopher/dev/'
    if not os.path.isdir(a):
        a = '/Users/timothyliu/Repo/'
    rl = [a + b for b in ['streamz_ext', 'xpdtools', 'xpdAn', 'xpdAcq', 'SHED', 'streamz']]
    authors_list = [('Christopher J. Wright', 'Simon J. L. Billinge'), 
                    ('Christopher J. Wright', 'Simon J. L. Billinge'),
                    ('Christopher J. Wright', 'Chia-Hao Liu',
                     'Simon J. L. Billinge'),
                    ('Chia-Hao Liu', 'Christopher J. Wright',
                     'Simon J. L. Billinge'),
                    ('Christopher J. Wright', 'Chia-Hao Liu',
                     'Julien Lhermitte', 'Simon J. L. Billinge'),
                    ('Christopher J. Wright', 'Matthew Rocklin',
                     'Julien Lhermitte', 'Simon J. L. Billinge')]
    s = track_repos(rl, authors_list, ['https://github.com/xpdAcq/',
                                       'https://github.com/xpdAcq/',
                                       'https://github.com/xpdAcq/',
                                       'https://github.com/xpdAcq/',
                                       'https://github.com/xpdAcq/',
                                       'https://github.com/mrocklin/'])
    s2 = []
    for k, v in s.items():
        for k2, v2 in v.items():
            s2.append(v2)
#    pprint(s2)
    db = BibDatabase()
    db.entries = s2
    writer = BibTexWriter()
    with open('bg-software.bib', 'w') as bibfile:
        bibfile.write(writer.write(db))

