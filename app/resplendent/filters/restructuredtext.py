"""Markdown filter."""
import codecs

import markdown

from pyspelling import filters


class MarkdownFilter(filters.Filter):
    """Spelling Python."""

    def get_default_config(self):
        """Get default configuration."""

        return {
            "markdown_extensions": []
        }

    def setup(self):
        """Setup."""

        extensions = []
        extension_configs = {}
        for item in self.config['markdown_extensions']:
            if isinstance(item, str):
                extensions.append(item)
            else:
                key, val = list(item.items())[0]
                extensions.append(key)
                if val is not None:
                    extension_configs[key] = val
        self.markdown = markdown.Markdown(
            extensions=extensions, extension_configs=extension_configs
        )

    def filter(self, source_file, encoding):  # noqa A001
        """Parse Markdown file."""

        with codecs.open(source_file, 'r', encoding=encoding) as fobj:
            text = fobj.read()
        return [filters.SourceText(
            self._filter(text), source_file, encoding, 'markdown'
        )]

    def _filter(self, text):
        """Filter markdown."""

        self.markdown.reset()
        return self.markdown.convert(text)

    def sfilter(self, source):
        """Filter."""

        return [filters.SourceText(
            self._filter(source.text), source.context, source.encoding,
            'markdown'
        )]


def get_plugin():
    """Return the filter."""

    return MarkdownFilter
