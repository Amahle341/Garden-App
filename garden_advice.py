
# # TODO: Examples of possible features to add:
# # - Add detailed comments explaining each block of code.
# # - Refactor the code into functions for better readability and modularity.
# # - Store advice in a dictionary for multiple plants and seasons.
# # - Recommend plants based on the entered season.


# Garden Advice App
# This program gives gardening tips
#  based on the selected season and plant type.
# It uses functions for modularity, a dictionary for advice storage,
# and provides plant recommendations for each season.

# Dictionary containing advice for each season and plant type
advice_data = {
    "spring": {
        "flower": "Prepare soil and plant new bulbs for colorful blooms.",
        "vegetable": "Start planting early crops like lettuce and peas.",
        "herb": "Plant herbs in pots for easy indoor care."
    },
    "summer": {
        "flower": "Water regularly and provide shade during hot days.",
        "vegetable": "Harvest ripe crops and check for pests.",
        "herb": "Trim herbs frequently to encourage new growth."
    },
    "autumn": {
        "flower": "Prune dead flowers and collect seeds for next season.",
        "vegetable": "Clear out harvested plants and enrich the soil.",
        "herb": "Dry herbs for storage and prepare them for cooler weather."
    },
    "winter": {
        "flower": "Protect flowers from frost with garden covers.",
        "vegetable": "Focus on soil care and plan next season’s crops.",
        "herb": "Move potted herbs indoors to keep them warm."
    }
}

# Dictionary recommending which plants are best for each season
plant_recommendations = {
    "spring": ["tulips", "peas", "mint"],
    "summer": ["roses", "tomatoes", "basil"],
    "autumn": ["marigolds", "carrots", "thyme"],
    "winter": ["pansies", "cabbage", "rosemary"]
}


def get_season():
    """Display a menu and return the chosen season."""
    print("\nSelect a season:")
    print("1. Spring")
    print("2. Summer")
    print("3. Autumn")
    print("4. Winter")
    choice = input("Enter the number of your choice: ")

    if choice == "1":
        return "spring"
    elif choice == "2":
        return "summer"
    elif choice == "3":
        return "autumn"
    elif choice == "4":
        return "winter"
    else:
        print("Invalid choice. Defaulting to 'summer'.")
        return "summer"


def get_plant_type():
    """Display a menu and return the chosen plant type."""
    print("\nSelect a plant type:")
    print("1. Flower")
    print("2. Vegetable")
    print("3. Herb")
    choice = input("Enter the number of your choice: ")

    if choice == "1":
        return "flower"
    elif choice == "2":
        return "vegetable"
    elif choice == "3":
        return "herb"
    else:
        print("Invalid choice. Defaulting to 'flower'.")
        return "flower"


def get_advice(season, plant_type):
    """Retrieve gardening advice from
      the dictionary based on the season and plant type."""
    # Get advice from dictionary, or a default message if not found
    season_data = advice_data.get(season, {})
    return season_data.get(
        plant_type, "No advice available for this selection.")


def recommend_plants(season):
    """Suggest suitable plants to grow based on the selected season."""
    plants = plant_recommendations.get(season, [])
    if plants:
        print("\nRecommended plants for", season.capitalize() + ":")
        for plant in plants:
            print("-", plant.capitalize())
    else:
        print("No plant recommendations available for this season.")


def main():
    """Main menu loop for the garden advice program."""
    print("Welcome to the Garden Advice App")

    while True:
        # Display main menu
        print("\nMenu:")
        print("1. Get gardening advice")
        print("2. Recommend plants for the season")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            season = get_season()
            plant_type = get_plant_type()
            print("\nGardening Advice:")
            print(get_advice(season, plant_type))
        elif choice == "2":
            season = get_season()
            recommend_plants(season)
        elif choice == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
