from timeit import timeit

class InOperatorTester:
    def __init__(self, iterations=1000, repeats=10000):
        self.iterations = iterations
        self.repeats = repeats

    def test_tuple(self):
        for i in range(self.iterations):
            if i in (314, 628):
                pass

    def test_list(self):
        for i in range(self.iterations):
            if i in [314, 628]:
                pass

    def test_set(self):
        for i in range(self.iterations):
            if i in {314, 628}:
                pass

    def test_logic(self):
        for i in range(self.iterations):
            if i == 314 or i == 628:
                pass

    def run_all_tests(self):
        tests = [
            ("Tuple ( )", self.test_tuple),
            ("List  [ ]", self.test_list),
            ("Set   { }", self.test_set),
            ("Logic  or", self.test_logic),
        ]
        
        print(f"{'Método':<12} | {'Tiempo (s)':<10}")
        print("-" * 25)
        
        for name, func in tests:
            result = timeit(func, number=self.repeats)
            print(f"{name:<12} | {result:.5f}")

# Uso de la clase
tester = InOperatorTester()
tester.run_all_tests()
