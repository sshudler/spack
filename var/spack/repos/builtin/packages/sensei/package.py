# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Sensei(CMakePackage):
    """SENSEI is a platform for scalable in-situ analysis and visualization.
    Its design motto is 'Write once, run everywhere', this means that once
    the application is instrumented with SENSEI it can use existing and 
    future analysis backends. Existing backends include: Paraview/Catalyst,
    Visit/Libsim, ADIOS, Python scripts, and so on."""

    homepage = "https://sensei-insitu.org"
    url      = "https://gitlab.kitware.com/sensei/sensei/-/archive/v2.1.1/sensei-v2.1.1.tar.gz"
    git      = "https://gitlab.kitware.com/sensei/sensei.git"

    version('master', branch='master')
    version('2.1.1', sha256='8a27ebf133fef00a59e4b29433762e6560bf20214072de7808836eb668bb5687')
    version('2.1.0', sha256='b7af21a25523cf6cd8934d797471b75ca32881166625d71f24b5c8b6d727ca99')
    version('2.0.0', sha256='df48eab035e1acdd8edf5159955c05306f9ca48117effacc4a6b77c3fb24f62b')
    version('1.1.0', sha256='e5a4ba691573ff6c7b0d4793665e218ee5868ebcc0198915d1f16a4b7b92a368')
    version('1.0.0', sha256='bdcb03c56b51f2795ec5a7e85a5abb01d473d192fac50f2a8bf2608cc3564ff8')

    variant('build_type', default='RelWithDebInfo', description='CMake build type', values=('Debug', 'Release', 'RelWithDebInfo', 'MinSizeRel'))
    variant('sencore', default=True, description='Enables the SENSEI core library')
    variant('catalyst', default=True, description='Build with ParaView-Catalyst support')
    variant('libsim', default=False, description='Build with VisIt-Libsim support')
    variant('vtkio', default=True, description='Enable adaptors to write to VTK XML format')
    variant('adios', default=False, description='Enable ADIOS adaptors and endpoints')
    variant('python', default=False, description='Enable Python bindings')
    variant('miniapps', default=True, description='Enable the parallel 3D and oscillators miniapps')

    depends_on("paraview@5.5:5.6", when="+catalyst")
    depends_on("visit", when="+libsim")
    depends_on("vtk", when="+libsim")
    depends_on("vtk", when="+adios ~libsim ~catalyst")
    depends_on("vtk", when="+sencore ~catalyst")
    depends_on("vtk", when="+python ~libsim ~catalyst")
    depends_on("adios", when="+adios")
    depends_on("python", when="+python")
    depends_on("py-numpy", when="+python")
    depends_on("py-mpi4py", when="+python")
    depends_on("swig", when="+python")

    # Can have either LibSim or Catalyst, but not both
    conflicts('+libsim', when='+catalyst')

    def cmake_args(self):
        spec = self.spec

        args = [
            '-DCMAKE_CXX_STANDARD=11',
            '-DCMAKE_C_STANDARD=11',
            '-DCMAKE_CXX_FLAGS=-fPIC -Wall -Wextra -O3 -mtune=generic',
            '-DCMAKE_C_FLAGS=-fPIC -Wall -Wextra -O3 -mtune=generic'
        ]

        sensei_switch = 'ON' if '+sencore' in spec else 'OFF'
        args.append('-DENABLE_SENSEI:BOOL={0}'.format(sensei_switch))

        vtk_dir_needed = True

        if '+catalyst' in spec:
            args.append('-DENABLE_CATALYST:BOOL=ON')
            args.append('-DENABLE_CATALYST_PYTHON:BOOL=ON')
            pview_prefix = spec['paraview'].prefix
            args.append('-DParaView_DIR:PATH={0}'.format(pview_prefix))
            vtk_dir_needed = False
        else:
            args.append('-DENABLE_CATALYST:BOOL=OFF')

        if '+libsim' in spec:
            args.append('-DENABLE_LIBSIM:BOOL=ON')
            args.append('-DVISIT_DIR:PATH={0}'.format(spec['visit'].prefix))
            args.append('-DVTK_DIR:PATH={0}'.format(spec['vtk'].prefix))
            vtk_dir_needed = False
        else:
            args.append('-DENABLE_LIBSIM:BOOL=OFF')

        vtkio_switch = 'ON' if '+vtkio' in spec else 'OFF'
        args.append('-DENABLE_VTK_IO:BOOL={0}'.format(vtkio_switch))
        python_switch = 'ON' if '+python' in spec else 'OFF'
        args.append('-DENABLE_PYTHON:BOOL={0}'.format(python_switch))

        if '+adios' in spec:
            args.append('-DENABLE_ADIOS:BOOL=ON')
            args.append('-DADIOS_DIR:PATH={0}'.format(spec['adios'].prefix))
        else:
            args.append('-DENABLE_ADIOS:BOOL=OFF')

        if vtk_dir_needed:
            args.append('-DVTK_DIR:PATH={0}'.format(spec['vtk'].prefix))

        if '+miniapps' in spec:
            args.append('-DENABLE_PARALLEL3D:BOOL=ON')
            args.append('-DENABLE_OSCILLATORS:BOOL=ON')
        else:
            args.append('-DENABLE_PARALLEL3D:BOOL=OFF')
            args.append('-DENABLE_OSCILLATORS:BOOL=OFF')

        return args
