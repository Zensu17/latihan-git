def list_benefits():
    return [
        "More organized code",
        "Easier to reuse code",
        "Improved readability",
        "Simplified debugging"
    ]

def build_sentence(benefit):
    return f"One of the benefits of functions is: {benefit}"

def name_the_benefits():
    benefits = list_benefits()
    for benefit in benefits:
        sentence = build_sentence(benefit)
        print(sentence)

name_the_benefits()