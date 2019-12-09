def sandwich(*toppings):
    """Describe toppings on a sandwich"""
    print('Here are what on your sandwich.')
    for topping in toppings:
        print(f'\t-{topping}')


sandwich('tuna')
sandwich('chicken', 'tomato')
sandwich('beef', 'cucumber', 'cabbage')
