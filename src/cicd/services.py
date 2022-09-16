def pop_calculator(api_message):
    api_message = api_message.json()
    forks = api_message['forks']
    stars = api_message['stargazers_count']
    score = forks*2 + stars
    return score >= 500
