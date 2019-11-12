from collections import deque
input = [[0,1], [0,2], [1,3], [2,3], [2,5], [5,6], [3,4]]
num_links = 7
num_routes = 7

# result [2, 3, 5]

route_dict = {}
visited_points = set()


for link in input:
  if link[0] in route_dict:
    route_dict[link[0]] += [link[1]]
  else:
    route_dict[link[0]] = [link[1]]

  if link[1] in route_dict:
    route_dict[link[1]] += [link[0]]
  else:
    route_dict[link[1]] = [link[0]]

print(route_dict)


def dfs(cut_route, route, route_dict, visited_points):
  visited_points.add(route)

  next_routes = route_dict[route]

  for next_route in next_routes:
        
    if next_route == cut_route or next_route in visited_points:
      continue

    visited_points = visited_points.union(dfs(cut_route, next_route, route_dict, visited_points))
  return visited_points

result = set()
for i in range(num_routes):
  visited_points = set()
  if i == 0:
    visited_points = dfs(i, 1, route_dict, visited_points)
  else:
    visited_points = dfs(i, 0, route_dict, visited_points)
  # print(i)
  # print(f'final {visited_points}')
  # print(f'length is {len(visited_points)}')
  if len(visited_points) != num_routes-1:
    result.add(i)


print(list(result))