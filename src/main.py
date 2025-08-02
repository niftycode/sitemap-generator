#!/usr/bin/env python3

"""
Main module for generating a sitemap.
This script initializes the sitemap creation process by fetching data from a specified URL
and creating a sitemap file.
Version: 1.0
Python 3.12+
Date created: July 31st, 2025
Date modified: August 2nd, 2025
"""

import logging
from logging.config import fileConfig

from src.argument_handler import ArgumentHandler
from src.sitemap import CreateSitemap

fileConfig("logging.ini")
logger = logging.getLogger()


def main() -> None:
    # Parse command-line arguments
    arg_handler = ArgumentHandler()
    args = arg_handler.parse_args()
    
    # Create sitemap using the provided URL and output filename
    create_sitemap = CreateSitemap(args.url, args.output)
    create_sitemap.fetch_data(args.url, 0)
    create_sitemap.create_file()
    
    logger.info(f"Sitemap created successfully at {args.output}")


if __name__ == "__main__":
    main()
