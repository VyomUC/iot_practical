import time
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas

# Initialize LED matrix
serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=1, block_orientation=90, rotate=0)

# Define patterns for different emojis
smiley_face = [
    0b00111100,
    0b01000010,
    0b10100101,
    0b10000001,
    0b10100101,
    0b10011001,
    0b01000010,
    0b00111100
]

# Corrected sad face emoji
sad_face = [
    0b00111100,
    0b01000010,
    0b10100101,
    0b10000001,
    0b10011001,
    0b10100101,
    0b01000010,
    0b00111100
]

# Additional emoji patterns
heart = [
    0b00000000,
    0b01100110,
    0b11111111,
    0b11111111,
    0b01111110,
    0b00111100,
    0b00011000,
    0b00000000
]

surprised_face = [
    0b00111100,
    0b01000010,
    0b10000001,
    0b10011001,
    0b10000001,
    0b10000001,
    0b01000010,
    0b00111100
]

wink_face = [
    0b00111100,
    0b01000010,
    0b10100101,
    0b10000001,
    0b10111101,
    0b10000001,
    0b01000010,
    0b00111100
]

# Rotate pattern by 90 degrees clockwise
def rotate_pattern_90_clockwise(pattern):
    return [list(i) for i in zip(*pattern[::-1])]

# Function to display an emoji on the LED matrix
def display_emoji(device, pattern):
    pattern = rotate_pattern_90_clockwise(pattern)  # Rotate the pattern
    with canvas(device) as draw:
        for y, row in enumerate(pattern):
            for x, col in enumerate(row):
                draw.point((x, y), fill="white" if col else None)

# Convert patterns to list of lists
emoji_patterns = [smiley_face, sad_face, heart, wink_face]
emoji_patterns = [[[int(bit) for bit in bin(row)[2:].zfill(8)] for row in emoji] for emoji in emoji_patterns]

# Main loop to cycle through emojis
while True:
    for pattern in emoji_patterns:
        display_emoji(device, pattern)
        time.sleep(5)  # Display each emoji for 5 seconds
