import re
from math import sqrt


def get_all_orientations(img):
    imgs = []
    flippeds = [[tuple(row) for row in img], [tuple(row) for row in img[::-1]]]
    for flipped in flippeds:
        rotated = flipped[::]
        for _ in range(3):
            imgs.append(rotated)
            rotated = list(zip(*rotated[::-1]))
        imgs.append(rotated)
    return imgs


def parse_rawimg(raw_img):
    splitted_img = raw_img.split('\n')
    return {re.search('[0-9]+', splitted_img[0]).group(): get_all_orientations(splitted_img[1:])}


def img_fits(img, row, col, full_img):
    if row == col == 0:
        return True
    if row == 0:
        return list(zip(*img))[0] == list(zip(*full_img[row][col-1][1]))[-1]
    if col == 0:
        return img[0] == full_img[row-1][col][1][-1]
    return list(zip(*img))[0] == list(zip(*full_img[row][col-1][1]))[-1] and img[0] == full_img[row-1][col][1][-1]


def next_pos(row, col, max_row, max_col):
    if col < (max_col - 1):
        return row, col + 1
    if row < max_row:
        return row + 1, 0


def make_fullimg(full_img, row, col, max_row, max_col, img_ids, id_to_imgs, has_sol):
    if row >= max_row:
        has_sol[0] = True
        return

    for img_id in img_ids:
        if has_sol[0]:
            return
        for img in id_to_imgs[img_id]:
            if img_fits(img, row, col, full_img):
                full_img[row][col] = (img_id, img)
                next_row, next_col = next_pos(row, col, max_row, max_col)
                make_fullimg(full_img, next_row, next_col, max_row, max_col, img_ids - {img_id}, id_to_imgs, has_sol)
                if has_sol[0]:
                    return


if __name__ == '__main__':
    id_to_imgs = {}
    with open('input', 'r') as f:
        for raw_img in f.read().strip().split('\n\n'):
            id_to_imgs.update(parse_rawimg(raw_img))

    rows = cols = int(sqrt(len(id_to_imgs)))
    full_img = [[None for _ in range(cols)] for _ in range(rows)]
    has_sol = [False]
    make_fullimg(full_img, 0, 0, rows, cols, set(id_to_imgs.keys()), id_to_imgs, has_sol)

    img = [[] for _ in range(len(full_img[0]) * (len(full_img[0][0][1]) - 2))]
    for i, super_row in enumerate(full_img):
        for _, tile in super_row:
            for k, row in enumerate(tile[1:-1]):
                img[i * (len(tile) - 2) + k] += row[1:-1]

    template = [
        '[.#]{18}#[.#]',
        '#[.#]{4}##[.#]{4}##[.#]{4}###',
        '[.#]#[.#]{2}#[.#]{2}#[.#]{2}#[.#]{2}#[.#]{2}#[.#]{3}'

    ]

    sharp_amounts = sum(map(lambda v: v == '#', [v for row in img for v in row]))
    for m in get_all_orientations(img):
        img_str_rows = [''.join(row) for row in m]
        count = 0
        for i in range(len(img_str_rows)):
            for j in range(len(img_str_rows[i]) - len(template[0])):
                if (i + 2) < len(img_str_rows) \
                        and re.search(template[0], img_str_rows[i][j:]) \
                        and re.search(template[1], img_str_rows[i + 1][j:]) \
                        and re.search(template[2], img_str_rows[i + 2][j:]):
                    count += 1
                    i += 2
        if count:
            print(sharp_amounts - (count * 15))
            break
