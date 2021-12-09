#!/usr/bin/env python3
import json
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont


class Render:

    @staticmethod
    def colors() -> int:
        c = plt.cm.tab20(np.linspace(0, 1, 20))
        c = c*255
        return c.astype(int)

    
    @staticmethod
    def render_line(
        img, 
        joints, 
        f: str, 
        s: str, 
        color:int
    ):
        if f in joints and s in joints:
            img.line(
                (joints[f][0], joints[f][1], joints[s][0], joints[s][1]), 
                fill=tuple(color),
                width=6)
    

    @staticmethod
    def render(
        img_path: str, 
        jsn: str,
        save_img_path: str
    ):
        img = Image.open(img_path)
        draw = ImageDraw.Draw(img)

        data = json.loads(jsn)

        j = data[0]

        colors = Render.colors()

        Render.render_line(draw, j, 'left_hip', 'left_shoulder', colors[0])
        Render.render_line(draw, j, 'left_hip', 'left_knee', colors[1])
        Render.render_line(draw, j, 'left_knee', 'left_ankle', colors[2])
        Render.render_line(draw, j, 'left_shoulder', 'left_elbow', colors[3])
        Render.render_line(draw, j, 'left_elbow', 'left_wrist', colors[4])
        Render.render_line(draw, j, 'left_shoulder', 'right_shoulder', colors[5])
        Render.render_line(draw, j, 'left_hip', 'right_hip', colors[6])
        Render.render_line(draw, j, 'right_hip', 'right_shoulder', colors[7])
        Render.render_line(draw, j, 'right_hip', 'right_knee', colors[8])
        Render.render_line(draw, j, 'right_knee', 'right_ankle', colors[9])
        Render.render_line(draw, j, 'right_shoulder', 'right_elbow', colors[10])
        Render.render_line(draw, j, 'right_elbow', 'right_wrist', colors[11])

        img = img.save(save_img_path)
