class Answer:
    """A single test stimulus paired with the participant's response to it."""

    def __init__(self, answer_id, question, similarity=-1, answer=-1, audio=None):
        self.id = answer_id
        self.question = question      # stimulus identifier (serializable, e.g. the audio path)
        self.audio = audio            # pydub AudioSegment used for playback
        self.answer = answer
        self.similarity = similarity

    def set_id(self, answer_id):
        self.id = answer_id

    def get_id(self):
        return self.id

    def set_answer(self, answer):
        self.answer = answer

    def get_answer(self):
        return self.answer

    def set_similarity(self, similarity):
        self.similarity = similarity

    def get_similarity(self):
        return self.similarity

    def set_question(self, question):
        self.question = question

    def get_question(self):
        return self.question

    def set_audio(self, audio):
        self.audio = audio

    def get_audio(self):
        return self.audio

    def to_dict(self):
        """Convert the Answer to a dict row for the history record."""
        return {
            'question': self.question,
            'participants_ans': self.answer,
            'participants_evaluation': self.similarity,
        }
