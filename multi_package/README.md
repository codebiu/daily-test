# 多语言调用项目

本项目包含Python和Rust模块，支持通过FFI/C接口实现多语言调用。

## 目录结构
- python_module/ - Python模块代码
- rust_module/ - Rust模块代码
- bindings/ - 跨语言接口定义
- docs/ - 文档

## 构建说明

```bash
# 安装Python依赖
pip install -r requirements.txt

# 构建Rust模块
cd rust_module
cargo build
```