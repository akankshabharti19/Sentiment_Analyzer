# Import the SentimentIntensityAnalyzer class from the vaderSentiment package
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Input a statement from the user
sentence = input("Sentence: \n")

# Create an instance of SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

# Finds the sentiment scores for the given sentence
vs = analyzer.polarity_scores(sentence)

# Prints the output in the required format
print(vs)

# Determine the overall tone based on the compound score
compound_score = vs['compound']

if compound_score > 0.05:
    print("\n Overall tone is positive")
elif compound_score < -0.05:
    print("\n Overall tone is negative")
else:
    print("\n Overall tone is neutral")

# Import matplotlib for plotting
import matplotlib.pyplot as plt
import numpy as np

# Create an array of sentiment scores multiplied by 100 for the pie chart
y = np.array([
    vs.get("neg") * 100,
    vs.get("neu") * 100,
    vs.get("pos") * 100
])

# Define labels for the pie chart
mylabels = ["Negative", "Neutral", "Positive"]

# Plot the pie chart
plt.pie(y, labels=mylabels)
plt.legend(title="Sentiment:")
plt.show()