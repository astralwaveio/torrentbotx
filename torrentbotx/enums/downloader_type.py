from enum import Enum


class DownloaderType(str, Enum):
    ARIA2 = "aria2"
    QBITTORRENT = "qbittorrent"
    TRANSMISSION = "transmission"

    @classmethod
    def from_name(cls, name: str) -> "DownloaderType":
        name = name.lower()
        for member in cls:
            if member.value == name:
                return member
        raise ValueError(f"无效的下载器类型: {name}")
