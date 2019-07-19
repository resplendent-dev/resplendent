"""reStructuedText filter."""
import codecs

import docutils.core
from pyspelling import filters


class ReStructuedTextFilter(filters.Filter):
    """Convert reStructuedText to HTML."""

    @staticmethod
    def get_default_config():
        """Get default configuration."""
        return {
        }

    def filter(self, source_file, encoding):  # noqa A001
        """Parse reStructuedText file."""

        with codecs.open(source_file, 'r', encoding=encoding) as fobj:
            text = fobj.read()
        return [filters.SourceText(
            self._filter(text), source_file, encoding, 'restructuedtext'
        )]

    @staticmethod
    def _filter(text):
        """Filter reStructuedText"""
        return docutils.core.publish_string(text, writer_name='html')

    def sfilter(self, source):
        """Filter."""

        return [filters.SourceText(
            self._filter(source.text), source.context, source.encoding,
            'restructuedtext'
        )]


def get_plugin():
    """Return the filter."""

    return ReStructuedTextFilter
