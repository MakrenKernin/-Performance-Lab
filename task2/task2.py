import sys

def read_circle_data(file_path):
    with open(file_path, 'r') as file:
        x, y = map(float, file.readline().strip().split())
        r = float(file.readline().strip())
        if not (-1e38 <= x <= 1e38 and -1e38 <= y <= 1e38 and 0 < r <= 1e38):
            raise ValueError("Координаты или радиус окружности вне допустимого диапазона")
        return x, y, r

def read_points_data(file_path):
    with open(file_path, 'r') as file:
        points = []
        for line in file:
            x, y = map(float, line.strip().split())
            if not (-1e38 <= x <= 1e38 and -1e38 <= y <= 1e38):
                raise ValueError("Координаты точки вне допустимого диапазона")
            points.append((x, y))
        if not (1 <= len(points) <= 100):
            raise ValueError("Количество точек должно быть от 1 до 100")
        return points

def determine_point_position(circle_x, circle_y, radius, point_x, point_y):
    distance_squared = (point_x - circle_x) ** 2 + (point_y - circle_y) ** 2
    radius_squared = radius ** 2
    if distance_squared == radius_squared:
        return 0  # точка лежит на окружности
    elif distance_squared < radius_squared:
        return 1  # точка внутри окружности
    else:
        return 2  # точка снаружи окружности

def main():
    if len(sys.argv) != 3:
        print("Укажите файлы с данными по примеру: python script.py <circle_data_file>.txt <points_data_file>.txt")
        return
    
    circle_data_file = sys.argv[1]
    points_data_file = sys.argv[2]

    try:
        circle_x, circle_y, radius = read_circle_data(circle_data_file)
        points = read_points_data(points_data_file)
    except ValueError as e:
        print(f"Ошибка: {e}")
        return

    for point_x, point_y in points:
        position = determine_point_position(circle_x, circle_y, radius, point_x, point_y)
        print(position)

if __name__ == "__main__":
    main()
