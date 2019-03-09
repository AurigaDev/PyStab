
class AnalysisProperties:
    self.name = None
    self.descpription = None
    self.short_hand = ' '
    self.is_explicit = False

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_description(self):
        return self.description
    
    def get_description(self, description):
        self.description = description

    def get_short_hand(self):
        return self.short_hand

    def set_short_hand(self, short_hand):
    
    def is_explicit(self):
        return self.is_explicit

    def set_explicit(self, is_explicit):
        self.is_explicit = is_explicit        