import math as m
'''
x, y = (float(i) for i in input('座標の入力>> ').split())
angle = float(input('回転角度の入力>> '))
rad = math.radians(angle)
nx = x * math.cos(rad) - y * math.sin(rad)
ny = x * math.sin(rad) + y * math.cos(rad)
print(f'({x}, {y})を{angle}度回転移動: ({nx:.3f}, {ny:.3f})')
'''

'''
x, y = (float(i) for i in input('座標の入力>> ').split())
angle = float(input('回転角度の入力>> '))
rad = m.radians(angle)
nx = x * m.cos(rad) - y * m.sin(rad)
ny = x * m.sin(rad) + y * m.cos(rad)
print(f'({x}, {y})を{angle}度回転移動: ({nx:.3f}, {ny:.3f})')
'''

x, y = (float(i) for i in input('二辺の長さ>> ').split())
angle = float(input('二辺間のの角度(°)>> '))
rad = m.radians(angle)
tr = (1 / 2) * x * y * m.sin(rad)
print(f"三角形の面積: {tr:.3f}")