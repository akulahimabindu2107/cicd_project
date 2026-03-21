from etl_processing import CustomerProcessor, load_customers


def test_filter_active():
    data = load_customers()
    processor = CustomerProcessor(data)
    active = processor.filter_active_customers()
    assert len(active) == 3


def test_total_revenue():
    data = load_customers()
    processor = CustomerProcessor(data)
    revenue = processor.total_revenue()
    assert revenue == 37000


def test_discount_senior():
    processor = CustomerProcessor([])
    customer = {"age": 65, "spend": 2000}
    discount = processor.calculate_discount(customer)
    assert discount == 0.20


def test_discount_high_spender():
    processor = CustomerProcessor([])
    customer = {"age": 40, "spend": 12000}
    discount = processor.calculate_discount(customer)
    assert discount == 0.15