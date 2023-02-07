import pygame as pg


class Visuliser:
    def __init__(self, window_size, graph_size, nodes) -> None:
        self.window_size = window_size
        self.graph_size = graph_size
        self.nodes = nodes
        self.path = []
        self.path_options = ('', {})

        pg.init()
        self.window = pg.display.set_mode(window_size)
        pg.display.set_caption("Traveling salesman symulator")

        self.running = True

    def set_path(self, path):
        self.path = path

    def mainloop(self):
        while self.running:

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False

            self.window.fill((0, 0, 0))
            self.draw_path()
            # self.draw_options()
            self.draw_nodes()
            pg.display.update()

    def draw_nodes(self):
        for node in self.nodes:
            pg.draw.circle(
                self.window, center=self.convert_point(
                    self.nodes[node]), radius=5, color=(255, 0, 0))

    def set_options(self, start, options):
        self.path_options = (start, options)

    def draw_options(self):
        if self.path_options[0] not in self.path or True:
            start = self.convert_point(self.nodes[self.path_options[0]])
            for option in self.path_options[1]:
                end = self.convert_point(self.nodes[option[0]])

                pg.draw.aaline(self.window, color=(
                    100, 100, 100), start_pos=start, end_pos=end)

    def draw_path(self):
        path = [self.convert_point(self.nodes[node]) for node in self.path]

        if len(path) > 2:
            pg.draw.lines(self.window, color=(255, 255, 255),
                          closed=False, points=path, width=5)
        elif len(path) == 2:
            pg.draw.aaline(self.window, color=(255, 255, 255),
                           start_pos=path[0], end_pos=path[1])

    def convert_point(self, point):
        x = point[0]
        y = point[1]
        new_x = (x / self.graph_size[0]) * self.window_size[0]
        new_y = (y / self.graph_size[1]) * self.window_size[1]
        return (new_x, new_y)
