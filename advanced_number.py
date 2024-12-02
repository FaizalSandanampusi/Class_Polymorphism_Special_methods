class AdvancedNumber:
    def __init__(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be an integer or float.")
        self.value = value

    # String representations
    def __str__(self):
        return f"Value: {self.value}"
    
    def __repr__(self):
        return f"AdvancedNumber({self.value})"

    # Arithmetic operations
    def __add__(self, other):
        return AdvancedNumber(self.value + self._extract_value(other))

    def __sub__(self, other):
        return AdvancedNumber(self.value - self._extract_value(other))

    def __mul__(self, other):
        return AdvancedNumber(self.value * self._extract_value(other))

    def __truediv__(self, other):
        if self._extract_value(other) == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return AdvancedNumber(self.value / self._extract_value(other))

    def __mod__(self, other):
        return AdvancedNumber(self.value % self._extract_value(other))

    # Comparison operations
    def __eq__(self, other):
        return self.value == self._extract_value(other)

    def __ne__(self, other):
        return self.value != self._extract_value(other)

    def __lt__(self, other):
        return self.value < self._extract_value(other)

    def __le__(self, other):
        return self.value <= self._extract_value(other)

    def __gt__(self, other):
        return self.value > self._extract_value(other)

    def __ge__(self, other):
        return self.value >= self._extract_value(other)

    # Hashing
    def __hash__(self):
        return hash(self.value)

    # Boolean conversion
    def __bool__(self):
        return self.value != 0

    # Callable behavior
    def __call__(self):
        return self.value ** 2

    # Custom formatting
    def __format__(self, format_spec):
        if format_spec == "#x" and isinstance(self.value, int):
            return format(self.value, "#x")
        elif format_spec.endswith("f"):
            return format(self.value, format_spec)
        else:
            return format(self.value, format_spec)

    # Destructor
    def __del__(self):
        print(f"AdvancedNumber with value {self.value} is being destroyed.")

    # Utility method for value extraction
    def _extract_value(self, other):
        if isinstance(other, AdvancedNumber):
            return other.value
        elif isinstance(other, (int, float)):
            return other
        else:
            raise TypeError("Operand must be an AdvancedNumber, int, or float.")
