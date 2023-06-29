def better_than_average(class_points, your_points):
    class_points.append(your_points)
    return (your_points > sum(class_points) / len(class_points)):

better_than_average([41, 75, 72, 56, 80, 82, 81, 33], 1)
