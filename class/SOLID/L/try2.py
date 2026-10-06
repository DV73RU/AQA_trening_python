from enum import Enum


class Color:
    red = (127, 0, 0)
    green = (127, 127, 255)
    blue = (0, 255, 0)


rd = Color.red
# print(Color.__dict__)


Color.red = (123,3,3)
print(Color.red)
print(rd)

print(Color.__dict__)