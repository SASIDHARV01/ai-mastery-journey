"""Vectors teaching example. No external packages or Python containers needed."""

# First component: east positive / west negative.
# Second component: north positive / south negative.
vx = 3
vy = 2
wx = 2
wy = -1
scale = -2

sum_x = vx + wx
sum_y = vy + wy
difference_x = vx - wx
difference_y = vy - wy
scaled_x = scale * vx
scaled_y = scale * vy
length = (vx ** 2 + vy ** 2) ** 0.5
dot_product = vx * wx + vy * wy

print(f"v = ({vx}, {vy})")
print(f"w = ({wx}, {wy})")
print(f"v + w = ({sum_x}, {sum_y})")
print(f"v - w = ({difference_x}, {difference_y})")
print(f"{scale} * v = ({scaled_x}, {scaled_y})")
print(f"Length of v = {round(length, 3)}")
print(f"v dot w = {dot_product}")

if length == 0:
    print("The zero vector has no direction; a unit vector is undefined.")
else:
    unit_x = vx / length
    unit_y = vy / length
    print(f"Unit vector = ({round(unit_x, 3)}, {round(unit_y, 3)})")

# Distinguish route length from displacement for the opening question.
east_steps = 3
north_steps = 2
route_length = east_steps + north_steps
displacement_length = (east_steps ** 2 + north_steps ** 2) ** 0.5
print(f"Original east-then-north route = {route_length} steps")
print(f"Original straight-line displacement = {round(displacement_length, 3)} steps")
