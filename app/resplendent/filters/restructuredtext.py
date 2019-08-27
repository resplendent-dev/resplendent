"""reStructuredText filter."""
import codecs

import docutils.core
from pyspelling import filters


class ReStructuredTextFilter(filters.Filter):
    """Convert reStructuredText to HTML."""

    @staticmethod
    def get_default_config():
        """Get default configuration."""
        return {}

    def filter(self, source_file, encoding):  # noqa A001
        """Parse reStructuredText file."""

        with codecs.open(source_file, "r", encoding=encoding) as fobj:
            text = fobj.read()
        return [
            filters.SourceText(
                self._filter(text), source_file, encoding, "restructuredtext"
            )
        ]

    @staticmethod
    def _filter(text):
        """Filter reStructuredText"""
        result = docutils.core.publish_string(
            text,
            writer_name="html",
            settings_overrides={
                "input_encoding": "unicode",
                "output_encoding": "unicode",
                "report_level": "quiet",
            },
        )
        return result

    def sfilter(self, source):
        """Filter."""

        return [
            filters.SourceText(
                self._filter(source.text),
                source.context,
                source.encoding,
                "restructuredtext",
            )
        ]


def get_plugin():
    """Return the filter."""

    return ReStructuredTextFilter
