## uv包管理
<!-- https://zhuanlan.zhihu.com/p/1888904532131575259 -->
```sh
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
$env:Path = "C:\Users\YanFaBu\.local\bin;$env:Path"   (powershell)
```
## 项目初始化
```sh
uv init a_package_template  # 初始化项目
cd a_package_template
# 可以删除.python-version


uv add 'requests==2.31.0' # 增加依赖
uv lock --upgrade-package requests # 更新项目依赖
uv remove requests # 删除项目依赖
```