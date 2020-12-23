# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install py-extrap
#
# You can edit this file again by typing:
#
#     spack edit py-extrap
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class PyExtrap(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://github.com/extra-p/extrap"
    url      = "https://github.com/extra-p/extrap/archive/v4.0.1.zip"

    maintainers = ['sshudler']

    version('4.0.1', sha256='a8d2cbb839e68ef77edb4ceee7dac79e37149f2f11c8daa70364e1e6cfd6bf83')
    version('4.0.0', sha256='0cb107d5692cfeb50b8722b9cfbec62d870be56483d84e8f7588fac977e4162e')

    # FIXME: Add dependencies if required. Only add the python dependency
    # if you need specific versions. A generic python dependency is
    # added implicity by the PythonPackage class.

    depends_on('python@3.7:',   type=('build', 'run'))
    depends_on('py-setuptools', type='build')
    depends_on('py-numpy',      type=('build', 'run'))
    depends_on('py-matplotlib', type=('build', 'run'))
    depends_on('py-tqdm',       type=('build', 'run'))
    depends_on('py-pyside2',    type=('build', 'run'))
    depends_on('py-pycubexr',    type=('build', 'run'))


    # def build_args(self, spec, prefix):
    #     # FIXME: Add arguments other than --prefix
    #     # FIXME: If not needed delete this function
    #     args = []
    #     return args
