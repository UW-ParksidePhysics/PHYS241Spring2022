from initial_conditions import set_initial_conditions
from unit_conversion import convert_units
from trajectory import calculate_height

initial_conditions = set_initial_conditions()

launch_angle = initial_conditions[2]
launch_angle = convert_units(launch_angle, 'degree', 'radian')

initial_velocity = initial_conditions[1]
initial_velocity = convert_units(initial_velocity, 'km/h', 'm/s')

projectile_height = calculate_height(initial_conditions[3],
                                     launch_angle,
                                     initial_velocity,
                                     initial_conditions[4])

print(f'y = {projectile_height:.3f} m')
