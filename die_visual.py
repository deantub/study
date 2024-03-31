from die import Die

# Створити D6
die = Die()

# Зробити декілька кидків та зберегти результати у список
results = []
for roll_num in range(100):
    result = die.roll()
    results.append(result)

print(results)