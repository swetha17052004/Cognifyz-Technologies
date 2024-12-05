{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "a9db081a-efed-4c59-a333-9bf968532bfb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   Restaurant ID         Restaurant Name  Country Code              City  \\\n",
      "0        6317637        Le Petit Souffle           162       Makati City   \n",
      "1        6304287        Izakaya Kikufuji           162       Makati City   \n",
      "2        6300002  Heat - Edsa Shangri-La           162  Mandaluyong City   \n",
      "3        6318506                    Ooma           162  Mandaluyong City   \n",
      "4        6314302             Sambo Kojin           162  Mandaluyong City   \n",
      "\n",
      "                                             Address  \\\n",
      "0  Third Floor, Century City Mall, Kalayaan Avenu...   \n",
      "1  Little Tokyo, 2277 Chino Roces Avenue, Legaspi...   \n",
      "2  Edsa Shangri-La, 1 Garden Way, Ortigas, Mandal...   \n",
      "3  Third Floor, Mega Fashion Hall, SM Megamall, O...   \n",
      "4  Third Floor, Mega Atrium, SM Megamall, Ortigas...   \n",
      "\n",
      "                                     Locality  \\\n",
      "0   Century City Mall, Poblacion, Makati City   \n",
      "1  Little Tokyo, Legaspi Village, Makati City   \n",
      "2  Edsa Shangri-La, Ortigas, Mandaluyong City   \n",
      "3      SM Megamall, Ortigas, Mandaluyong City   \n",
      "4      SM Megamall, Ortigas, Mandaluyong City   \n",
      "\n",
      "                                    Locality Verbose   Longitude   Latitude  \\\n",
      "0  Century City Mall, Poblacion, Makati City, Mak...  121.027535  14.565443   \n",
      "1  Little Tokyo, Legaspi Village, Makati City, Ma...  121.014101  14.553708   \n",
      "2  Edsa Shangri-La, Ortigas, Mandaluyong City, Ma...  121.056831  14.581404   \n",
      "3  SM Megamall, Ortigas, Mandaluyong City, Mandal...  121.056475  14.585318   \n",
      "4  SM Megamall, Ortigas, Mandaluyong City, Mandal...  121.057508  14.584450   \n",
      "\n",
      "                           Cuisines  ...          Currency Has Table booking  \\\n",
      "0        French, Japanese, Desserts  ...  Botswana Pula(P)               Yes   \n",
      "1                          Japanese  ...  Botswana Pula(P)               Yes   \n",
      "2  Seafood, Asian, Filipino, Indian  ...  Botswana Pula(P)               Yes   \n",
      "3                   Japanese, Sushi  ...  Botswana Pula(P)                No   \n",
      "4                  Japanese, Korean  ...  Botswana Pula(P)               Yes   \n",
      "\n",
      "  Has Online delivery Is delivering now Switch to order menu Price range  \\\n",
      "0                  No                No                   No           3   \n",
      "1                  No                No                   No           3   \n",
      "2                  No                No                   No           4   \n",
      "3                  No                No                   No           4   \n",
      "4                  No                No                   No           4   \n",
      "\n",
      "   Aggregate rating  Rating color Rating text Votes  \n",
      "0               4.8    Dark Green   Excellent   314  \n",
      "1               4.5    Dark Green   Excellent   591  \n",
      "2               4.4         Green   Very Good   270  \n",
      "3               4.9    Dark Green   Excellent   365  \n",
      "4               4.8    Dark Green   Excellent   229  \n",
      "\n",
      "[5 rows x 21 columns]\n",
      "The dataset must contain 'Restaurant Name', 'Rating', and 'City' columns.\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import os\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# Load the dataset\n",
    "full_file_path = r\"C:\\Users\\Sweth\\OneDrive\\Desktop\\DA inten\\Dataset  (1).csv\"\n",
    "data = pd.read_csv(full_file_path)\n",
    "\n",
    "# Check the first few rows to understand the dataset structure\n",
    "print(data.head())\n",
    "\n",
    "# Ensure there are the necessary columns ('Restaurant Name', 'Rating', 'City')\n",
    "if 'Restaurant Name' not in data.columns or 'Rating' not in data.columns or 'City' not in data.columns:\n",
    "    print(\"The dataset must contain 'Restaurant Name', 'Rating', and 'City' columns.\")\n",
    "else:\n",
    "    # 1. Identify restaurant chains by checking repeated Restaurant Names\n",
    "    restaurant_chain_counts = data['Restaurant Name'].value_counts()\n",
    "    \n",
    "    # Filter out the restaurants that appear more than once (restaurant chains)\n",
    "    restaurant_chains = restaurant_chain_counts[restaurant_chain_counts > 1]\n",
    "    \n",
    "    # Print restaurant chains and the number of locations for each\n",
    "    print(\"\\nRestaurant Chains (with multiple locations):\")\n",
    "    print(restaurant_chains)\n",
    "\n",
    "    # 2. Analyze ratings and popularity of restaurant chains\n",
    "    # Create a DataFrame to calculate average rating and number of locations for each chain\n",
    "    chain_analysis = data.groupby('Restaurant Name').agg(\n",
    "        avg_rating=('Rating', 'mean'),         # Calculate average rating\n",
    "        num_locations=('Restaurant Name', 'size')  # Count number of locations (popularity)\n",
    "    )\n",
    "    \n",
    "    # Filter to include only restaurant chains (more than one location)\n",
    "    chain_analysis = chain_analysis[chain_analysis['num_locations'] > 1]\n",
    "    \n",
    "    # Sort by average rating (descending) to find the highest-rated chains\n",
    "    chain_analysis_sorted_by_rating = chain_analysis.sort_values(by='avg_rating', ascending=False)\n",
    "    \n",
    "    # Sort by number of locations (popularity, descending)\n",
    "    chain_analysis_sorted_by_popularity = chain_analysis.sort_values(by='num_locations', ascending=False)\n",
    "    \n",
    "    # Print analysis results\n",
    "    print(\"\\nRestaurant Chains Sorted by Average Rating:\")\n",
    "    print(chain_analysis_sorted_by_rating[['avg_rating', 'num_locations']])\n",
    "\n",
    "    print(\"\\nRestaurant Chains Sorted by Popularity (Number of Locations):\")\n",
    "    print(chain_analysis_sorted_by_popularity[['avg_rating', 'num_locations']])\n",
    "\n",
    "    # Pie chart for the number of locations (popularity)\n",
    "    plt.figure(figsize=(10, 6))\n",
    "    plt.pie(chain_analysis['num_locations'], labels=chain_analysis.index, autopct='%1.1f%%', startangle=90)\n",
    "    plt.title(\"Restaurant Chains by Popularity (Number of Locations)\")\n",
    "    plt.axis('equal')  # Equal aspect ratio ensures that pie chart is circular.\n",
    "    plt.show()\n",
    "\n",
    "    # Pie chart for the average ratings of the restaurant chains\n",
    "    plt.figure(figsize=(10, 6))\n",
    "    plt.pie(chain_analysis['avg_rating'], labels=chain_analysis.index, autopct='%1.1f%%', startangle=90)\n",
    "    plt.title(\"Restaurant Chains by Average Rating\")\n",
    "    plt.axis('equal')  # Equal aspect ratio ensures that pie chart is circular.\n",
    "    plt.show()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bda0fed9-9f5b-4066-a080-ee4d41254a1c",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
