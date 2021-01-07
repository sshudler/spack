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
#     spack install saxpy-example
#
# You can edit this file again by typing:
#
#     spack edit saxpy-example
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class SaxpyExample(CMakePackage, CudaPackage):
    """Simple SAXPY computation example in CUDA, Hip, and OneAPI."""

    homepage = "https://github.com/sshudler/saxpy-example"
    url      = "https://github.com/sshudler/saxpy-example"
    git      = "https://github.com/sshudler/saxpy-example.git"

    maintainers = ['sshudler']

    version('master', branch='master')

    variant("cuda", default=True, description="Build with Cuda support")

    depends_on('cuda@10.1.0:', when='+cuda')

    # conflicts("+hip", when="+cuda")

    def cmake_args(self):
        spec = self.spec
        options = []
        if '+cuda' in spec:
            options.append('-DENABLE_CUDA=ON')
            # options.append("-DCMAKE_CUDA_HOST_COMPILER={0}".format(
            #                env["SPACK_CXX"]))
            cuda_arch = spec.variants['cuda_arch'].value
            if cuda_arch[0] != 'none':
                options.append('-DCUDA_FLAGS=-arch=sm_{0}'.format(cuda_arch[0]))
        else:
            options.append('-DENABLE_CUDA=OFF')

        return options
