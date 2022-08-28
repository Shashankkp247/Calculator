from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
# Set the size of our app
from kivy.core.window import Window

# Set app size
Window.size = (500, 700)

Builder.load_file('calc.kv')

class CalcGui(Widget):
	def clear(self):
		self.ids.calc_input.text = '0'

	def remove(self):
		latest = self.ids.calc_input.text
		latest = latest[:-1]
		if latest == '':
			self.ids.calc_input.text = '0'
		else:
			self.ids.calc_input.text = latest

	def pos_neg(self):
		pr = self.ids.calc_input.text
		if '-' in pr:
			self.ids.calc_input.text = f'{pr.replace("-", "")}'
		else:
			self.ids.calc_input.text = f'-{pr}'


	def button_press(self, button):
		# Text in calc input
		textbox = self.ids.calc_input.text

		if 'Error' in textbox:
			textbox = ''

		# Check for 0
		if textbox == '0':
			self.ids.calc_input.text = f'{button}'
		else:
			self.ids.calc_input.text = textbox + f'{button}'


	def dot(self):
		pr = self.ids.calc_input.text

		num_list = pr.split("+")


		if '+' in pr and '.' not in num_list[-1]:
			self.ids.calc_input.text = f'{pr}.'
		elif '.' in pr:
			pass
		else:
			self.ids.calc_input.text = f'{pr}.'

	def math_sign(self, sign):
		pr = self.ids.calc_input.text

		ss = '+-x/'

		if pr[len(pr)-1] == sign:
			pass
		elif pr[len(pr)-1] in ss:
			pass 
		else:
			self.ids.calc_input.text = f'{pr}{sign}'


	def equals(self):
		text = self.ids.calc_input.text 

		'''
		# Addition
		if '+' in text:
			nlist = text.split('+')
			answer = 0.0
			# loop thru our list
			for n in nlist:
				answer = answer + float(n)

			self.ids.calc_input.text = str(answer)
		'''
		try:
			ans = eval(text)
			self.ids.calc_input.text = str(ans)
		except:
			self.ids.calc_input.text = 'Error'

class Calculator(App):
	def close_app(self):
		# closing application
		App.get_running_app().stop()
		# removing window
		Window.close()

	def build(self):
		return CalcGui()

if __name__ == '__main__':
	Calculator().run()