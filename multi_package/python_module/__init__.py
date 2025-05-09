"""
Python模块入口文件

通过FFI/C接口调用Rust模块功能
"""

# 导入必要的模块
import os
import sys

# 添加Rust模块路径
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "rust_module", "target", "release"))