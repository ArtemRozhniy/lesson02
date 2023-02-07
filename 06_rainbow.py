# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)


def rainbow(point, step):
    y = 5
    step = 5
    machine = 0
    for x in range(10, 26, 5):
        for y in range(10, 26, 5):
            y += step
            x2 = x + 990
            y2 = y + 990
            start_point = sd.get_point(x, y)
            end_point = sd.get_point(x2, y2)
            sd.line(start_point=start_point, end_point=end_point, color=rainbow_colors[machine], width=3)
        machine += 1
    # Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
# start_point = sd.get_point(50, 50)
# end_point = sd.get_point(350, 450)
# sd.line(start_point=start_point, end_point=end_point, color=rainbow_colors[0], width=4)
# start_point = sd.get_point(55, 50)
# end_point = sd.get_point(355, 450)
# sd.line(start_point=start_point, end_point=end_point, color=rainbow_colors[1], width=4)


def rainbow(x1, y1, x2, y2, step=5, lines_number=7):
    for i in range(lines_number):
        start_point = sd.get_point(x1, y1)
        end_point = sd.get_point(x2, y2)
        sd.line(start_point=start_point, end_point=end_point, color=rainbow_colors[i], width=4)
        x1 += step
        x2 += step


rainbow(x1=50, y1=50, x2=350, y2=450, step=5)


# for i in range(1, len(rainbow_colors) + 1):
#     start_point = sd.get_point(i * 50, 50)
#     end_point = sd.get_point(i * 50 * 7, 450)
#     sd.line(start_point=start_point, end_point=end_point, color=rainbow_colors[i - 1], width=4)



# rainbow(7, 5)

sd.pause()
