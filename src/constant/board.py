BOARD_SIZE = 6
# Used to detect when adding a line for drawing quarters.
HALF_BOARD_SIZE = (BOARD_SIZE / 2)

WIN_CONDITION = 5
WIN_AREA_CHECK = BOARD_SIZE - WIN_CONDITION + 1

QUARTER_BOUNDARIES = {
    0: (slice(0, 3), slice(0, 3)),
    1: (slice(0, 3), slice(3, 6)),
    2: (slice(3, 6), slice(3, 6)),
    3: (slice(3, 6), slice(0, 3))
}
