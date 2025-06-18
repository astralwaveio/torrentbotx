"""Utility helpers for common operations."""

from __future__ import annotations

import re


class Utility:
    """Collection of static helper functions."""

    @staticmethod
    def format_bytes(size: int) -> str:
        """Return human readable file size.

        Args:
            size: Size in bytes.

        Returns:
            Formatted string with appropriate unit.
        """
        if size < 0:
            raise ValueError("size must be non-negative")

        units = ["B", "KB", "MB", "GB", "TB", "PB"]
        value = float(size)
        for unit in units:
            if value < 1024 or unit == units[-1]:
                return f"{value:.1f} {unit}" if unit != "B" else f"{int(value)} {unit}"
            value /= 1024
        return f"{value:.1f} PB"

    @staticmethod
    def is_valid_torrent_hash(hash_str: str) -> bool:
        """Check whether given string looks like a torrent hash.

        Args:
            hash_str: Hash string to validate.

        Returns:
            ``True`` if string length is 16, 32 or 40 and consists of
            alphanumeric characters only, otherwise ``False``.
        """
        if not hash_str:
            return False
        return (
            len(hash_str) in {16, 32, 40}
            and re.fullmatch(r"[A-Za-z0-9]+", hash_str) is not None
        )
