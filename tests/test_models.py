from model.answer import Answer
from model.session import Session


def test_answer_to_dict_uses_question_identifier():
    a = Answer(answer_id=3, question="pa.wav", audio="<segment>", answer="ㄅ", similarity=4)
    d = a.to_dict()
    assert d == {
        "question": "pa.wav",
        "participants_ans": "ㄅ",
        "participants_evaluation": 4,
    }
    # Regression guard: the serialized 'question' must be the stimulus identifier,
    # never the internal row id (the old bug stored self.id here).
    assert d["question"] != a.id


def test_answer_audio_is_separate_from_question():
    a = Answer(answer_id=0, question="pi.wav", audio="AUDIO")
    assert a.get_audio() == "AUDIO"
    assert a.get_question() == "pi.wav"


def test_answer_defaults():
    a = Answer(answer_id=1, question="po.wav")
    assert a.get_answer() == -1
    assert a.get_similarity() == -1
    assert a.get_audio() is None


def test_session_set_get_reset():
    s = Session()
    assert s.get_user_info() is None
    s.set_user_info({"participantID": 7})
    assert s.get_user_info() == {"participantID": 7}
    s.set_user_info(None)  # reset on replay must clear prior participant data
    assert s.get_user_info() is None
