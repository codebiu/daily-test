# demo_tool_package/cli.py
import argparse
from . import repeat  # 导入你的函数


def main():
    # 主解析器
    parser = argparse.ArgumentParser(
        description="Demo Tool Package CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""示例用法:
                py_tools repeat "Hello" --times 3   # 重复输出3次Hello
                py_tools repeat "Test"              # 默认重复输出2次Test
                """,
    )

    # 子命令解析器
    subparsers = parser.add_subparsers(
        dest="command",
        title="可用命令",
        description="以下是支持的子命令",
        required=True,
        metavar="{repeat}",  # 在帮助中显示子命令占位符
    )

    # repeat 子命令
    repeat_parser = subparsers.add_parser(
        "repeat",
        help="重复输出字符串",
        description="重复输出指定文本多次",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    repeat_parser.add_argument("text", help="要重复的文本")
    repeat_parser.add_argument(
        "--times", "-t", type=int, default=2, help="重复次数 (默认: %(default)s)"
    )

    # 添加示例到子命令帮助
    repeat_parser.epilog = """示例:
                            py_tools repeat "Hello" -t 3   # 重复3次
                            py_tools repeat "World"        # 默认重复2次
                            """

    args = parser.parse_args()

    if args.command == "repeat":
        repeat(args.text, args.times)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
