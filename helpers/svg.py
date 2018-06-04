from bs4 import BeautifulSoup


class SVG(object):
    def __init__(self, svg):
        self.svg = BeautifulSoup(svg, 'html.parser')

    def resize(self, height, width):
        new_svg = self.svg
        new_svg.find('svg')['height'] = height
        new_svg.find('svg')['width'] = width
        return new_svg
