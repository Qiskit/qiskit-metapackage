# -*- coding: utf-8 -*-

# This code is part of Qiskit.
#
# (C) Copyright IBM 2018.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

import os
import re
import subprocess
from functools import partial

from docutils import nodes
from docutils.parsers.rst.directives.tables import Table
from docutils.parsers.rst import Directive, directives

translations = [
    ('', 'English'),
    ('ja', 'Japanese')
]

def setup(app):
    app.connect('config-inited', _extend_html_context)
    app.add_config_value('content_prefix', '', '')
    app.add_directive('version-history', _VersionHistory)
    _extend_html_context(app.config.html_context, app.config)

def _extend_html_context(app, config):
    context = config.html_context
    context['translations'] = translations
    context['current_translation'] = _get_current_translation(config)
    context['translation_url'] = partial(_get_translation_url, config)
    context['version_list'] = _get_documentation_versions()
    context['current_version'] = config.release
    context['version_url'] = partial(_get_version_url, config)
    context['version_label'] = _get_version_label(config)

def _get_current_translation(config):
    language = config.language or ''
    return next(v for k, v in translations if k == language)

def _get_translation_url(config, code, pagename):
    base = '/locale/%s' % code if code else ''
    return _get_url(config, base, pagename)

def _get_documentation_versions():
    all_versions = _get_git_tags()
    return ['latest', *(v for v in all_versions if not v.startswith('0.7'))]

def _get_version_url(config, version_number, pagename):
    base = '/stable/%s' % version_number if version_number != 'latest' else ''
    return _get_url(config, base, pagename)

def _get_version_label(config):
    return '%s (%s)' % (config.release, _get_current_translation(config))

def _get_git_tags():
    repo_root = os.path.abspath(os.path.dirname(__file__))
    cmd = ['git' , 'tag', '--sort=-creatordate']
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE, cwd=repo_root)
    stdout, stderr = proc.communicate()
    if proc.returncode > 0:
        raise RuntimeError("%s failed with:\nstdout:\n%s\nstderr:\n%s\n"
                           % (cmd, stdout, stderr))
    return stdout.decode('utf8').splitlines()

def _get_url(config, base, pagename):
    return _add_content_prefix(config, '%s/%s.html' % (base, pagename))

def _add_content_prefix(config, url):
    prefix = ''
    if config.content_prefix:
        prefix = '/%s' % config.content_prefix
    return '%s%s' % (prefix, url)

class _VersionHistory(Table):

    headers = ["Qiskit Metapackage Version", "qiskit-terra", "qiskit-aer",
               "qiskit-ignis", "qiskit-ibmq-provider", "qiskit-aqua"]
    repo_root = os.path.abspath(os.path.dirname(__file__))

    def _get_setup_py(self, version):
        cmd = ['git', 'show', '%s:setup.py' % version]
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                cwd=self.repo_root)
        stdout, stderr = proc.communicate()
        if proc.returncode > 0:
            raise RuntimeError("%s failed with:\nstdout:\n%s\nstderr:\n%s\n"
                               % (cmd, stdout, stderr))
        return stdout.decode('utf8')

    def get_versions(self, tags):
        versions = {}
        for tag in tags:
            version = {}
            setup_py = self._get_setup_py(tag)
            for package in self.headers[1:] + ['qiskit_terra']:
                version_regex = re.compile(package + '[=|>]=(.*)\"')
                match = version_regex.search(setup_py)
                if match:
                    ver = match[1]
                    if '<' in match[1]:
                        ver = '>=' + ver
                    if package != 'qiskit_terra':
                        version[package] = ver
                    else:
                        version['qiskit-terra'] = ver
            if version:
                versions[tag] = version
        return versions

    def build_table(self, versions):
        table = nodes.table()
        table['classes'] += ['colwidths-auto']
        tgroup = nodes.tgroup(cols=len(self.headers))
        table += tgroup
        self.options['widths'] = [30, 15, 15, 15, 20, 15]
        tgroup.extend(
            nodes.colspec(colwidth=col_width, colname='c' + str(idx))
            for idx, col_width in enumerate(self.col_widths)
        )

        thead = nodes.thead()
        tgroup += thead

        row_node = nodes.row()
        thead += row_node
        row_node.extend(nodes.entry(h, nodes.paragraph(text=h))
                        for h in self.headers)

        tbody = nodes.tbody()
        tgroup += tbody

        rows = []
        for version in versions:
            row_node = nodes.row()
            entry = nodes.entry()
            entry += nodes.paragraph(text=version)
            row_node += entry
            for cell in self.headers[1:]:
                if cell in versions[version]:
                    entry = nodes.entry()
                    text = versions[version][cell]
                    entry += nodes.paragraph(text=text)
                else:
                    entry = nodes.entry()
                row_node += entry
            rows.append(row_node)
        tbody.extend(rows)
        return table

    def run(self):
        tags = _get_git_tags()
        versions = self.get_versions(tags)
        self.max_cols = len(self.headers)
        self.col_widths = self.get_column_widths(self.max_cols)
        table_node = self.build_table(versions)
        title, messages = self.make_title()
        if title:
            table_node.insert(0, title)
        return [table_node] + messages
