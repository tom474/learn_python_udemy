capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nested List in Dictionary
travel_log1 = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}

# Print Lille
print(travel_log1["France"][1])

# Nested List
nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])

# Nested dictionary in a dictionary
travel_log2 = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    },
}

# Print Stuttgart
print(travel_log2["Germany"]["cities_visited"][2])
