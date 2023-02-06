import random

generated_names = []


def generate_name():
    # choose 3 random numbers to make up the name
    name = str(random.randint(10, 99)) + 'M'
    # check if the generated name is unique
    if name in generated_names:
        return generate_name()
    # add the generated name to the list of generated names
    generated_names.append(name)
    return name


# generate 10 unique names
for i in range(10):
    print(generate_name())
