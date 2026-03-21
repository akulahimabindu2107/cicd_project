import csv
import random


class CustomerProcessor:

    def __init__(self, customers):
        self.customers = customers

    def filter_active_customers(self):
        active = []
        for c in self.customers:
            if c.get("status") == "active":
                active.append(c)
        return active

    def calculate_discount(self, customer):
        if customer["age"] > 60:
            return 0.20
        elif customer["spend"] > 10000:
            return 0.15
        elif customer["spend"] > 5000:
            return 0.10
        else:
            return 0.05

    def enrich_customer_data(self):
        enriched = []
        for c in self.customers:
            discount = self.calculate_discount(c)
            c["discount"] = discount
            c["loyalty_score"] = random.randint(1, 100)
            enriched.append(c)
        return enriched

    def total_revenue(self):
        total = 0
        for c in self.customers:
            total = total + c["spend"]
        return total


def load_customers():
    return [
        {"name": "Ravi", "age": 65, "spend": 12000, "status": "active"},
        {"name": "Sita", "age": 45, "spend": 7000, "status": "inactive"},
        {"name": "John", "age": 30, "spend": 3000, "status": "active"},
        {"name": "Meena", "age": 70, "spend": 15000, "status": "active"},
    ]


def run_etl():
    data = load_customers()
    processor = CustomerProcessor(data)

    active = processor.filter_active_customers()
    enriched = processor.enrich_customer_data()
    revenue = processor.total_revenue()

    print("Active Customers:", active)
    print("Enriched Data:", enriched)
    print("Total Revenue:", revenue)


if __name__ == "__main__":
    run_etl()