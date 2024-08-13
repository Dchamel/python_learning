import time


# def func_time_decorator(function):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         return_value = function(*args, **kwargs)
#         end = time.time()
#         print('Function took {} seconds'.format(end - start))
#         return return_value
#
#     return wrapper

class FileAdapterFacade:
    """Facade for accessing files that hides system where file is located."""

    def __init__(self, subsystem):
        self._file_system = subsystem

    def get_file(self, file_name):
        return self._file_system.get(file_name)


class LocalStorager:
    """Access to local files."""

    def get_file(self, file_name):
        pass


class CephStorager:
    """
    Access to remote files at ceph bucket
    Class for implementing Ceph storage
    """

    def get_file(self, file_name):
        connector = self.connect()
        connector.set_s3_mode()
        connector.turn_off_sll()
        connector.establish()
        file = connector.get_file(file_name)
        return file
