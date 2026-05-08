def connected(relations, person_a, person_b):
    visited = set()

    def dfs(person):

        if person == person_b:
            return True
        
        if person in visited:
            return False
        
        visited.add(person)

        for man in relations.get(person, set()):

            if dfs(man):
                return True
        
        return False
    
    return dfs(person_a)



# All tests use the same dictionary
relations = {
    "Sebastian": {"Kevin", "Lewis", "Fernando"},
    "Max": {"Fernando"},
    "Lewis": {"Sebastian"},
    "Yuki": {"Pierre"},
    "Pierre": {"Yuki"},
    "Fernando": {"Sebastian", "Max"},
    "Carlos": {"Charles", "Lando"},
    "Lando": {"Carlos"},
    "Charles": {"Carlos"},
    "Kevin": {"Sebastian"}
}
assert connected(relations, "Max", "Lewis") == True
assert connected(relations, "Lewis", "Yuki") == False
assert connected(relations, "Yuki", "Pierre") == True
assert connected(relations, "Lando", "Carlos") == True
assert connected(relations, "Kevin", "Carlos") == False
assert connected(relations, "Kevin", "Fernando") == True

print("All tests passed!")
print("Discuss time & space complexity if time remains.")
