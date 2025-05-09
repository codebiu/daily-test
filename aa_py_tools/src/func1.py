def repeat(text, times=2):
    """
    重复输入文本的函数
    :param text: 要重复的文本
    :param times: 重复次数，默认为2
    :return: 重复后的文本
    """
    print(' '.join([text] * times))
    return text * times