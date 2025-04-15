def make_sandwich(*items):
    """Summarizes the sandwich we are about to make."""
    print(f"\nMaking a sandwich with the following items:")
    for item in items:
        print(f"- {item}")

make_sandwich('bacon', 'lettuce', 'tomato')
make_sandwich('peanut butter', 'jelly')
make_sandwich('mayonaise')

