import re

def to_snake_case(s: str) -> str:
    """将驼峰式命名转换为下划线命名"""
    s = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', s)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s).lower()

def to_camel_case(s: str) -> str:
    """将下划线命名转换为驼峰命名（小驼峰）"""
    parts = s.split('_')
    return parts[0] + ''.join(x.capitalize() for x in parts[1:])

def to_pascal_case(s: str) -> str:
    """将下划线命名转换为帕斯卡命名（大驼峰）"""
    return ''.join(x.capitalize() for x in s.split('_'))

def remove_whitespace(s: str) -> str:
    """去除字符串所有空白字符"""
    return ''.join(s.split())

def normalize_whitespace(s: str) -> str:
    """将多个空白字符压缩为一个空格"""
    return ' '.join(s.split())

def is_blank(s: str) -> bool:
    """判断字符串是否为空或全是空白"""
    return not s or s.strip() == ''
