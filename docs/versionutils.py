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
import tempfile
from functools import partial

from docutils import nodes
from docutils.parsers.rst.directives.tables import Table
from docutils.parsers.rst import Directive, directives
from sphinx.util import logging


logger = logging.getLogger(__name__)

translations_list = [
    ('en', 'English'),
    ('bn_BN', 'Bengali'),
    ('fr_FR', 'French'),
    ('de_DE', 'German'),
    ('ja_JP', 'Japanese'),
    ('ko_KR', 'Korean'),
    ('pt_UN', 'Portuguese'),
    ('es_UN', 'Spanish'),
    ('ta_IN', 'Tamil'),
]

default_language = 'en'


def setup(app):
    app.connect('config-inited', _extend_html_context)
    app.add_config_value('content_prefix', '', '')
    app.add_config_value('translations', True, 'html')
    app.add_directive('version-history', _VersionHistory)


def _extend_html_context(app, config):
    context = config.html_context
    context['translations'] = config.translations
    context['translations_list'] = translations_list
    context['version_list'] = _get_version_list()
    context['current_translation'] = _get_current_translation(config) or config.language
    context['translation_url'] = partial(_get_translation_url, config)
    context['version_label'] = _get_version_label(config)
    context['language_label'] = _get_language_label(config)


def _get_current_translation(config):
    language = config.language or default_language
    try:
        found = next(v for k, v in translations_list if k == language)
    except StopIteration:
        found = None
    return found


def _get_translation_url(config, code, pagename):
    base = '/locale/%s' % code if code and code != default_language else ''
    return _get_url(config, base, pagename)


def _get_version_label(config):
    proc = subprocess.run(
        ['git', 'describe', '--abbrev=0', '--tags', 'HEAD'],
        encoding='utf8', capture_output=True)
    return proc.stdout

def _get_language_label(config):
    return '%s' % (_get_current_translation(config) or config.language,)



def _get_version_list():
    start_version = (0, 24, 0)
    proc = subprocess.run(['git', 'describe', '--abbrev=0'],
                          capture_output=True)
    proc.check_returncode()
    current_version = proc.stdout.decode('utf8')
    current_version_info = current_version.split('.')
    if current_version_info[0] == '0':
        version_list = [
            '0.%s' % x for x in range(start_version[1],
                                      int(current_version_info[1]) + 1)]
    else:
        #TODO: When 1.0.0 add code to handle 0.x version list
        version_list = []
        pass
    # Prepend version 0.19 which was built and uploaded manually:
    version_list.insert(0, '0.19')
    return version_list


def _get_url(config, base, pagename):
    return _add_content_prefix(config, '%s/%s.html' % (base, pagename))


def _add_content_prefix(config, url):
    prefix = ''
    if config.content_prefix:
        prefix = '/%s' % config.content_prefix
    return '%s%s' % (prefix, url)


class _VersionHistory(Table):

    headers = ["Qiskit Metapackage Version", "qiskit-terra", "qiskit-aer",
               "qiskit-ignis", "qiskit-ibmq-provider", "qiskit-aqua",
               "Release Date"]
    repo_root = os.path.abspath(os.path.dirname(__file__))

    def _get_setup_py(self, version, git_dir):
        cmd = ['git', 'show', '%s:setup.py' % version]
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                cwd=git_dir)
        stdout, stderr = proc.communicate()
        if proc.returncode > 0:
            logger.warn("%s failed with:\nstdout:\n%s\nstderr:\n%s\n"
                        % (cmd, stdout, stderr))
            return ''
        return stdout.decode('utf8')

    def _get_date(self, version, git_dir):
        cmd = ['git', 'log', '--format=%ai', str(version), '-1']
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                cwd=git_dir)
        stdout, stderr = proc.communicate()
        if proc.returncode > 0:
            logger.warn("%s failed with:\nstdout:\n%s\nstderr:\n%s\n"
                        % (cmd, stdout, stderr))
            return ''
        return stdout.decode('utf8').split(' ')[0]

    def get_versions(self, tags, git_dir):
        versions = {}
        for tag in tags:
            version = {}
            setup_py = self._get_setup_py(tag, git_dir)
            version['Release Date'] = self._get_date(tag, git_dir)
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
        with tempfile.TemporaryDirectory() as tmp_dir:
            tags, git_dir = _get_qiskit_metapackage_git_tags(tmp_dir)
            versions = self.get_versions(tags, git_dir)
        self.max_cols = len(self.headers)
        self.col_widths = self.get_column_widths(self.max_cols)
        table_node = self.build_table(versions)
        title, messages = self.make_title()
        if title:
            table_node.insert(0, title)
        return [table_node] + messages


def _get_qiskit_metapackage_git_tags(tmp_dir):
    cmd = ['git', 'clone', 'https://github.com/Qiskit/qiskit.git']
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE, cwd=tmp_dir)
    stdout, stderr = proc.communicate()
    if proc.returncode > 0:
        logger.warn("%s failed with:\nstdout:\n%s\nstderr:\n%s\n"
                    % (cmd, stdout, stderr))
        return []
    else:

        return _get_git_tags(os.path.join(tmp_dir, 'qiskit'))


def _get_git_tags(git_dir):
    cmd = ['git', 'tag', '--sort=-creatordate']
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE, cwd=git_dir)
    stdout, stderr = proc.communicate()
    if proc.returncode > 0:
        logger.warn("%s failed with:\nstdout:\n%s\nstderr:\n%s\n"
                    % (cmd, stdout, stderr))
        return []

    return stdout.decode('utf8').splitlines(), git_dir
