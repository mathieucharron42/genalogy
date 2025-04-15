import re 

class Person:
    def __init__(self, id, name, parent1_id, parent2_id, birthdate):
        self.id = id
        self.name = name
        self.parent1_id = parent1_id
        self.parent1 = None
        self.parent2_id = parent2_id
        self.parent2 = None
        self.birthdate = birthdate
    
    def get_resolved_parents(self):
        parents = []
        parents.append(self.parent1)
        parents.append(self.parent2)
        return parents

    def set_resolved_parents(self, parent1, parent2):
        self.parent1 = parent1
        self.parent2 = parent2

    def get_display(self):
        if self.birthdate:
            return f"{self.get_short_name()} {self.birthdate}"
        else:
            return self.get_short_name()
    
    def get_short_name(self):
        separator = ' '
        tokens = self.name.split(separator)

        optional_pattern = re.compile("\[.*\]")
        dit_pattern = re.compile("dit")

        filtered_tokens = []

        for i in range(0, len(tokens)):
            token = tokens[i]
            if optional_pattern.match(token):
                continue
            elif dit_pattern.match(token):
                ++i
                continue
            else:
                filtered_tokens.append(token)
        
        return separator.join(filtered_tokens)