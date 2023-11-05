from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Line

class MyWidget(Widget):
	def on_touch_down(self, touch):
		self.line = Line(points=(touch.x, touch.y))
		self.canvas.add(self.line)

	def on_touch_move(self, touch):
		self.line.points += (touch.x, touch.y)

class MyselfApp(App):

	def build(self):
		return MyWidget()

if __name__ == '__main__':
    MyselfApp().run()
