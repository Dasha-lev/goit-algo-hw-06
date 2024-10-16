import networkx as nx
import matplotlib.pyplot as plt

# Створюємо порожній граф
metro_graph = nx.Graph()

#Червона лінія метро
red_line = [
    "Академмістечко", "Житомирська", "Святошин", "Нивки", "Берестейська", 
    "Шулявська", "Політехнічний інститут", "Вокзальна", "Університет", 
    "Театральна", "Хрещатик", "Арсенальна", "Дніпро", "Гідропарк", 
    "Лівобережна", "Дарниця", "Чернігівська", "Лісова"
]

#Синя лінія метро
blue_line = [
    "Героїв Дніпра", "Мінська", "Оболонь", "Почайна", "Тараса Шевченка", 
    "Контрактова площа", "Поштова площа", "Майдан Незалежності", 
    "Площа Льва Толстого", "Олімпійська", "Палац 'Україна'", "Либідська", 
    "Деміївська", "Голосіївська", "Васильківська", "Виставковий центр", 
    "Іподром", "Теремки"
]

#Зелена лінія метро
green_line = [
    "Сирець", "Дорогожичі", "Лук'янівська", "Золоті ворота", "Палац спорту", 
    "Кловська", "Печерська", "Дружби народів", "Видубичі", "Славутич", 
    "Осокорки", "Позняки", "Харківська", "Вирлиця", "Бориспільська", 
    "Червоний хутір"
]

#Додаємо станції та зв'язки для кожної лінії
def add_line_to_graph(line):
    for i in range(len(line) - 1):
        metro_graph.add_edge(line[i], line[i+1])

add_line_to_graph(red_line)
add_line_to_graph(blue_line)
add_line_to_graph(green_line)

#Додаємо пересадкові станції 
metro_graph.add_edge("Театральна", "Золоті ворота") 
metro_graph.add_edge("Хрещатик", "Майдан Незалежності") 
metro_graph.add_edge("Площа Льва Толстого", "Палац спорту") 

#Візуалізуємо граф
plt.figure(figsize=(10, 10))
pos = nx.spring_layout(metro_graph)  # Позиція вузлів для візуалізації
nx.draw(metro_graph, pos, with_labels=True, node_color='skyblue', node_size=5000, font_size=10, font_weight='bold', edge_color='gray')

plt.title("Київська Мережа Метро")
plt.show()

#Функція для DFS 
def dfs(graph, start, goal, path=None):
    if path is None:
        path = []  
    path.append(start)  
    if start == goal: 
        return path
   
    for neighbor in graph[start]:
        if neighbor not in path:  
            new_path = dfs(graph, neighbor, goal, path.copy())  
            if new_path:
                return new_path
    return None  

#Функція для BFS 
def bfs(graph, start, goal):
    queue = [(start, [start])]  
    while queue:
        vertex, path = queue.pop(0)  
        for neighbor in graph[vertex]:  
            if neighbor not in path:
                if neighbor == goal:  
                    return path + [neighbor]
                else:
                    queue.append((neighbor, path + [neighbor]))  
    return None  

#Вибираємо стартову та кінцеву станції для пошуку
start_station = "Академмістечко"
end_station = "Червоний хутір"

#Знаходимо шляхи за допомогою DFS та BFS
dfs_path = dfs(metro_graph, start_station, end_station)
bfs_path = bfs(metro_graph, start_station, end_station)


print(f"DFS шлях від {start_station} до {end_station}: {dfs_path}")
print(f"BFS шлях від {start_station} до {end_station}: {bfs_path}")
