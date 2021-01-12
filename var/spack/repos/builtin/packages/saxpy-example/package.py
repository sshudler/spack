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
import os


class SaxpyExample(CMakePackage, CudaPackage, ROCmPackage):
    """Simple SAXPY computation example in CUDA, Hip, and OneAPI."""

    homepage = "https://github.com/sshudler/saxpy-example"
    url      = "https://github.com/sshudler/saxpy-example"
    git      = "https://github.com/sshudler/saxpy-example.git"

    maintainers = ['sshudler']

    version('master', branch='master')

    # Variant for when we want to compile with OenAPI
    variant('sycl', default=False, description='Build with OneAPI')
    
    depends_on('cmake@3.13:', when='+cuda', type='build')
    depends_on('intel-oneapi-compilers', when='+sycl', type='build')

    def cmake_args(self):
        spec = self.spec
        options = []
        if '+cuda' in spec:
            options.extend([
                '-DENABLE_CUDA=ON',
                '-DCUDA_TOOLKIT_ROOT_DIR={0}'.format(spec['cuda'].prefix),
                '-DCMAKE_CUDA_HOST_COMPILER={0}'.format(env["SPACK_CXX"])])
            cuda_archs = spec.variants['cuda_arch'].value
            if 'none' not in cuda_archs:
                options.append('-DCUDA_NVCC_FLAGS={0}'.format(
                    ' '.join(self.cuda_flags(cuda_archs))))
        else:
            options.append('-DENABLE_CUDA=OFF')

        if '+rocm' in spec:
            options.extend([
                '-DENABLE_HIP=ON',
                '-DHIP_ROOT_DIR={0}'.format(spec['hip'].prefix)
            ])

            hip_archs = self.spec.variants['amdgpu_target'].value
            if 'none' not in hip_archs:
                archs_str = ",".join(hip_archs)
                options.append(
                    '-DHIP_HIPCC_FLAGS=--amdgpu-target={0} --rocm-device-lib-path={1}'
                    .format(archs_str, os.getenv('DEVICE_LIB_PATH'))
                )
        else:
            options.append('-DENABLE_HIP=OFF')

        if '+sycl' in spec:
            options.append('-DENABLE_ONEAPI=ON')
        else:
            options.append('-DENABLE_ONEAPI=OFF')

        return options

    def _test_target(self, target_exe):
        reason = "test installation of {0}".format(target_exe)
        self.run_test(target_exe, ['1'], ['Buffer size: 1048576', 'Max error: 0'],
                      status=0, installed=True, purpose=reason, skip_missing=False, work_dir='.')

    def test(self):
        """ Perform smoke test on the installation."""

        if '+cuda' in self.spec:
            self._test_target('saxpy-cuda')

        if '+rocm' in self.spec:
            self._test_target('saxpy-hip')
