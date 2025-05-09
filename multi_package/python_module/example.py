"""
Python调用Rust模块示例
"""

import ctypes
import os

# 加载Rust编译的动态库
lib_path = os.path.join(os.path.dirname(__file__), "..", "rust_module", "target", "release")
lib = ctypes.CDLL(os.path.join(lib_path, "rust_module.dll"))

# 定义Rust函数的参数和返回类型
lib.add_numbers.argtypes = [ctypes.c_int, ctypes.c_int]
lib.add_numbers.restype = ctypes.c_int

# 调用Rust函数
result = lib.add_numbers(5, 7)
print(f"Rust add_numbers result: {result}")