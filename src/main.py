#!/usr/bin/env python3

"""
Main module for generating a sitemap.
This script initializes the sitemap creation process by fetching data from a specified URL
and creating a sitemap file.
Version: 1.0
Python 3.12+
Date created: July 31st, 2025
Date modified: -
"""

import logging
from logging.config import fileConfig

from src.sitemap import CreateSitemap

fileConfig("logging.ini")
logger = logging.getLogger()


def main() -> None:
    create_sitemap = CreateSitemap("https://bodo-schoenfeld.eu", "sitemap.xml")
    create_sitemap.fetch_data("https://bodo-schoenfeld.eu", 0)
    create_sitemap.create_file()


if __name__ == "__main__":
    main()
