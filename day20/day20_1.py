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
    print(has_sol)
    if has_sol[0]:
        print(int(full_img[0][0][0]) * int(full_img[0][-1][0]) * int(full_img[-1][0][0]) * int(full_img[-1][-1][0]))


