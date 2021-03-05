def build(brick, period):
    all_bricks = 0
    for week in range (1, period):
        all_bricks = all_bricks + brick
        print("%s week: %s bricks" % (week, all_bricks))

build(10, 40)