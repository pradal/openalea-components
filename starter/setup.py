# standard imports
import sys
import os

from setuptools import setup, find_packages


# User defined variables used to facilitate the adaptation of the setup script: TO BE ADAPTED FOR YOUR PACKAGE


# Name and version of the 'distribution package'
# (This will determine the name of the egg, and of the installation directory of the package)
# (This name is also the one to use in other packages to declare a dependency to this package)
# (The version number is used by deploy to detect UPDATES)
name = 'OpenAlea.Starter'
version= '0.0.2a2' 

# Name of the 'root' python package 
# (the one shiped within your 'distribution package')
# (this name is the one use by the import command)
# (This is generally the name of the 'top package': Sub package living under this one will be automatically detected in this script)
# (namespace is used by deploy to make your module declared,imported and used as a submodule of a larger collection (eg openalea,alinea,vplants) 
namespace = 'openalea'
short_pkg_name = 'starter'

# Meta information 
# (used to construct egg infos)
description= 'Starter package for OpenAlea.' 
long_description= '''
The Starter package is a typical package example to help developper
to create their own package, compatible with OpenAlea standards.
It defines best practices for build, installation, coding rules,
and license information.
It contains code in C++, Python, as well as Boost.Python wrappers.
The package can be installed on various platform.
'''
author= 'Samuel Dufour-Kowalski, Christophe Pradal'
author_email= 'samuel.dufour@sophia.inria.fr, christophe.pradal@cirad.fr'
url= 'http://openalea.gforge.inria.fr'
license= 'Cecill-C' 

# dependencies to other eggs
# (This is used by deploy to automatically downloads eggs during the installation of your package)
# (allows 'one click' installation for windows user)
# (linux users generally want to void this behaviour and will use the dependance list of your documentation)
# (dependance to deploy is mandatory for runig this script)
setup_requires = ['openalea.deploy']
if("win32" in sys.platform):
    install_requires = ['PlantGL']
else:
    install_requires = []
# web sites where to find eggs
dependency_links = ['http://openalea.gforge.inria.fr/pi']


# Following variable is used only for non pure-python packages (like this one, which includes C++ libs)
# (could be removed for pure python packages)
# (The build prefix is the directory where you told scons to put all the includes, binaries and libs.)
build_prefix = "build-scons"



# Research of all packages under your root (do not edit) 
pkg_name = '%s.%s'%(namespace,short_pkg_name)
packages = [pkg_name]+['%s.%s'%(pkg_name,x) for x in find_packages(src_rep)]
# expeted key and value of your top level wralea file 
# (mandatory if you have visualea components)
wralea_key = short_pkg_name
wralea_path = pkg_name

# setup function call
#
setup(
    # Meta data (no edition needed if you correctly defined the variables above)
    name=name,
    version=version,
    description=description,
    long_description=long_description,
    author=author,
    author_email=author_email,
    url=url,
    license=license,
    keywords = '',	
    # package installation
    packages= packages,	
    package_dir= {pkg_name : src_rep},
    # Namespace packages creation by deploy
    namespace_packages = [namespace],
    create_namespaces = True,
    # tell setup not  tocreate a zip file but install the egg as a directory (recomended to be set to False)
    zip_safe= False,
    # Dependencies
    setup_requires = setup_requires,
    install_requires = install_requires,
    dependency_links = dependency_links,


    # optional stuff 
    # (to be used if you want other things than pure python package installation)
 
    # Code compilation (with scons)
    # Define what to execute with scons
    scons_scripts=['SConstruct'],
    # Tell deploy where to find libs, includes and bins generated by scons.
    lib_dirs = {'lib' : build_prefix+'/lib'), },
    inc_dirs = { 'include' : build_prefix+'/include') },
    #bin_dirs = { 'bin' : build_prefix+'/bin') },

    # Install data (for demos) which are not python file.
    # Extension have to be declared in package_data. 
    include_package_data = True,
    package_data = {'' : ['*.pyd', '*.so'],},

    # postinstall_scripts = ['',],

    # Declare scripts and wralea as entry_points (extensions) of your package 
    entry_points = { 
		    #'console_scripts': [
                     #       'fake_script = openalea.fakepackage.amodule:console_script', ],
                     # 'gui_scripts': [
                      #      'fake_gui = openalea.fakepackage.amodule:gui_script',],
		#	'wralea': ['%s = %s'%(wralea_key,wralea_path),
		#]
		},
    )


