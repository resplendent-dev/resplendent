"""
Test modules for resplendent.__main__
"""

from resplendent.__main__ import main


def test_main():
    """
    GIVEN the resplendent.__main__
    module entry point WHEN calling main THEN the call executes successfully
    with a result of `None`
    """
    # Setup
    # Exercise
    result = main()  # pylint: disable=assignment-from-no-return
    # Verify
    assert result is None  # nosec
