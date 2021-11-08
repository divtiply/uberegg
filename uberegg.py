import os
import subprocess
import sys
from distutils import log

from setuptools.command.bdist_egg import bdist_egg


class bdist_uberegg(bdist_egg):
    description = "create an uber-egg (egg with dependencies) distribution"
    user_options = bdist_egg.user_options + [
        (
            'requirements=',
            'r',
            'include packages from the given requirements file [default: requirements.txt]',
        ),
    ]

    def initialize_options(self):
        self.requirements = None
        super().initialize_options()

    def finalize_options(self):
        if self.requirements is None:
            self.requirements = 'requirements.txt'
        super().finalize_options()

    def run(self):
        if self.requirements and os.path.exists(self.requirements):
            log.info(
                'installing dependencies from %s to %s',
                self.requirements,
                self.bdist_dir,
            )
            self._install(self.requirements, self.bdist_dir)
        else:
            log.warn(
                '% file not found, falling back to standard egg',
                self.requirements,
            )
        super().run()

    @staticmethod
    def _install(requirements, target):
        return subprocess.check_call(
            [sys.executable, '-m', 'pip', 'install']
            + ['-U', '-t', target, '-r', requirements]
        )
