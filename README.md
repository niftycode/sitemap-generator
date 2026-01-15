# Sitemap Generator

A Python tool that automatically generates a sitemap.xml file for a website by crawling all accessible links. The tool recursively visits all pages on the website, extracts links, and creates a properly formatted sitemap.xml file that follows the [Sitemaps XML format](https://www.sitemaps.org/protocol.html).

## Requirements

- Python 3.12+
- Dependencies listed in `requirements.txt`

## Installation

1. Clone this repository
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

The sitemap generator accepts the following arguments:

| Argument | Short | Description | Required |
|----------|-------|-------------|----------|
| `--url` | `-u` | URL of the website for which to generate a sitemap | Yes |
| `--output` | | Output filename for the sitemap (default: sitemap.xml) | No |

By default, the sitemap.xml file is saved to your Desktop. If you provide a full path in the `--output` argument, the file will be saved to that location instead.

### Examples

Generate a sitemap for example.com and save it with the default name (sitemap.xml) on your Desktop:

```bash
python src/main.py --url https://example.com
```

Generate a sitemap for example.com and save it with a custom name:

```bash
python src/main.py --url https://example.com --output my_sitemap.xml
```

Generate a sitemap for example.com and save it to a specific location:

```bash
python src/main.py --url https://example.com --output /path/to/save/sitemap.xml
```
