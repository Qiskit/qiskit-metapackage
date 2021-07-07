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


def main(repos=None, output_path=None):
    # Some contributors have no commits associated with their name, but should also appear in the
    # bib-file (previous Qiskit versions, co-author in some code, intellectual contribution, ...)
    whitelisted_authors = [
        'Andrea Simonetto',  # to Aqua
        'Ivano Tavernelli',  # to Aqua
        'Julia Rice',        # to Aqua
        'Kanav Setia',       # to Aqua
        'Martin Mevissen',   # to Aqua
        'Nikolaj Moll',      # to Aqua
        'Sergey Bravyi',     # to Aqua
        'Tal Kachmann',      # to Aqua
        'Dmitri Maslov',      # to Circuits and Compilers
    ]

    if not repos:
        repos = [
            'https://github.com/Qiskit/qiskit-terra',
            'https://github.com/Qiskit/qiskit-aer',
            'https://github.com/Qiskit/qiskit-aqua',
            'https://github.com/Qiskit/qiskit-ignis',
            'https://github.com/Qiskit/qiskit',
            'https://github.com/Qiskit/qiskit-ibmq-provider',
        ]
    if not output_path:
        output_path = 'AUTHORS'
    authors = []
    emails = []

    def generate_authors(git_dir, meta=False, whitelisted_authors=[]):
        """Create AUTHORS file using git commits."""
        git_log_cmd = ['git', 'log', '--format=%aN|%aE', '--use-mailmap']
        if meta:
            git_log_cmd += ['--', ':!docs/LOCALIZATION_CONTRIBUTORS']
        tmp_authors = _run_shell_command(git_log_cmd, git_dir).split('\n')

        for author_str in tmp_authors:
            author, email = author_str.split('|')
            author = author.strip()
            email = email.strip()
            if author.lower() not in [x.lower() for x in authors]:
                if email.lower() not in [x.lower() for x in emails]:
                    authors.append(author)
                    emails.append(email)

        co_author_cmd = ['git', 'log', '--use-mailmap']
        if meta:
            co_author_cmd += ['--', ':!docs/LOCALIZATION_CONTRIBUTORS']
        co_authors_raw = _run_shell_command(co_author_cmd,
                                            git_dir)
        co_authors = re.findall('Co-authored-by:.+', co_authors_raw,
                                re.MULTILINE | re.I)
        co_authors = [signed.split(":", 1)[1].strip() for signed in co_authors if signed]

        for author_str in co_authors:
            try:
                author, email = author_str.split('<')
            except ValueError:
                continue
            author = author.strip()
            email = email[:-1].strip()
            mailmap_contact = '<' + email + '>'
            mailmap_out = _run_shell_command(['git', 'check-mailmap', mailmap_contact],
                                             git_dir)
            if mailmap_out != mailmap_contact:
                author, email = mailmap_out.split('<')
                author = author.strip()
                email = email[:-1].strip()
            if author.lower() not in [x.lower() for x in authors]:
                if email.lower() not in [x.lower() for x in emails]:
                    authors.append(author)
                    emails.append(email)

        # Add whitelisted authors
        for author in whitelisted_authors:
            if author.lower() not in [x.lower() for x in authors]:
                authors.append(author)

    for repo in repos:
        repo_name = repo.rsplit('/', 1)[-1]
        repo_dir = get_repo(repo, repo_name)
        with repo_dir as repo_dir_path:
            if repo_name == 'qiskit':
                generate_authors(repo_dir_path, True, whitelisted_authors)
            else:
                generate_authors(repo_dir_path, whitelisted_authors=whitelisted_authors)

    # Write out flat authors file
    authors = sorted(set(authors), key=lambda x: (x.split()[-1], x.split()[:]))
    with open(output_path, 'w') as fd:
        for author in authors:
            if author in ['qiskit-bot', 'mergify[bot]']:
                continue
            fd.write(author + '\n')


if __name__ == '__main__':
    main()
