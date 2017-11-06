from git import Repo
import os


def create_repo_dict(repo_path, authors=None):
    l = {}
    r = Repo(repo_path)
    tags = r.tags
    for tag in tags:
        d = dict(title=os.path.split(repo_path)[-1],
                 version=str(tag),
                 date=str(tag.commit.committed_datetime.date()),
                 url='https://github.com/xpdAcq/' + os.path.split(
                     repo_path)[-1])
        if authors:
            d['author'] = authors
        l[str(tag)] = d
    return l


def track_repos(repo_path_list, authors_list):
    l = {}
    for rp, authors in zip(repo_path_list, authors_list):
        l[os.path.split(rp)[-1]] = (create_repo_dict(rp, authors))
    return l


if __name__ == '__main__':
    from pprint import pprint
    a = '/home/christopher/dev/'
    rl = [a + b for b in ['xpdAn', 'xpdAcq', 'SHED', 'streamz']]
    g = ('Simon J. L. Billinge', 'Christopher J. Wright')
    authors_list = [g + ('Timothy Liu',),
                    g + ('Timothy Liu',),
                    g + ('Timothy Liu', 'Julien Lhermitte'),
                    g + ('Julien Lhermitte', 'Matthew Rocklin')]
    pprint(track_repos(rl, authors_list))