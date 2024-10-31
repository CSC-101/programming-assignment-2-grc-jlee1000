import data

# Write your functions for each part in the space below.

# Part 1
def create_rectangle(point1: 'Point', point2: 'Point') -> 'Rectangle':
    """Creates a Rectangle object based on two given Points.
    Determines the top-left and bottom-right corners by finding
    the leftmost, rightmost, highest, and lowest coordinates.
    Parameters:
    - point1: The first Point object.
    - point2: The second Point object.
    Returns:
    - Rectangle: A Rectangle object created with the top-left
      and bottom-right corners.
    """
    top_left = Point(min(point1.x, point2.x), max(point1.y, point2.y))
    bottom_right = Point(max(point1.x, point2.x), min(point1.y, point2.y))
    return Rectangle(top_left, bottom_right)

# Part 2
def shorter_duration_than(duration1: 'Duration', duration2: 'Duration') -> bool:
    """Compares two Duration objects to see if the first is shorter than the second.
    Parameters:
    - duration1: First Duration object to compare.
    - duration2: Second Duration object to compare.
     Returns:
    - bool: True if duration1 is shorter, False otherwise.
    """
    return (duration1.minutes * 60 + duration1.seconds) < (duration2.minutes * 60 + duration2.seconds)

# Part 3
def songs_shorter_than(songs: list['Song'], max_duration: 'Duration') -> list['Song']:
    """Filters a list of songs to find those with durations shorter than a given Duration.
    Parameters:
    - songs: List of Song objects to filter.
    - max_duration: Duration object representing the upper bound.
    Returns:
    - list[Song]: List of songs with durations shorter than max_duration.
    """
    return [song for song in songs if shorter_duration_than(song.duration, max_duration)]

# Part 4
def running_time(songs: list['Song'], playlist: list[int]) -> 'Duration':
    """Calculates the total Duration of a playlist based on song indices.
    Parameters:
    - songs: List of Song objects.
    - playlist: List of integers representing song indices for the playlist.
    Returns:
    - Duration: The total Duration for the playlist in whole minutes and seconds.
    """
    total_seconds = sum(
        song.duration.minutes * 60 + song.duration.seconds
        for i, song in enumerate(songs) if i in playlist
    )
    return Duration(total_seconds // 60, total_seconds % 60)

# Part 5
def validate_route(city_links: list[list[str]], route: list[str]) -> bool:
    """Validates if a given route between cities is connected as per city links.
    Parameters:
    - city_links: List of city pairs indicating connections between cities.
    - route: List of city names representing a route to validate.
    Returns:
    - bool: True if the route is valid, False otherwise."""
    for i in range(1, len(route)):
        if [route[i - 1], route[i]] not in city_links and [route[i], route[i - 1]] not in city_links:
            return False
    return True

# Part 6
def longest_repetition(numbers: list[int]) -> Optional[int]:
    """Finds the starting index of the longest contiguous repetition of a number.
    Parameters:
    - numbers: List of integers to check for repetitions.
    Returns:
    - Optional[int]: The starting index of the longest contiguous repetition
      or None if the list is empty.
    """
    if not numbers:
        return None

    max_count = 1
    max_index = 0
    current_count = 1
    current_index = 0

    for i in range(1, len(numbers)):
        if numbers[i] == numbers[i - 1]:
            current_count += 1
        else:
            if current_count > max_count:
                max_count = current_count
                max_index = current_index
            current_count = 1
            current_index = i

    if current_count > max_count:
        max_index = current_index

    return max_index