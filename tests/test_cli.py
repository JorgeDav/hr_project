from hr import cli
import pytest

@pytest.fixture()
def parser():
    return cli.create_parser()


def test_parser_fails_withouth_arguments(parser):
# With no arguments fails
    with pytest.raises(SystemExit):
        parser.parse_args([])

def test_parser_with_valid_path(parser):
#Parser will not exit if has a path
    args=parser.parse_args(['/some/path'])
    assert args.path=='/some/path'

def test_parser_with_export_flag(parser):
#export flag will change if its present
    args=parser.parse_args(['some/path','--export'])
    assert args.export==True

    args=parser.parse_args(['some/path'])
    assert args.export==False
