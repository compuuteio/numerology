# Minimal interpretations for old API compatibility
# This is a placeholder to make the old Pythagorean class work


class Interpretations:
    def __init__(self, key_figures=None):
        self.key_figures = key_figures or {}
        self._meanings = {}

    @property
    def meanings(self):
        # Return empty interpretations for now - this maintains compatibility
        # without breaking the old API
        return self._meanings
