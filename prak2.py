import networkx as nx
import vk_api
import matplotlib.pyplot as plt

#  Авторизация в VK API
access_token = ''
vk_session = vk_api.VkApi(token=access_token)
vk = vk_session.get_api()

# Получение информации о друзьях
def get_friends(user_id):
    try:
        friends = vk.friends.get(user_id=user_id)
        return friends['items']
    except vk_api.exceptions.ApiError as e:
        print(f"Ошибка при получении друзей для пользователя {user_id}: {e}")
        return []

def get_friends_of_friends(user_id):
    friends = get_friends(user_id)
    friends_of_friends = set()
    for friend in friends:
        friends_of_friends.update(get_friends(friend))
    return friends_of_friends

# Создание графа
G = nx.Graph()

# Добавляем членов группы и их друзей
group_members = []  
for member in group_members:
    friends = get_friends(member)
    G.add_node(member)
    for friend in friends:
        G.add_edge(member, friend)

# Добавляем друзей друзей
for member in group_members:
    friends_of_friends = get_friends_of_friends(member)
    for friend in friends_of_friends:
        G.add_node(friend)
        if friend in G.nodes():
            G.add_edge(member, friend)

# Расчет центральности
# Степенная центральность (Degree Centrality)
degree_centrality = nx.degree_centrality(G)
print("Степенная центральность:")
for member in group_members:
    print(f"Пользователь {member}: {degree_centrality[member]}")

# Центральность по близости (Closeness Centrality)
closeness_centrality = nx.closeness_centrality(G)
print("Центральность по близости:")
for member in group_members:
    print(f"Пользователь {member}: {closeness_centrality[member]}")

# Центральность по посредничеству (Betweenness Centrality)
betweenness_centrality = nx.betweenness_centrality(G)
print("Центральность по посредничеству:")
for member in group_members:
    print(f"Пользователь {member}: {betweenness_centrality[member]}")

# Центральность по собственному вектору (Eigenvector Centrality)
eigenvector_centrality = nx.eigenvector_centrality(G)
print("Центральность по собственному вектору:")
for member in group_members:
    print(f"Пользователь {member}: {eigenvector_centrality[member]}")

#  Визуализация графа (опционально)
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold')
plt.show()