from torrentbotx.trackers.carpt import CarptTracker
from torrentbotx.trackers.dicmusic import DicMusicTracker
from torrentbotx.trackers.mteam import MTeamTracker
from torrentbotx.trackers.ptskit import PTSKitTracker

# Tracker 初始化
TRACKERS = {
    "mteam": MTeamTracker,
    "dicmusic": DicMusicTracker,
    "carpt": CarptTracker,
    "ptskit": PTSKitTracker,
}


def get_tracker_by_name(name: str):
    """
    根据站点名称获取对应的 Tracker 类。
    :param name: 站点名称，如 "mteam"、"dicmusic" 等。
    :return: 对应的 Tracker 类实例
    """
    tracker_class = TRACKERS.get(name.lower())
    if tracker_class:
        return tracker_class()
    else:
        raise ValueError(f"不支持的 Tracker : {name}")
