import math



def pageCount(last_page, target_page):
    distance = min(target_page, abs(last_page - target_page))

    if target_page == last_page:
        return 0

    if target_page <= 3:
        if target_page % 2 == 0:
            print(math.ceil(distance / 2))
        else:
            print(math.ceil(distance / 2) - 1)

    if last_page % 2 == 0:
        print(math.ceil(distance / 2))

    else:
        print(distance // 2)

pageCount(1, 1)