class Genealogy:
    def __init__(self, persons):
        self.__persons = persons
        self.resolve_parents()
    

    def get_persons(self):
        return self.__persons


    def add_person(self, person):
        self.__persons.append(person)


    def find_person(self, id):
        found = None
        for person in self.get_persons():
            if person.id == id:
                found = person
                break
        return found
    

    def resolve_parents(self):
        for person in self.get_persons():
            parent1 = self.find_person(person.parent1_id)
            if person.parent1_id and not parent1:
                raise Exception(f"No matching person for '{person.id}' parent1 '{person.parent1}'")
            parent2 = self.find_person(person.parent2_id)
            if person.parent2_id and not parent2:
                raise Exception(f"No matching person for '{person.id}' parent2 '{person.parent2}'")
            person.set_resolved_parents(parent1, parent2)