#coding=utf-8
__author__ = 'jesse'
import pyglet

window = pyglet.window.Window()
label = pyglet.text.Label(u'你好,世界',
                          font_name='Microsoft Yahei',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')
@window.event
def on_draw():
    window.clear()
    label.draw()

pyglet.app.run()