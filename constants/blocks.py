# 4x4 matrix
COMMON_BLOCKS = [
    [   # North-East C
        [0,0,0,0], #
        [0,0,0,0], #
        [1,0,0,0], #█
        [1,1,0,0], #██
    ],
    [   # South-West C
        [0,0,0,0], #
        [0,0,0,0], #
        [1,1,0,0], #██
        [0,1,0,0]  # █
    ],
    [   # Nort-West C
        [0,0,0,0], #
        [0,0,0,0], #
        [0,1,0,0], # █
        [1,1,0,0]  #██
    ],
    [   # South-East C
        [0,0,0,0], #
        [0,0,0,0], #
        [1,1,0,0], #██
        [1,0,0,0]  #█
    ],
    [   # Horizontal J
        [0,0,0,0], #
        [0,0,0,0], #
        [1,0,0,0], #█
        [1,1,1,0]  #███
    ],
    [   # Horizontal L
        [0,0,0,0], #
        [0,0,0,0], #
        [0,0,1,0], #  █
        [1,1,1,0]  #███
    ],
    [   # Vertical L (Upside-down)
        [0,0,0,0], #
        [1,1,0,0], #██
        [0,1,0,0], # █
        [0,1,0,0]  # █
    ],
    [   # Vertical L
        [0,0,0,0], #
        [1,0,0,0], #█
        [1,0,0,0], #█
        [1,1,0,0]  #██
    ],
    [   # East T
        [0,0,0,0], #
        [1,0,0,0], #█
        [1,1,0,0], #██
        [1,0,0,0]  #█
    ],
    [   # West T
        [0,0,0,0], #
        [0,1,0,0], # █
        [1,1,0,0], #██
        [0,1,0,0]  # █
    ],
    [   # North T
        [0,0,0,0], #
        [0,0,0,0], #
        [0,1,0,0], # █
        [1,1,1,0]  #███
    ],
    [   # South T
        [0,0,0,0], #
        [0,0,0,0], #
        [1,1,1,0], #███
        [0,1,0,0]  # █
    ],
    [   # Horizontal Z
        [0,0,0,0], #
        [0,0,0,0], #
        [1,1,0,0], #██
        [0,1,1,0]  # ██
    ],
    [   # Horizontal S
        [0,0,0,0], #
        [0,0,0,0], #
        [0,1,1,0], # ██
        [1,1,0,0]  #██
    ],
    [   # Vertical S
        [0,0,0,0], #
        [1,0,0,0], #█
        [1,1,0,0], #██
        [0,1,0,0]  # █
    ],
    [   # Vertical Z
        [0,0,0,0], #
        [0,1,0,0], # █
        [1,1,0,0], #██
        [1,0,0,0]  #█
    ],
    [   # Vertical I
        [1,0,0,0], #█
        [1,0,0,0], #█
        [1,0,0,0], #█
        [1,0,0,0]  #█
    ],
    [   # Horizontal I
        [0,0,0,0], #█
        [0,0,0,0], #█
        [0,0,0,0], #█
        [1,1,1,1]  #█
    ],
    [   # O
        [0,0,0,0], #
        [0,0,0,0], #
        [1,1,0,0], #██
        [1,1,0,0]  #██
    ],
    [   # .
        [0,0,0,0], #
        [0,0,0,0], #
        [0,0,0,0], #
        [1,0,0,0]  #█
    ]
]

# 5x5 Matrix
CIRCLE_BLOCKS = [
    [   # Big Square
        [0,0,0,0,0], #
        [1,1,1,1,0], #████
        [1,1,1,1,0], #████
        [1,1,1,1,0], #████
        [1,1,1,1,0]  #████
    ],
     [   # Big  Circle
        [0,0,0,0,0], #
        [0,1,1,0,0], # ██
        [1,1,1,1,0], #████
        [1,1,1,1,0], #████
        [0,1,1,0,0]  # ██
    ],
     [   # Big U
        [0,0,0,0,0], #
        [1,0,0,1,0], #█  █
        [1,0,0,1,0], #█  █
        [1,0,0,1,0], #█  █
        [1,1,1,1,0]  #████
    ],
    [   # South-West angle
        [0,0,0,0,0], #
        [1,1,1,1,0], #████
        [0,0,0,1,0], #   █
        [0,0,0,1,0], #   █
        [0,0,0,1,0]  #   █
    ],
    [   # Odd rectangle
        [0,0,0,0,0], #
        [1,1,1,1,0], #
        [0,0,0,1,0], #
        [1,1,1,1,0], #████
        [1,1,1,0,0]  #███
    ],
    [   # Reverse C
        [0,0,0,0,0], #
        [1,1,1,1,0], #████
        [0,0,0,1,0], #   █
        [0,0,0,1,0], #   █
        [1,1,1,1,0]  #████
    ],
    [   # Vertical Long Rectangle
        [0,0,0,0,0], #
        [1,1,0,0,0], #██
        [1,1,0,0,0], #██
        [1,1,0,0,0], #██
        [1,1,0,0,0]  #██
    ],
    [   # Horinzontal Long Rectangle
        [0,0,0,0,0], #
        [0,0,0,0,0], #
        [0,0,0,0,0], #
        [1,1,1,1,0], #████
        [1,1,1,1,0]  #████
    ],
     [   # Vertical I
         [1,0,0,0,0], #█
        [1,0,0,0,0], #█
        [1,0,0,0,0], #█
        [1,0,0,0,0], #█
        [1,0,0,0,0]  #█
    ],
    [   # Horinzontal I
        [0,0,0,0,0], #
        [0,0,0,0,0], #
        [0,0,0,0,0], #
        [0,0,0,0,0], #
        [1,1,1,1,0]  #█████
    ],
    [   # Hat
        [0,0,0,0,0], #
        [0,0,0,0,0], #
        [0,0,0,0,0], #
        [1,1,1,1,1], #█████
        [1,0,0,0,1]  #█   █
    ],
     [   # Hook
        [0,0,0,0,0], #
        [1,0,0,0,0], #█
        [1,0,0,0,0], #█
        [1,0,0,1,0], #█  █
        [1,1,1,1,0]  #████
    ]
]

# 5x5 Matrix
DIAMOND_BLOCKS = [
    [   # Top-Left Corner
        [0,0,0,0,0], #
        [0,0,1,1,0], #  ██
        [0,1,1,0,0], # ██
        [1,1,0,0,0], #██
        [1,0,0,0,0]  #█
    ],
    [    # Top-Right Corner
        [0,0,0,0,0], #
        [1,1,0,0,0], #██
        [0,1,1,0,0], # ██
        [0,0,1,1,0], #  ██
        [0,0,0,1,0]  #   █
    ],
    [    # Bottom-Left Corner
        [0,0,0,0,0], #
        [1,0,0,0,0], #█
        [1,1,0,0,0], #██
        [0,1,1,0,0], # ██
        [0,0,1,1,0]  #  ██
    ],
    [    # Bottom-Right Corner
        [0,0,0,0,0], #
        [0,0,0,1,0], #   █
        [0,0,1,1,0], #  ██
        [0,1,1,0,0], # ██
        [1,1,0,0,0]  #██
    ],
    [    # Thick T
        [0,0,0,0,0], #
        [1,1,1,1,0], #████
        [0,1,1,0,0], # ██
        [0,1,1,0,0], # ██
        [0,1,1,0,0]  # ██
    ],
    [    # Vertical I
        [1,0,0,0,0], #█
        [1,0,0,0,0], #█
        [1,0,0,0,0], #█
        [1,0,0,0,0], #█
        [1,0,0,0,0]  #█
    ],
    [    # Horizontal I
        [0,0,0,0,0], #
        [0,0,0,0,0], #
        [0,0,0,0,0], #
        [0,0,0,0,0], #
        [1,1,1,1,1]  #█████
    ],
    [    # Thick X
        [0,0,0,0,0], #
        [1,0,0,1,0], #█  █
        [0,1,1,0,0], # ██
        [0,1,1,0,0], # ██
        [1,0,0,1,0]  #█  █
    ],
    [    # West T
        [0,0,0,0,0], #
        [0,0,0,0,0], #
        [0,0,0,1,0], #   █
        [1,1,1,1,0], #████
        [0,0,0,1,0]  #   █
    ],
    [    # Pyramid
        [0,0,0,0,0], #
        [0,0,0,0,0], #
        [1,1,1,1,1], #█████
        [0,1,1,1,0], # ███
        [0,0,1,0,0]  #  █
    ],
    [    # Big Square
        [0,0,0,0,0], #
        [1,1,1,1,0], #████
        [1,1,1,1,0], #████
        [1,1,1,1,0], #████
        [1,1,1,1,0]  #████
    ],
    [    # Horinzontal J
        [0,0,0,0,0], #
        [0,0,0,0,0], #
        [0,0,0,0,0], #
        [1,1,1,1,0], #████
        [0,0,0,1,0]  #   █
    ],
    [    # Vertical L (Upside-down)
        [0,0,0,0,0], #
        [1,1,0,0,0], #██
        [0,1,0,0,0], # █
        [0,1,0,0,0], # █
        [0,1,0,0,0]  # █
    ],
    [   # Vertical L
        [0,0,0,0,0], #
        [1,0,0,0,0], #█
        [1,0,0,0,0], #█
        [1,0,0,0,0], #█
        [1,1,0,0,0]  #██
    ]
]

# 3x3 Matrix
TRIANGLE_BLOCKS = [
    [   # Horizontal S
        [1,0,0], #█
        [1,1,1], #███
        [0,0,1]  #  █
    ],
    [   # Vertical Z
        [1,1,0], #██
        [0,1,0], # █
        [0,1,1]  # ██
    ],
    [   # Horizontal Z
        [0,0,1], #  █
        [1,1,1], #███
        [1,0,0]  #█
    ],
    [   # Vertical S
        [0,1,1], # ██
        [0,1,0], # █
        [1,1,0]  #██
    ],
    [   # Right Oblique
        [0,0,1], #  █
        [0,1,0], # █
        [1,0,0]  #█
    ],
    [   # Left Oblique
        [1,0,0], #█
        [0,1,0], # █
        [0,0,1]  #  █
    ],
    [   # Vertical I
        [1,0,0], #█
        [1,0,0], #█
        [1,0,0]  #█
    ],
    [   # Horizontal I
        [0,0,0], #
        [0,0,0], #
        [1,1,1]  #███
    ],
    [   # Vertical Small I
        [0,0,0], #
        [1,0,0], #█
        [1,0,0]  #█
    ],
    [   # Horizontal Small I
        [0,0,0], #
        [0,0,0], #
        [1,1,0]  #██
    ],
    [   # Star
        [0,1,0], # █
        [1,1,1], #███
        [0,1,0]  # █
    ]
]

if __name__ == '__main__':

    def test_blockset(blockset: list[list[list[int]]], name: str) -> None:
        '''
        Verifies that a set of blocks is valid.
        A set of block is valid if:
         - Every block is stored in a square matrix
         - Every block has the same size
         - Every block is stored in the matrix from the bottom left corner.
            (i.e. the first column and the last row of the matrix must contain at least one `1`)
        
        :param blockset: A list of blocks.
        :param name: The name of the blockset.
        '''
        print(f'Testing {name}...')
        previous_size = (len(blockset[0]), len(blockset[0][0]))
        for i in range(len(blockset)):
            block = blockset[i]
            # Size checks
            size = (len(block), len(block[0]))
            assert len(block) == len(block[0]), f'Block #{i} is not square'
            assert previous_size == size, \
                f'Block #{i} has a non consistent size. Expected {previous_size}, got {size}'
            previous_size = size
            # Corner checks
            first_column = [row[0] for row in block]
            last_row = block[-1]
            assert 1 in first_column and 1 in last_row, \
                f'Block #{i} is not stored from the bottom left corner'
        print('✔ OK')
    
    def line(block_width, block_count, separator):
        '''
        Generates a separator line to showcase a set of blocks.

        :param block_width: The width of a block in the blockset.
        :param block_count: The number of blocks displayed in a row.
        :param separator: The separator character.
        :return: A string containing the separator line.
        '''
        return separator.join(['═' * block_width for _ in range(block_count)])

    def showcase_blockset(blockset: list[list[list[int]]], name: str, bpr = 10) -> None:
        '''
        Showcases a set of blocks in the console.

        :param blockset: The set of blocks to showcase.
        :param name: The name of the blockset.
        :param bpr: The number of blocks to display per row.
        '''
        size = (len(blockset[0][0]), len(blockset[0]))
        print(f'== {name} set - {size[0]}x{size[1]} ==')
        
        for i in range(0, len(blockset) - bpr + 1, bpr):
            blocks = blockset[i:i+bpr]
            ###################### Title Row ######################
            print('╔' + line(size[0], bpr, '╦') + '╗')
            print('║', end='')
            for j in range(bpr):
                id = '#' + str(i + j)
                print(id + ' ' * (size[0] - len(id)), end='║')
            print('\n╠' + line(size[0], bpr, '╬') + '╣')
            #######################################################

            ###################### Block Rows #####################
            # Renders each row of the blocks
            for j in range(len(blocks[0])):
                    for k in range(bpr):
                        print('║', end='')
                        # This map replaces 0s with `-` and 1s with `█` 
                        # in the current row of the current block
                        row = map(lambda x: '█' if x else '-', blocks[k][j])
                        print(''.join(row), end='')
                    print('║')
            #######################################################
                
            ###################### Bottom Line ####################
            print('╚' + line(size[0], bpr, '╩') + '╝')
            #######################################################
    
    test_blockset(COMMON_BLOCKS, 'Common blocks')
    test_blockset(TRIANGLE_BLOCKS, 'Triangle blocks')
    test_blockset(DIAMOND_BLOCKS, 'Diamond blocks')
    showcase_blockset(COMMON_BLOCKS, 'Common blocks')
    showcase_blockset(TRIANGLE_BLOCKS, 'Triangle blocks')
    showcase_blockset(DIAMOND_BLOCKS, 'Diamond blocks')
