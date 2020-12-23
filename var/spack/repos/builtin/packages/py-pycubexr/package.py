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
#     spack install py-pycubexr
#
# You can edit this file again by typing:
#
#     spack edit py-pycubexr
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class PyPycubexr(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/extra-p/pycubexr"
    url      = "https://github.com/extra-p/pycubexr/archive/v1.1.0.tar.gz"

    maintainers = ['sshudler']

    version('1.1.0', sha256='b052f8ea07f5eec5bdc93dfa63a671d189451c0b591d0768b0e312d8e536db8b')
    version('1.0.0', sha256='6ac9f1a9e597fee623d4b7c9e0e4f3c30dfa2469b84001b713727fbc4a40cce1')

    # FIXME: Add dependencies if required. Only add the python dependency
    # if you need specific versions. A generic python dependency is
    # added implicity by the PythonPackage class.
    # depends_on('python@2.X:2.Y,3.Z:', type=('build', 'run'))
    # depends_on('py-setuptools', type='build')
    # depends_on('py-foo',        type=('build', 'run'))

    # def build_args(self, spec, prefix):
    #     # FIXME: Add arguments other than --prefix
    #     # FIXME: If not needed delete this function
    #     args = []
    #     return args
