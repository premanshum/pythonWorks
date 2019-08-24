'''
List comprehension

    -   [ expr(item) for item in iterable if predicate (item)]
    -   p = [x*x for x in primeNumbers if (x>5)]

Set comprehension

    -   { expr(item) for item in iterable if predicate (item)}

Dictionary comprehension

    -   { key_expr:value_expr for item in iterable if predicate (item)}
    -   Cap_To_Country = { capital:country for country, capital in country_to_capital.items()}
    -   can use tuple unpacking like country and capital

'''