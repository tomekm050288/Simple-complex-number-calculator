import os
import json
from calculator.decorators import show_code_author
from calculator.calc import ComplexNumber



class Controller:

    def __init__(self):
        self.path = os.path.join(os.path.dirname(__file__), "results.json")
        self.results = self.load_results()

    def load_results(self):
        if not os.path.exists(self.path):
            with open(self.path, "w") as file:
                file.write("{}")
        with open(self.path) as file:
            rank = json.load(file)
        return rank

    def add_result(self, result, operation):
        self.results[operation] = result
        with open(self.path, "w+") as file_json:
            json.dump(self.results, file_json)

    @show_code_author
    def action(self, real1: str, imag1: str, real2: str, imag2: str, operator: str):
        result = eval(f'ComplexNumber({real1}, {imag1}){operator}ComplexNumber({real2}, {imag2})')
        operation = f"{real1}{'+' if int(imag1) > 0 else '-'}{imag1}j {operator} {real2}{'+' if int(imag2) > 0 else '-'}{imag2}j"
        self.add_result(str(result), operation)
        return result


    def sort_results(self):
        self.results = sorted(self.results.items(), key=lambda x: eval(x[1]).imag)
        return dict(self.results)

    def filer_results(self, number):
        filtr_dict = filter(lambda x:  eval(x[1]).imag > number, self.results.items())
        return filtr_dict




controller = Controller()
print(controller.action("1", "2", "4", "5", "+"))

# print(controller.sort_results())

