def connected(relations, person_a, person_b):
    # Your solution here!
    pass

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
