import time, requests

# Pattern Decorator

# def func_time_decorator(function):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         return_value = function(*args, **kwargs)
#         end = time.time()
#         print('Function took {} seconds'.format(end - start))
#         return return_value
#
#     return wrapper

# Pattern Facade

# class FileAdapterFacade:
#     """Facade for accessing files that hides system where file is located."""
#
#     def __init__(self, subsystem):
#         self._file_system = subsystem
#
#     def get_file(self, file_name):
#         return self._file_system.get(file_name)
#
#
# class LocalStorager:
#     """Access to local files."""
#
#     def get_file(self, file_name):
#         pass
#
#
# class CephStorager:
#     """
#     Access to remote files at ceph bucket
#     Class for implementing Ceph storage
#     """
#
#     def get_file(self, file_name):
#         connector = self.connect()
#         connector.set_s3_mode()
#         connector.turn_off_sll()
#         connector.establish()
#         file = connector.get_file(file_name)
#         return file

# Pattern Adapter

CORRELATION_ID = 'correlation_id'


class HttpRequests:
    def __init__(self, url):
        self.url = url

    def request(self, obj):
        try:
            if CORRELATION_ID not in obj.headers.keys():
                raise AttributeError
            else:
                response = requests.get(self.url, params=obj.params, headers=obj.headers)
        except AttributeError:
            print("not correlation_id in headers")


class OldClass:
    def __init__(self, headers, params):
        self.headers = headers
        self.params = params


class OldClassHttpRequestAdapter:
    def __init__(self, obj):
        self.obj = obj

    @property
    def headers(self):
        if CORRELATION_ID not in self.obj.headers.keys():
            self.obj.headers[CORRELATION_ID] = '1232-1112-3333'
        return self.obj.headers

    @property
    def params(self):
        return self.obj.params


http_requests = HttpRequests('htpps://github.com')
old_class_obj = OldClass({'test': '111'}, {'params1': 'value1'})
adapter_obj = OldClassHttpRequestAdapter(old_class_obj)
http_requests.request(old_class_obj)
http_requests.request(adapter_obj)
