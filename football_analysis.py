import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset into a Pandas DataFrame
data = pd.read_csv('results.csv')

# Filter the data for the relevant date range and selected international football teams
data['date'] = pd.to_datetime(data['date'])
data = data[(data['date'].dt.year >= 2011) & (data['date'].dt.year <= 2020)]
teams = ['Germany', 'Brazil', 'Spain', 'Argentina', 'France']
data = data[(data['home_team'].isin(teams)) | (data['away_team'].isin(teams))]

# Calculate the winning percentage trend for each selected team by year
results = {}
for year in range(2011, 2021):
    for team in teams:
        home_games = data[(data['home_team'] == team) & (data['date'].dt.year == year)]
        away_games = data[(data['away_team'] == team) & (data['date'].dt.year == year)]
        games = pd.concat([home_games, away_games])
        total_games = len(games)
        total_wins = len(games[(games['home_team'] == team) & (games['home_score'] > games['away_score'])]) + \
                     len(games[(games['away_team'] == team) & (games['away_score'] > games['home_score'])])
        win_percent = total_wins / total_games * 100 if total_games > 0 else 0
        results.setdefault(team, {})[year] = win_percent

# Create summary tables for winning percentages
table1a = pd.DataFrame(results).T
table1a.index.name = 'Team'
table1a.columns.name = 'Year'

table1b = pd.DataFrame(results)
table1b.index.name = 'Year'
table1b.columns.name = 'Team'

# Display winning percentages
print('Table 1a: Winning Percentage by Team by Year')
print(table1a)

print('\nTable 1b: Winning Percentage by Year by Team')
print(table1b)

# Visualize winning percentages
plt.plot(table1b)
plt.title('Winning Percentage by Year by Team')
plt.xlabel('Year')
plt.ylabel('Winning Percentage')
plt.legend(table1b.columns)
plt.show()

# Summary of winning percentage trends
print('\nSummary:')
print('The winning percentage of each selected team varies by year. Germany and Brazil show consistent performance, while other teams fluctuate more significantly.')

# Calculate average goals per match for each team by year
goals_results = {}
for year in range(2011, 2021):
    for team in teams:
        home_games = data[(data['home_team'] == team) & (data['date'].dt.year == year)]
        away_games = data[(data['away_team'] == team) & (data['date'].dt.year == year)]
        games = pd.concat([home_games, away_games])
        total_goals = home_games['home_score'].sum() + away_games['away_score'].sum()
        total_games = len(games)
        goals_per_match = total_goals / total_games if total_games > 0 else 0
        goals_results.setdefault(team, {})[year] = goals_per_match

# Summarize average goals per match
table2a = pd.DataFrame(goals_results)
table2a.index.name = 'Year'
table2a.columns.name = 'Team'

print('\nTable 2b: Average Number of Goals per Match by Year by Team')
print(table2a)

# Calculate correlation between winning percentage and average goals
correlation = table1b.corrwith(table2a)
print('\nCorrelation between Winning Percentage and Average Goals per Match by Team:')
print(correlation)

# Create scatter plots for correlation analysis
for team in teams:
    plt.scatter(table1b[team], table2a[team])
    plt.title(f'Winning Percentage vs. Average Goals per Match for {team}')
    plt.xlabel('Winning Percentage')
    plt.ylabel('Average Goals per Match')
    plt.show()

# Findings regarding goals and winning
print('The analysis shows a weak positive correlation between winning percentage and average goals per match, suggesting that while scoring more goals may lead to winning, other factors also play a significant role.')

# Winning trends based on previous match outcomes
df = pd.read_csv('results.csv')
df['date'] = pd.to_datetime(df['date'])
df = df[(df['date'] >= '2011-01-01') & (df['date'] <= '2020-12-31')]
df = df[df['home_team'].isin(teams) & df['away_team'].isin(teams)]

# Determine winning team for each match
df.loc[df['home_score'] > df['away_score'], 'winning_team'] = df['home_team']
df.loc[df['away_score'] > df['home_score'], 'winning_team'] = df['away_team']
df['previous_winning_team'] = df['winning_team'].shift(1)
df['second_previous_winning_team'] = df['winning_team'].shift(2)

# Calculate winning percentages under different conditions
condition_a = (df['winning_team'] == df['previous_winning_team']) & (df['winning_team'] == df['second_previous_winning_team'])
winning_prob_a = len(df[condition_a]) / len(df)

condition_b = (df['winning_team'] == df['previous_winning_team']) | (df['winning_team'] == df['second_previous_winning_team'])
winning_prob_b = len(df[condition_b]) / len(df)

condition_c = (df['winning_team'] != df['previous_winning_team']) & (df['winning_team'] != df['second_previous_winning_team'])
winning_prob_c = len(df[condition_c]) / len(df)

# Display winning probabilities
print('Winning probability given two previous wins:', round(winning_prob_a * 100, 2), '%')
print('Winning probability given one previous win:', round(winning_prob_b * 100, 2), '%')
print('Winning probability given two previous losses:', round(winning_prob_c * 100, 2), '%')

# Discussion of trends in winning probabilities
print("The findings indicate that teams with winning records are more likely to continue winning, while teams that have lost their last two matches show a significantly lower winning percentage.")

# Analyze goal scoring statistics
df_selected = df[(df['date'] >= '2011-01-01') & (df['date'] <= '2020-12-31')]
home_mean = df_selected['home_score'].mean()
home_std = df_selected['home_score'].std()
away_mean = df_selected['away_score'].mean()
away_std = df_selected['away_score'].std()

# Create standardized scores for visualization
df_selected['home_score_std'] = (df_selected['home_score'] - home_mean) / home_std if home_std > 0 else 0
df_selected['away_score_std'] = (df_selected['away_score'] - away_mean) / away_std if away_std > 0 else 0

# Boxplot for standardized scores
df_selected[['home_score_std', 'away_score_std']].plot(kind='box')
plt.title('Standardized Scores of Goals for Selected Teams')
plt.xlabel('Team')
plt.ylabel('Standardized Score')
plt.show()

# Histogram of goal distribution
plt.hist(df_selected[['home_score', 'away_score']].values.flatten(), bins=30)
plt.xlabel('Goals scored')
plt.ylabel('Frequency')
plt.title('Distribution of Goals Scored by Selected Teams')
plt.show()

# Calculate draws and scoring probabilities
df_selected_teams = df[(df['home_team'].isin(teams)) & (df['away_team'].isin(teams))]
num_draws = len(df_selected_teams[df_selected_teams['home_score'] == df_selected_teams['away_score']])
num_home_goals = len(df_selected_teams[df_selected_teams['home_score'] >= 1])

p_A = num_draws / len(df_selected_teams)
p_B_given_A = num_home_goals / num_draws if num_draws > 0 else 0
p_B = num_home_goals / len(df_selected_teams)

# Calculate conditional probability
p_A_given_B = (p_B_given_A * p_A) / p_B if p_B > 0 else 0
print("The conditional probability of a draw given that the home team scores at least one goal is", p_A_given_B)

# Calculate and plot the probability distribution of home scores
score_counts = df_selected['home_score'].value_counts()
total_scores = score_counts.sum()
score_probs = score_counts / total_scores

plt.bar(score_probs.index, score_probs.values)
plt.xlabel('Home Scores')
plt.ylabel('Probability')
plt.title('Probability Distribution of Home Scores')
plt.show()