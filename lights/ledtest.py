import board
import neopixel
pixels = neopixel.NeoPixel(board.D18, 30) # Raspberry Pi wiring!
pixels.fill((0, 0, 50))
