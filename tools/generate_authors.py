#!/usr/bin/env python3

import re
import subprocess
import tempfile


def _run_shell_command(cmd, git_dir):
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE, cwd=git_dir)
    out, _ = proc.communicate()

    return out.strip().decode('utf8', 'replace')


def get_repo(repo_url, name):
    temp_dir = tempfile.TemporaryDirectory(suffix=name)
    subprocess.call(['git', 'clone', repo_url, temp_dir.name])
    return temp_dir


def generate_authors(git_dir):
    """Create AUTHORS file using git commits."""
    authors = []
    emails = []
    git_log_cmd = ['git', 'log', '--format=%aN|%aE']
    tmp_authors = _run_shell_command(git_log_cmd, git_dir).split('\n')
    for author_str in tmp_authors:
        author, email = author_str.split('|')
        author = author.strip()
        email = email.strip()
        if author.lower() not in [x.lower() for x in authors]:
            if email.lower() not in [x.lower() for x in emails]:
                authors.append(author)
                emails.append(email)
    co_authors_raw = _run_shell_command(['git', 'log'], git_dir)
    co_authors = re.findall('Co-authored-by:.+', co_authors_raw,
                            re.MULTILINE)
    co_authors = [signed.split(":", 1)[1].strip().split('<')
                  for signed in co_authors if signed]
    for author_str in co_authors:
        author, email = author_str.split('<')
        author = author.strip()
        email = email[:-1].strip()
        if author.lower() not in [x.lower() for x in authors]:
            if email.lower() not in [x.lower() for x in emails]:
                authors.append(author)
                emails.append(email)
    authors = sorted(set(authors))
    return authors


def main(repos=None, output_path=None):
    if not repos:
        repos = ['https://github.com/Qiskit/qiskit-terra',
                 'https://github.com/Qiskit/qiskit-aer']
    if not output_path:
        output_path = 'AUTHORS'
    authors = {}
    for repo in repos:
        repo_name = repo.rsplit('/', 1)[-1]
        repo_dir = get_repo(repo, repo_name)
        with repo_dir as repo_dir_path:
            authors[repo_name] = generate_authors(repo_dir_path)
    with open(output_path, 'w') as fd:
        for repo_name in authors:
            fd.write('%s:\n' % repo_name)
            underline = '-' * len(repo_name)
            fd.write(underline + '\n')
            for author in authors[repo_name]:
                fd.write(author + '\n')
            fd.write('\n')


if __name__ == '__main__':
    main()
