# You are on a flight and wanna watch two movies during this flight.
# You are given int[] movie_duration which includes all the movie durations.
# You are also given the duration of the flight which is d in minutes.
# Now, you need to pick two movies and the total duration of the two movies is less than or equal to (d - 30min).
# Find the pair of movies with the longest total duration. If multiple found, return the pair with the longest movie.

# e.g.
# Input
# movie_duration: [90, 85, 75, 60, 120, 150, 125]
# d: 250

# [90, 125]
# 90min + 125min = 215 is the maximum number within 220 (250min - 30min)


def selectMovies(movies, flight_duration):
	movies.sort()
	max_time = 0
	target_time = flight_duration - 30
	num_movies = len(movies)
	result = []

	#movies = [60, 75, 85, 90, 120, 125, 150]

	for i in range(num_movies-1, 1, -1):
		for j in range(num_movies-2, 0, -1):
			time_sum = movies[i] + movies[j]
			if time_sum <= target_time:
				if time_sum > max_time:
					max_time = time_sum
					result = [movies[j], movies[i]]

	return result


print(selectMovies([90, 85, 75, 60, 120, 150, 125], 250)) # [90, 125]
print(selectMovies([90, 85, 75, 60, 120, 150, 125], 300)) # [120, 150]