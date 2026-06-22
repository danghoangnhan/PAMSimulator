import pandas as pd

from storage.localStorage import CsvHandler, JsonHandler, DataHandaler
from config.constant import USER_COLUMNS, HISTORY_COLUMNS


def test_csvhandler_append_read_truncate_roundtrip(tmp_path):
    csv = tmp_path / "history.csv"
    pd.DataFrame(columns=HISTORY_COLUMNS).to_csv(csv, index=False)
    handler = CsvHandler(path=str(csv))

    handler.append_data(pd.DataFrame([
        {"question": "pa.wav", "participants_ans": "ㄅ",
         "participants_evaluation": 4, "participate_number": 1},
    ]))
    df = handler.readData()
    assert len(df) == 1
    assert df.iloc[0]["question"] == "pa.wav"

    handler.truncate()
    assert handler.readData().empty
    assert list(handler.readData().columns) == HISTORY_COLUMNS


def test_jsonhandler_read_write_missing(tmp_path):
    path = tmp_path / "default.json"
    handler = JsonHandler(path=str(path))
    assert handler.read_data() is None  # missing file returns None, not a crash
    handler.write_data({"selected_similarity": 5, "selected_keyboard_layout": "bopomofo.csv"})
    assert handler.read_data()["selected_similarity"] == 5


def test_ensure_seed_files_creates_headers(tmp_path, monkeypatch):
    user = tmp_path / "user.csv"
    history = tmp_path / "history.csv"
    import storage.localStorage as ls
    monkeypatch.setattr(ls, "user_dir", str(user))
    monkeypatch.setattr(ls, "history_dir", str(history))

    DataHandaler._ensure_seed_files()

    assert user.exists() and history.exists()
    assert list(pd.read_csv(user).columns) == USER_COLUMNS
    assert list(pd.read_csv(history).columns) == HISTORY_COLUMNS
