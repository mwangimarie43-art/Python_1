from pathlib import Path


def test_smoke():
    assert True


def test_conda_environment_file_exists():
    repo_root = Path(__file__).resolve().parents[1]
    assert (repo_root / "environment.yml").is_file()
