# demo_tool_package

Python工具包示例

## 安装

```bash
pip install -e .
```
## 构建

```bash
pip install build twine
# 构建 wheel 包
python -m build
# cmd
python -m build && rm -rf *.egg-info
#  power shell
python -m build ;  Remove-Item -Recurse -Force *.egg-info ;pip install dist/aa_py_tools-0.1.0-py3-none-any.whl --force-reinstall

# 本地安装
pip install dist/aa_py_tools-0.1.0-py3-none-any.whl
# 上传 Python 包到 PyPI 
python -m twine upload dist/*
```

## 使用

### 命令行使用

```sh
aa_py_tools
aa_py_tools "Test " 4
# 输出: Test Test Test Test 
```


### 代码导入使用
```python
from demo_tool_package import repeat

result = repeat("Test ", 4)
print(result)  # 输出: Test Test Test Test 
```