from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class CommunalPaymentApp(App):
    def build(self):
        layout = GridLayout(cols=2, spacing=7, size_hint=(0.5, 0.8), pos_hint={'center_x': 0.35, 'center_y': 0.55})
        labels = ['Содержание жилья', 'Холодная вода', 'Тариф на холодную воду', 'Тариф на х_водоотведение',
                  'Горячая вода', 'Тариф на горячую воду', 'Тариф на г_водоотведение', 'Электричество',
                  'Тариф на электричество', 'Вывоз мусора', 'Домофон', 'Отопление']
        self.inputs = []
        for label in labels:
            input_label = Label(text=label, halign='right')
            layout.add_widget(input_label)
            input_text = TextInput()
            layout.add_widget(input_text)
            self.inputs.append(input_text)
        calculate_button = Button(text='Рассчитать', on_press=self.calculate)
        layout.add_widget(calculate_button)
        self.result_labels = []
        for _ in range(3):
            result_label = Label(text='', halign='right', valign='bottom')
            layout.add_widget(result_label)
            self.result_labels.append(result_label)
        return layout

    def calculate(self, instance):
        values = [float(input_text.text) for input_text in self.inputs]
        electricity = values[7] * values[8]
        hot_water = (values[4] * values[5]) + (values[4] * values[6])
        cold_water = (values[1] * values[2]) + (values[1] * values[3])
        total_cost = values[0] + cold_water + hot_water + electricity + values[9] + values[10] + values[11]
        self.result_labels[0].text = (f'Содержание жилья: {values[0]}\n'
                                      f'Холодная вода: {cold_water}')
        self.result_labels[1].text =(f'/n')
        self.result_labels[2].text =(f'Горячая вода: {hot_water}\n'
                                     f'Электричество: {electricity}\n'
                                     f'Общая стоимость: {total_cost}')

if __name__ == '__main__':
    CommunalPaymentApp().run()