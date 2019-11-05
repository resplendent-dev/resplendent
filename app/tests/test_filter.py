"""
Test text plugin.
"""

from spellingtest.check import PluginTestCase


class TestResplendentFilter(PluginTestCase):
    """Check processing reStructuredText."""

    def setup_fs(self):
        """Setup files."""

        good_words = ["yes", "word"]
        self.bad_words1 = ["zxq", "helo", "begn"]
        self.mktemp("test1.rst", "\n".join(self.bad_words1 + good_words), "utf-8")

        config = self.dedent(
            """
            matrix:
            - name: name
              group: group1
              default_encoding: utf-8
              expect_match: false
              sources:
              - '{temp}/**/test1.rst'
              aspell:
                lang: en
              hunspell:
                d: en_AU
              pipeline:
              - resplendent.filters.restructuredtext:
              - pyspelling.filters.html:
                  comments: false
                  attributes:
                  - title
                  - alt
                  ignores:
                  - code
                  - pre
              - pyspelling.filters.url:
            """
        ).format(temp=self.tempdir)
        self.mktemp(".source.yml", config, "utf-8")

    def test_all(self):
        """Test all."""

        self.assert_spellcheck(".source.yml", self.bad_words1)
