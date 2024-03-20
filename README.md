# And_The_Oscar_Goes_To...

## **Application Overview:**

This application is designed to highlight a variety of dashboard components offered by the Streamlit Python package, along with interactive charts available in Python. Navigating through the app is intuitive, with four main pages accessible via a dropdown menu in the sidebar:

1. Oscar 2024 Nominees: Explore this year's Oscar nominees.
2. My Predictions: My ML Model's Oscar predictions.
3. Past Oscar Winners: Delve into a repository of past Oscar winners.
4. Best Picture Emoji Quiz: Test your knowledge with an engaging emoji-based quiz about the best pictures of 2024.

## **Oscar 2024 Nominees:**

This page provides an overview of this year's nominees, categorized by movie and award category, through three distinct outputs:
- An interactive Plotly bar chart allows users to filter for specific award categories in the legend and hover their cursor over the bars for detailed information.
- A count summary table displays the total number of nominations by movie. Notably, "Oppenheimer" leads with an impressive 13 nominations, closely followed by "Poor Things" with 11, and "Killers of the Flower Moon" with 10.
- A detailed table presents all nominees across categories along with additional descriptions. For instance, it includes details on Best Actor and Actress nominees, their respective movies, and the roles they portrayed.

Each of these outputs offers further filtering options by selecting specific award categories in a dropdown multi-select box.

## **My Predictions:**

- Gathered data from various sources, excluding IMDB web-scraping due to time constraints.
- Acquired data on past winners and nominations from major movie awards like the Oscars, Golden Globes, Baftas, and SAG Awards.
- Organized data into four separate data frames in Jupyter Notebook, focusing on six key categories spanning from 1997.
- Cleaned and standardized the data, noting an imbalance with 680 false nominations, 156 true winners, and 35 TBA (to be awarded on March 10th).
- Segregated the 35 TBA entries into a separate data frame and experimented with under-sampling and over-sampling techniques.
- Employed three classifiers (DecisionTreeClassifier, GridSearch CSV, and RandomForestClassifier), with varied results for each approach.

## **Past Oscar Winners:**

This page retrieves live Oscar data from Wikipedia. While we acknowledge it may not be the most reliable source, Wikipedia offers well-formatted tables and comprehensive data dating back to the 1920s.

The highlight of the page is an interactive "jitter" plot showcasing the relationship between the number of nominations and awards won by movies. This plot employs a unique feature where scatter points are slightly offset to prevent overlap, enhancing visibility and clarity.

A jitter plot is particularly useful when one of the chart axes is not continuous, such as categorical or integer values. For instance, when there are more than 20 movies with 7 nominations and only 1 award, a normal scatter plot would result in overlapping points, making it difficult to discern individual data points.

## **Best Picture Emoji Quiz:**

This page is designed purely for entertainment purposes, showcasing Streamlit's capability of displaying emojis. Each of the 10 Best Picture nominees is represented by a unique set of emojis.

You can engage in the quiz in two modes:

#### **Easy Mode:**
Match the emojis to the corresponding movie using pre-filled dropdowns.
#### **Hard Mode:**
Challenge yourself by typing out the movie names in blank textboxes.

Experiment with different numbers of correct answers to observe how the output message changes based on your performance.
