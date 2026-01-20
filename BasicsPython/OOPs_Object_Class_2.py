class APICallCounter:
    def __init__(self):
        self.count = 0

    def hit(self):
        self.count += 1
        return self.count
api_counter = APICallCounter()

api_counter.hit()
api_counter.hit()
api_counter.hit()
api_counter.hit()
# print(api_counter.count)   # 4



def calling():
    api_called = 0

    def api_call():
        nonlocal api_called
        api_called += 1
        return api_called

    return api_call

f = calling()
# print(f())
# print(f())
# print(f())



class RateOfInterest:
    default_interest_rate = 0.05
    def __init__(self, name, loan_amount):
        self.name = name
        self.loan_amount = loan_amount

    def CalculateRateOfInterest(self, inter):
        print(f"Hi {self.name}!, your loan amount is \"{self.loan_amount}\" and interest is \"{self.loan_amount*self.default_interest_rate}\" per month with a rate of interest at \"{self.default_interest_rate}\"")
        print(f"Hi {self.name}!, your loan amount is \"{self.loan_amount}\" and interest is \"{self.loan_amount*inter}\" per month with a rate of interest at \"{inter}\"")

person1 = RateOfInterest("Sagar", 50000)
person1.CalculateRateOfInterest(inter=person1.default_interest_rate)
person1.default_interest_rate = 0.08
person1.CalculateRateOfInterest(0.1)