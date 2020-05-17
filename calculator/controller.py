import os
import json
from datetime import datetime
from calculator.decorators import show_code_author
from collections import namedtuple
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
            results = json.load(file)
        return results

    def add_result(self, result, operation):
        self.results[operation] = result
        with open(self.path, "w+") as file_json:
            json.dump(self.results, file_json)

    @show_code_author
    def action(self, real1: int, imag1: int, real2: int, imag2: int, operator: str):
        try:
            result = eval(f'ComplexNumber({real1}, {imag1}){operator}ComplexNumber({real2}, {imag2})')
            operation = f"{real1}{'+' if int(imag1) > 0 else '-'}{imag1}j {operator} {real2}{'+' if int(imag2) > 0 else '-'}{imag2}j"
            result_with_tuple = self.create_tuple(result)
            self.add_result(result_with_tuple, operation)
            return result
        except ValueError:
            print("Wrong input")

    def create_tuple(self, result: complex):
        Result_with_date = namedtuple('Result_with_date', 'result date')
        return tuple(Result_with_date(str(result), datetime.now().strftime("%d/%m/%Y")))

    def sort_results(self, method="imag"):
        if method == "imag":
            return dict(sorted(self.results.items(), key=lambda x: eval(x[1][0]).imag))
        elif method == "real":
            return dict(sorted(self.results.items(), key=lambda x: eval(x[1][0]).real))
        elif method == "date":
            return dict(sorted(self.results.items(),
                               key=lambda x: datetime.strptime(x[1][1],"%d/%m/%Y").strftime("%Y-%m-%d")))

    def filer_results(self, operator: str, number: int, method="imag"):
        if method == "imag":
            return dict(filter(lambda x:  eval(f'complex(x[1][0]).imag {operator} {number}'), self.results.items()))
        elif method == "real":
            return dict(filter(lambda x:  eval(f'complex(x[1][0]).real {operator} {number}'), self.results.items()))




