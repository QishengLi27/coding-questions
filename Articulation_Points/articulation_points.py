input = [[0,1], [0,2], [1,3], [2,3], [2,5], [5,6], [3,4]]
num_links = 7
num_routes = 7

# result [2, 3, 5]

def ap(input, num_links, num_routes):
	route_dict = {}
	visited_points = set()

	# save routes in dict
	# {0: [1, 2], 1: [0, 3], 2: [0, 3, 5], 3: [1, 2, 4], 5: [2, 6], 6: [5], 4: [3]}
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

	result = set()

	# use each point and the first point in the graph to do dfs 
	# and see if all other points could be visited
	for i in range(num_routes):
		visited_points = set()
		if i == 0:
		  visited_points = dfs(i, 1, route_dict, visited_points)
		else:
		  visited_points = dfs(i, 0, route_dict, visited_points)
		# print(i)
		# print(f'final {visited_points}')
		# print(f'length is {len(visited_points)}')

		# if the length of visited points is not equal to num_routes - 1, add the point to result
		if len(visited_points) != num_routes - 1:
			result.add(i)

	return list(result)

def dfs(cut_route, route, route_dict, visited_points):
	# add current point to visited
	visited_points.add(route)

	# get connected routes from current route
	next_routes = route_dict[route]

	# for each connected point do dfs to get full path and add to visited list
	for next_route in next_routes:
	    if next_route == cut_route or next_route in visited_points:
			continue
		visited_points = visited_points.union(dfs(cut_route, next_route, route_dict, visited_points))
	return visited_points