from src.helper.commands import help_, install, sanity_check
from tests.settings import DATABASE, DB_TYPE
from pytest import mark

class TestCommands:

    @mark.skip(reason="Need Chromer installed with version 94")
    def test_sanity_check_works(self):
        actual = sanity_check(DATABASE, DB_TYPE)
        expected = "Sanity check finished"
        assert actual == expected

    def test_install_creates_database(self):
        actual = install(DATABASE, DB_TYPE)
        expected = "Installation finished"
        assert actual == expected

    def test_help_is_opened(self):
        actual = help_()
        assert "--initdb" in actual
        assert "--help" in actual
        assert "--sanity-check"
