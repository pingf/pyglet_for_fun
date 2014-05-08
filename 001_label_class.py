#coding=utf-8
__author__ = 'jesse'
import pyglet


class SimpleWindow(pyglet.window.Window):
    def __init__(self,name):
        super(SimpleWindow,self).__init__(caption=name)
        self.label = pyglet.text.Label(u'你好,世界',
                                  font_name='Microsoft Yahei',
                                  font_size=36,
                                  x=self.width//2, y=self.height//2,
                                  anchor_x='center', anchor_y='center')
        #self.event(self.on_draw)()
        self.push_handlers(self.on_draw)
    def on_draw(self):
        self.clear()
        self.label.draw()


window1 = SimpleWindow('window1')
window2 = SimpleWindow('window2')
pyglet.app.run()