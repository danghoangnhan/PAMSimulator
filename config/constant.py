color_dict = {
    "white": (255, 255, 255),
    "green": (0, 255, 0),
    "blue": (0, 0, 128),
    "red": (255, 0, 0),
    "yellow": (255, 255, 0),
    "orange": (255, 165, 0),
    "purple": (128, 0, 128),
    "pink": (255, 182, 193),
    "brown": (165, 42, 42),
    "gray": (128, 128, 128),
    "black": (0, 0, 0),
    "cyan": (0, 255, 255),
    "magenta": (255, 0, 255),
    "lime": (0, 255, 0),
    "teal": (0, 128, 128),
    "navy": (0, 0, 128),
    # Add more colors as needed
}


pofomopo_consonants = ["ㄅ", "ㄆ", "ㄇ", "ㄈ", "ㄉ", "ㄊ", "ㄋ", "ㄌ", "ㄍ", "ㄎ", "ㄏ", "ㄐ", "ㄑ", "ㄒ", "ㄓ", "ㄔ", "ㄕ", "ㄖ", "ㄗ", "ㄘ", "ㄙ"]

similarity_list = [1, 2, 3, 4, 5]

# Canonical schemas for the participant-data CSV files. Kept here so the storage
# seeder and the test-submission writer agree on column names.
USER_COLUMNS = [
    "中文姓名",
    "英文姓名",
    "性別",
    "出生年",
    "教育程度",
    "母語",
    "跟家人常說語言",
    "跟朋友常說語言",
    "participantID",
]

HISTORY_COLUMNS = [
    "question",
    "participants_ans",
    "participants_evaluation",
    "participate_number",
]
