// TODO: Examples of possible features to add:
// - Add detailed comments explaining each block of code.
// - Refactor the code into functions for better readability and modularity.
// - Store advice in an object for multiple plants and seasons.
// - Suggest plants that thrive in the given season.

// Garden Advice App
// This program gives gardening tips based on the selected season and plant type.
// It uses functions for modularity, an object for advice storage,
// and provides plant recommendations for each season.

// Object containing advice for each season and plant type
const adviceData = {
  spring: {
    flower: "Prepare soil and plant new bulbs for colorful blooms.",
    vegetable: "Start planting early crops like lettuce and peas.",
    herb: "Plant herbs in pots for easy indoor care."
  },
  summer: {
    flower: "Water regularly and provide shade during hot days.",
    vegetable: "Harvest ripe crops and check for pests.",
    herb: "Trim herbs frequently to encourage new growth."
  },
  autumn: {
    flower: "Prune dead flowers and collect seeds for next season.",
    vegetable: "Clear out harvested plants and enrich the soil.",
    herb: "Dry herbs for storage and prepare them for cooler weather."
  },
  winter: {
    flower: "Protect flowers from frost with garden covers.",
    vegetable: "Focus on soil care and plan next season’s crops.",
    herb: "Move potted herbs indoors to keep them warm."
  }
};

// Object recommending plants for each season
const plantRecommendations = {
  spring: ["tulips", "peas", "mint"],
  summer: ["roses", "tomatoes", "basil"],
  autumn: ["marigolds", "carrots", "thyme"],
  winter: ["pansies", "cabbage", "rosemary"]
};

// Function to get user input for season
function getSeason() {
  const season = prompt("Enter a season (spring, summer, autumn, winter):").toLowerCase();
  return ["spring", "summer", "autumn", "winter"].includes(season) ? season : "summer";
}

// Function to get user input for plant type
function getPlantType() {
  const type = prompt("Enter a plant type (flower, vegetable, herb):").toLowerCase();
  return ["flower", "vegetable", "herb"].includes(type) ? type : "flower";
}

// Function to get gardening advice based on season and plant type
function getAdvice(season, plantType) {
  if (adviceData[season] && adviceData[season][plantType]) {
    return adviceData[season][plantType];
  } else {
    return "No advice available for this selection.";
  }
}

// Function to recommend plants based on the selected season
function recommendPlants(season) {
  const plants = plantRecommendations[season];
  if (plants) {
    console.log(`Recommended plants for ${season}:`);
    plants.forEach(plant => console.log("- " + plant));
  } else {
    console.log("No plant recommendations available for this season.");
  }
}

// Main function to control the menu flow
function main() {
  while (true) {
    const choice = prompt(
      "Garden Advice Menu:\n1. Get gardening advice\n2. Recommend plants\n3. Exit\nEnter your choice:"
    );

    if (choice === "1") {
      const season = getSeason();
      const plantType = getPlantType();
      console.log("\nGardening Advice:");
      console.log(getAdvice(season, plantType));
    } else if (choice === "2") {
      const season = getSeason();
      recommendPlants(season);
    } else if (choice === "3") {
      console.log("Goodbye.");
      break;
    } else {
      console.log("Invalid choice. Please try again.");
    }
  }
}

// Run the program
main();
