"""dump out with processing filter."""
from __future__ import print_function

import codecs

from pyspelling import filters


class DumpOutFilter(filters.Filter):
    """Pass through logger."""

    @staticmethod
    def get_default_config():
        """Get default configuration."""
        return {
        }

    def filter(self, source_file, encoding):  # noqa A001
        """Parse text file."""

        with codecs.open(source_file, 'r', encoding=encoding) as fobj:
            text = fobj.read()
        return [filters.SourceText(
            self._filter(text), source_file, encoding, 'text'
        )]

    @staticmethod
    def _filter(text):
        """Filter text"""
        print(text)
        return text

    def sfilter(self, source):
        """Filter."""

        return [filters.SourceText(
            self._filter(source.text), source.context, source.encoding,
            'text'
        )]


def get_plugin():
    """Return the filter."""

    return DumpOutFilter
