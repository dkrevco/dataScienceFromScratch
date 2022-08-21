users = []

names = ['Liam', 'Olivia', 'Noah', 'Emma', 'Oliver', 'Charlotte', 'Elijah', 'Amelia', 'James', 'Ava']

for i, name in enumerate(names):
    users.append({'id': i, 'name': name})

back_up_users = users.copy()

for user in users:
    user['friends'] = []


friendships = [
    (0, 1), (0, 2), (0, 7), (1, 2), (1, 9), (2, 3), (2, 4), (3, 6), (3, 7),
    (4, 7), (5, 6), (5, 8), (6, 7), (6, 9), (8, 9)]

friendships.sort(key=lambda a: a[1])
friendships.sort(key=lambda a: a[0])


for i, j in friendships:
    users[i]['friends'].append(users[j])
    users[j]['friends'].append(users[i])


def number_of_friends(user): return len(user['friends'])


total_connections = sum(number_of_friends(user) for user in users)
num_users = len(users)
avg_connections = total_connections / num_users
num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]

"""
SyntaxError: invalid syntax

sorted(num_friends_by_id,
key=lambda (user_id, num_friends): num_friends,
reverse=True)
"""


def friends_of_friend_ids_bad(user):
    # "foaf" is short for "friend of a friend"
    return [foaf["id"] for friend in user["friends"] for foaf in friend["friends"]]


from collections import Counter


def friends_of_friends(user):

    user_id = user['id']

    return Counter(foaf_id for friend_id in friendships[user_id] for foaf_id in friendships[friend_id]
                   if foaf_id != user and foaf_id not in friendships[user_id])


interests = [(0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
            (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
            (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
            (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
            (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
            (3, "statistics"), (3, "regression"), (3, "probability"),
            (4, "machine learning"), (4, "regression"), (4, "decision trees"),
            (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
            (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
            (6, "probability"), (6, "mathematics"), (6, "theory"),
            (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
            (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
            (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
            (9, "Java"), (9, "MapReduce"), (9, "Big Data")
            ]

import random

themes = []

for i, j in interests:
    _ = i
    if j not in themes:
        themes.append(j)

for i in range(10, 21):
    x = 3
    while x < random.randint(4, 7):
        interests.append((i, random.choice(themes)))
        x += 1

def data_scientists_who_like(target_interest):

    return [user_id for user_id, user_interest in interests if user_interest == target_interest]

shared_themes = []

for theme in themes:
    shared_themes.append({theme: data_scientists_who_like(theme)})

# better realization

from collections import defaultdict

user_ids_by_interests = defaultdict(list)

for user_id, interest in interests:
    user_ids_by_interests[interest].append(user_id)

interests_by_user_id = defaultdict(list)

for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)

def most_common_interests_with(user):
    return Counter(interested_user_id for interest in interests_by_user_id[user['id']]
                   for interested_user_id in user_ids_by_interests[interest]
                   if interested_user_id != user['id'])

salaries_and_tenures = [(83000, 8.7), (88000, 8.1), (48000, 0.7), (76000, 6), (69000, 6.5), (76000, 7.5),
                        (60000, 2.5), (83000, 10), (48000, 1.9), (63000, 4.2)]

salary_by_tenure = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)

average_salary_by_tenure = {tenure : sum(salaries) / len(salaries) for tenure, salaries in salary_by_tenure.items()}


def tenure_bucket(tenure):
    if tenure < 2:
        return "less than two"
    elif tenure < 5:
        return "between two and five"
    else:
        return "more than five"

salary_by_tenure_bucket = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    bucket = tenure_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)

average_salary_by_bucket = {tenure_bucket : sum(salaries) / len(salaries) for tenure_bucket, salaries in salary_by_tenure_bucket.items()}

words_and_counts = Counter(word for user, interest in interests for word in interest.lower().split())

for word, count in words_and_counts.most_common():
    if count > 1:
        print(word, count)