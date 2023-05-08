class ThreadParam:
  def __init__(self, thread, thread_id, user_id, intent, politeness, acceptance, explicit_words, highlight_words,
               engagement, emotion, trust):
    self.thread_id = thread_id
    self.user_id = user_id
    self.thread = thread
    self.intent = intent
    self.politeness = politeness
    self.acceptance = acceptance
    self.explicit_words = explicit_words
    self.highlight_words = highlight_words
    self.engagement = engagement
    self.emotion = emotion
    self.trust = trust
