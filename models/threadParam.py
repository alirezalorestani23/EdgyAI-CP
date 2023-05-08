class ThreadParam:
  def __init__(self, thread, thread_id, user_id, thread_intent, politeness, acceptance, explicit_words, highlight_words,
               engagement, emotion, trust):
    self.thread = thread
    self.thread_id = thread_id
    self.user_id = user_id
    self.thread_intent = thread_intent
    self.politeness = politeness
    self.acceptance = acceptance
    self.explicit_words = explicit_words
    self.highlight_words = highlight_words
    self.engagement = engagement
    self.emotion = emotion
    self.trust = trust