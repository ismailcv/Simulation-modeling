# 1. ödev monte carlo yöntemi kullanarak çözeceğiz.
# İsmail Can VARLI   

import random

def monte_carlo_triangle_area(base: float, height: float, num_samples: int) -> float:
    num_points_inside = 0
    for i in range(num_samples):
        x = random.uniform(0, base)
        y = random.uniform(0, height)
        if y <= -height / base * x + height:
            num_points_inside += 1
    area_rectangular = base * height
    area_triangle = area_rectangular * num_points_inside / num_samples
    return area_triangle

base1 = 2  # taban uzunluğu
height1 = 2  # yükseklik
base2 = 4  # taban uzunluğu
height2 = 1  # yükseklik
base3 = 2  # taban uzunluğu
height3 = 1  # yükseklik

num_samples = 1000000  # nokta sayısı

triangle_area_1 = monte_carlo_triangle_area(base1, height1, num_samples)
triangle_area_2 = monte_carlo_triangle_area(base2, height2, num_samples)
triangle_area_3 = monte_carlo_triangle_area(base3, height3, num_samples)

def monte_carlo_rectangle_area(length: float, width: float, num_samples: int) -> float:
    num_points_inside = 0
    for i in range(num_samples):
        x = random.uniform(0, length)
        y = random.uniform(0, width)
        if x <= length and y <= width:
            num_points_inside += 1
    area_rectangular = length * width
    area_rectangle = area_rectangular * num_points_inside / num_samples
    return area_rectangle

length1 = 4  # uzun kenar uzunluğu
width1 = 1  # kısa kenar uzunluğu


num_samples = 1000000  # nokta sayısı

rectangle_area1 = monte_carlo_rectangle_area(length1, width1, num_samples)


#Tüm alanlar toplanıyor ve sonucu bize veriyor.

print(triangle_area_1 + triangle_area_2 + triangle_area_3 + rectangle_area1)
