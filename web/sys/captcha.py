# coding=utf-8

import random
from PIL import Image, ImageFont, ImageDraw


class Captcha:
    def __init__(self, width, height, ch_len=5, font_path='C:\Windows\Fonts\Verdanaz.ttf', font_size=28):
        self.width = width
        self.height = height
        self.ch_len = ch_len
        self.font_path = font_path
        self.font_size = font_size
        self.code = []

    def _verify_code(self):
        img = Image.new(mode='RGBA', size=(self.width, self.height), color='white')
        draw = ImageDraw.Draw(img)
        # 图片中文本的颜色范围
        text_rgb_r = [x for x in range(115, 151)]
        text_rgb_g = [x for x in range(140, 206)]
        text_rgb_b = [x for x in range(95, 125)]
        # 图片中干扰圆圈的颜色范围
        arc_rgb_r = [x for x in range(160, 241)]
        arc_rgb_g = [x for x in range(190, 231)]
        arc_rgb_b = [x for x in range(185, 236)]

        # 写干扰圆圈
        for i in range(8):
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            draw.arc((x, y, x + random.choice([x for x in range(8, 14)]), y + random.choice([x for x in range(8, 14)])),
                     0, 360,
                     fill=(random.choice(arc_rgb_r), random.choice(arc_rgb_g), random.choice(arc_rgb_b), 200),
                     width=random.choice([2, 3, 4]))

        # 写文字
        font = ImageFont.truetype(self.font_path, self.font_size)
        i = 0
        for code_str in self.code:
            h = random.randint(0, 8)
            draw.text([i * self.width / self.ch_len, h], str(code_str), font=font,
                      fill=(random.choice(text_rgb_r), random.choice(text_rgb_g), random.choice(text_rgb_b), 255))
            i += 1

        return img, ''.join([str(x) for x in self.code])

    def _random_verify_code(self):
        num_code = [x for x in range(0, 10)]
        str_code = [x for x in range(65, 91)]
        num_code_times = random.choice([x for x in range(self.ch_len)])
        for x in range(num_code_times):
            self.code.append(random.choice(num_code))
        for x in range(self.ch_len-num_code_times):
            self.code.append(chr(random.choice(str_code)))

    def render_code(self):
        self._random_verify_code()
        return self._verify_code()

