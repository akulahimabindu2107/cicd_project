import random


def load_customers():
    return [
        {"name": "Ravi", "age": 65, "spend": 12000, "status": "active"},
        {"name": "Sita", "age": 45, "spend": 7000, "status": "inactive"},
        {"name": "John", "age": 30, "spend": 3000, "status": "active"},
        {"name": "Meena", "age": 70, "spend": 15000, "status": "active"},
    ]


class CustomerProcessor:

    def __init__(self, data):
        self.data = data

    def filter_active_customers(self):
        return [c for c in self.data if c["status"] == "active"]

    def total_revenue(self):
        return sum(c["spend"] for c in self.data)

    def calculate_discount(self, customer):
        if customer["age"] >= 60:
            return 0.20
        elif customer["spend"] >= 10000:
            return 0.15
        elif customer["spend"] >= 5000:
            return 0.10
        else:
            return 0.05

    def enrich_customer_data(self):
        enriched = []
        for c in self.data:
            discount = self.calculate_discount(c)
            loyalty_score = random.randint(10, 100)

            new_record = c.copy()
            new_record["discount"] = discount
            new_record["loyalty_score"] = loyalty_score

            enriched.append(new_record)

        return enriched


def run_etl():
    data = load_customers()
    processor = CustomerProcessor(data)

    active = processor.filter_active_customers()
    enriched = processor.enrich_customer_data()
    revenue = processor.total_revenue()

    return active, enriched, revenue


if __name__ == "__main__":
    active, enriched, revenue = run_etl()

    print("Active Customers:", active)
    print("Enriched Data:", enriched)
    print("Total Revenue:", revenue)