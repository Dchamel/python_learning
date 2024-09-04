# sys
# System module
# import sys
#
# # Manage input parameters
# sys.argv
#
# # Path to python
# sys.executable
#
# # Program quit
# sys.exit()
#
# # List of paths where modules
# print(sys.path)
#
# # About OS
# sys.platform

# ---------

# os
# Work with files by OS module
# import os

# # current dir
# print(os.getcwd())
#
# # create ampty folder
# if not os.path.isdir(f'{os.getcwd()}/123'):
#     os.mkdir(f'{os.getcwd()}/123')
#
# # make some folders recursive
# os.makedirs(f'{os.getcwd()}/123/234/345', exist_ok=True)
#
# # and other funcs
# os.rename('1.txt', 'renamed-1.txt')
# os.listdir(f'{os.getcwd()}/123')

# # print all folders recursively
# for dirpath, dirnames, filenames in os.walk(os.getcwd()):
#     for dirname in dirnames:
#         print("The directory is ", dirname)
#     for filename in filenames:
#         print("The filename is ", filename)

# # del folder, folders
# os.rmdir(f'{os.getcwd()}/123')
# os.removedirs(f'{os.getcwd()}/123/')
# os.remove(f'{os.getcwd()}/123/1.txt')

# print(os.stat('libs_for_interactions_with_os.py'))

# ---------

# # for gettin some input parameters and etc... like sys
# import argparse
#
# parser = argparse.ArgumentParser('libs_for_interactions_with_os.py')
# parser.add_argument('service')
# args = parser.parse_args()
# result = args.service
# ...
# ...
# # google about this module if neded

# ---------

# # io
# # for work with input/output
#
# import io

# ---------

# glob
# finds all paths according to Unix shell rules

# import glob
#
# print(glob.glob('*.py'))

# ---------

# # shutil
#
# # module for operations with files and file collections
#
# import shutil
#
# # shutil.copyfile(from, to)
# # shutil.copytree(from, to)

# ---------

# subprocess
# launch new processes
# module for replace old modules os.system and os.spawn
# read more in google/yandex if needed

# ---------

# resource
# for measure sys resources using by prog

# import resource
# read more in google/yandex if needed
