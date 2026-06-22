import os

from config import dir as config_dir


def test_paths_anchored_to_module_not_cwd(monkeypatch, tmp_path):
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(config_dir.__file__)))
    assert config_dir.static_dir == os.path.join(repo_root, "static")
    assert config_dir.exam_dir == os.path.join(repo_root, "static", "csv", "exam.csv")

    # Resolved from the module location at import time, so changing the working
    # directory must not change where assets are looked up (the old os.getcwd() bug).
    monkeypatch.chdir(tmp_path)
    assert os.path.isabs(config_dir.audio_dir)
    assert os.path.isdir(config_dir.audio_dir)
