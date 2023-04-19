import platform
import json

from ctypes import *
from importlib_resources import files

if platform.uname()[0] == "Windows":
    lib_name = "libili2gpkg.dll"
elif platform.uname()[0] == "Linux":
    lib_name = "libili2gpkg.so"
else:
    lib_name = "libili2gpkg.dylib"

class Ili2gpkg:

    @staticmethod
    def validate(args: list) -> bool:
        lib_path = files('ili2gpkg.lib_ext').joinpath(lib_name)
        dll = CDLL(str(lib_path))
        isolate = c_void_p()
        isolatethread = c_void_p()
        dll.graal_create_isolate(None, byref(isolate), byref(isolatethread))
        dll.ili2gpkg.restype = bool

        args_string = ';'.join(args)

        result = dll.ili2gpkg(isolatethread, c_char_p(bytes(args_string, "utf8")))
        return result