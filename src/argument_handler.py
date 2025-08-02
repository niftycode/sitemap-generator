#!/usr/bin/env python3

"""
argument_handler.py - Handle command-line arguments for the sitemap generator
Version: 1.0
Python 3.12+
Date created: August 2nd, 2025
Date modified: -
"""

import argparse
import logging
from logging.config import fileConfig

fileConfig("logging.ini")
logger = logging.getLogger()


class ArgumentHandler:
    """Class to handle command-line arguments for the sitemap generator."""

    def __init__(self):
        """Initialize the ArgumentHandler with an ArgumentParser."""
        self.parser = argparse.ArgumentParser(
            description="Generate a sitemap.xml file for a website."
        )
        self._add_arguments()

    def _add_arguments(self):
        """Add arguments to the parser."""
        self.parser.add_argument(
            "-u",
            "--url",
            type=str,
            required=True,
            help="URL of the website for which to generate a sitemap",
        )
        self.parser.add_argument(
            "--output",
            type=str,
            default="sitemap.xml",
            help="Output filename for the sitemap (default: sitemap.xml)",
        )

    def parse_args(self):
        """Parse command-line arguments.

        Returns:
            argparse.Namespace: The parsed arguments
        """
        return self.parser.parse_args()
