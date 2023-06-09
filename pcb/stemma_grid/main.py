from kicad.units import *

import sys
sys.path.insert(0,"/Applications/KiCad/KiCad.app/Contents/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages")

# import pcbnew

# importlib.reload(stemma_grid); stemma_grid.stemma_grid(pcb, 2, 1); pcbnew.Refresh()

RIGHT = (180, 360)
LEFT = (0, 180)
UP = (90, 270)
DOWN = (270, 90)
FULL = (0, 360)

pattern = {
    (0, 0): DOWN,
    (0, 1): RIGHT,
    (0, 2): LEFT,
    (1, 0): UP,
    (1, 1): FULL,
    (1, 2): DOWN,
    (2, 0): RIGHT,
    (2, 1): LEFT,
    (2, 2): UP,
}
CORNERS = (
    (0, 0, 1, 1, 270, 360),
    (0, 1, 1, -1, 180, 270),
    (1, 0, -1, 1, 0, 90),
    (1, 1, -1, -1, 90, 180)
)

def _round(values):
    return [round(v, 2) for v in values]

def stemma_grid(pcb, rows: int, cols: int, pos=(1, 1)):
    """blah"""
    height = 0.6 * rows
    deciheight = 6 * rows
    width = 0.6 * cols
    deciwidth = 6 * cols
    # Corners
    for xmul, ymul, xshift, yshift, start, end in CORNERS:
        x = pos[0] + xshift * 0.05 + (xmul * width)
        y = pos[1] + yshift * 0.05 + (ymul * height)
        pcb.add_arc(inch_to_mm(_round((x, y))), inch_to_mm(0.1 / 2), start, end, layer="Edge.Cuts")

    # logo = pcbnew.FootprintLoad("/home/tannewt/.local/share/kicad/7.0/footprints/adafruit.pretty", "ADAFRUIT_2.5MM")
    
    # logo_anchor = inch_to_mm([pos[0] + 0.01, pos[1] + 0.645])
    # logo.SetPosition(kicad.Point.native_from(logo_anchor))
    # pcb._obj.Add(logo)

    anchor = inch_to_mm([pos[0] + 0.325, pos[1] + 0.6])
    pcb.add_text(anchor, f"{rows}x{cols} v2", layer="F.Silkscreen", size=1.5, thickness=0.3)

    # Horizontal edges and silk grid
    for y in range(0, deciheight + 1):
        if y % 6 != 0:
            continue
        for layer in ["Edge.Cuts", "F.Silkscreen", "B.Silkscreen"]:
            trim = 0.05
            trim_left = 0
            edge = y == 0 or y == deciheight
            if edge and layer != "Edge.Cuts":
                continue

            if not edge and layer == "Edge.Cuts":
                continue

            if y == 6 and layer == "F.Silkscreen":
                trim_left = 0.5
                if cols == 1:
                    continue
            start = inch_to_mm(_round([pos[0] + trim + trim_left, pos[1] + y / 10]))
            end = inch_to_mm(_round([pos[0] + width - trim, pos[1] + y / 10]))
            pcb.add_line(start, end, layer=layer)

    # Vertical edges and silk grid
    for x in range(0, int(deciwidth) + 1):
        if x % 6 != 0:
            continue
        trim = 0.05
        if x == 0 or x == deciwidth:
            layers = ["Edge.Cuts"]
        else:
            # Do silk and copper to give more of a tactile feel
            layers = ["F.Silkscreen", "B.Silkscreen", "F.Cu", "B.Cu"]
        start = inch_to_mm(_round([pos[0] + x / 10, pos[1] + trim]))
        end = inch_to_mm(_round([pos[0] + x / 10, pos[1] + height - trim]))
        for layer in layers:
            pcb.add_line(start, end, layer=layer)

    # Coordinates
    for r in range(rows):
        for c in range(cols):
            anchor = _round(inch_to_mm([pos[0] + 0.3 + 0.6 * c, pos[1] + 0.3 + 0.6 * r + 0.1]))
            pcb.add_text(anchor, f"{r},{c}", layer="F.Silkscreen")
            pcb.add_text(anchor, f"{r},{c}", mirrored=True, layer="B.Silkscreen")

    for x in range(0, deciwidth):
        for y in range(0, deciheight):
            start, end = pattern[((y // 2) % 3, (x // 2) % 3)]
            shift = (0.1, 0.1)
            if x % 2 != 0 or y % 2 != 0:
                direction = pattern[((y // 2) % 3, (x // 2) % 3)]
                if direction == RIGHT and y % 2 == 0:
                    start = _round(inch_to_mm([pos[0] + shift[0] + x / 10 - 0.1, pos[1] + shift[1] + y / 10 - 0.05]))
                    end = _round(inch_to_mm([pos[0] + shift[0] + x / 10 + 0.1, pos[1] + shift[1] + y / 10 - 0.05]))
                    pcb.add_line(start, end, layer="Edge.Cuts")
                    start = _round(inch_to_mm([pos[0] + shift[0] + x / 10 - 0.1, pos[1] + shift[1] + y / 10 + 0.05]))
                    end = _round(inch_to_mm([pos[0] + shift[0] + x / 10 + 0.1, pos[1] + shift[1] + y / 10 + 0.05]))
                    pcb.add_line(start, end, layer="Edge.Cuts")
                    continue
                elif direction == DOWN and x % 2 == 0:
                    start = _round(inch_to_mm([pos[0] + shift[0] + x / 10 - 0.05, pos[1] + shift[1] + y / 10 - 0.1]))
                    end = _round(inch_to_mm([pos[0] + shift[0] + x / 10 - 0.05, pos[1] + shift[1] + y / 10 + 0.1]))
                    pcb.add_line(start, end, layer="Edge.Cuts")
                    start = _round(inch_to_mm([pos[0] + shift[0] + x / 10 + 0.05, pos[1] + shift[1] + y / 10 - 0.1]))
                    end = _round(inch_to_mm([pos[0] + shift[0] + x / 10 + 0.05, pos[1] + shift[1] + y / 10 + 0.1]))
                    pcb.add_line(start, end, layer="Edge.Cuts")
                    continue
                else:
                    continue
                # pcb.add_circle(round(inch_to_mm([pos[0] + x / 10, pos[1] + y / 10]), 0.04, layer="User.Eco1")
                continue
            center = _round(inch_to_mm([pos[0] + shift[0] + x / 10, pos[1] + shift[1] + y / 10]))
            pcb.add_arc(center, inch_to_mm(0.1 / 2), start, end, layer="Edge.Cuts")

from kicad.pcbnew import board
import pathlib

pcb = board.Board()
stemma_grid(pcb, 10, 10)

path = str(pathlib.Path().resolve()) + 'generated/board.kicad_pcb'
pcb.save(path)