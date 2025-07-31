#!/usr/bin/env python3

"""
sitemap.py - Create a sitemap from a website
Version: 1.0
Python 3.12+
Date created: July 31st, 2025
Date modified: -
"""

import logging
import urllib
import xml.etree.ElementTree as ET
from logging.config import fileConfig
from urllib.parse import urlparse

from bs4 import BeautifulSoup

import requests


fileConfig("logging.ini")
logger = logging.getLogger()


class CreateSitemap:
    def __init__(self, sitemap_url, filename):
        self.sitemap_url = sitemap_url
        self.filename = filename
        self.urls = {}
        self.hostname = urlparse(self.sitemap_url).hostname

    def fetch_data(self, url, level):
        print("Level: " + str(level) + "/ Explore " + url)
        page = requests.get(url)

        if page.status_code == 200:
            url = urllib.parse.urldefrag(url)[0]

            if url not in self.urls:
                self.urls[url] = level

                soup = BeautifulSoup(page.content, "html.parser")

                for link in soup.findAll("a"):  # type: ignore

                    try:

                        href = link.get("href")
                        result = urlparse(href)
                        new_url = None

                        if result.hostname is None and href is not None:
                            new_url = (
                                self.sitemap_url
                                + ("/", "")[href.startswith("/")]
                                + href
                            )
                        elif result.hostname == self.hostname:
                            new_url = href

                        if new_url is not None:
                            self.fetch_data(new_url, level + 1)

                    except TypeError:
                        print("Error for link:" + link.get("href"))

            else:
                if self.urls[url] > level:
                    self.urls[url] = level

        else:
            print(url + " unreachable")

    def create_file(self):
        urls_by_level = {}
        maxlevel = 0

        for key, value in self.urls.items():
            if value > maxlevel:
                maxlevel = value

            listurls = None

            if value not in urls_by_level:
                listurls = []
            else:
                listurls = urls_by_level[value]

            if listurls is not None:
                listurls.append(key)
                urls_by_level[value] = listurls

        step = 1 / (maxlevel * 2)

        rootstr = "<urlset></urlset>"
        root = ET.fromstring(rootstr)
        root.attrib = {"xmlns": "https://www.sitemaps.org/schemas/sitemap/0.9"}

        for key, value in urls_by_level.items():
            priority = round(1 - step * key, 2)

            if priority < 0:
                print("Step = " + str(step) + " Key = " + str(key))

            for item in value:
                url = ET.SubElement(root, "url")
                ET.SubElement(url, "loc").text = item
                ET.SubElement(url, "priority").text = str(priority)

        tree = ET.ElementTree(root)
        ET.indent(tree, "  ")
        tree.write(self.filename, encoding="utf-8", xml_declaration=True)
