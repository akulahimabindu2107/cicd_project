from etl_processing import CustomerProcessor, load_customers, run_etl


def test_filter_active_customers():
    data = load_customers()
    processor = CustomerProcessor(data)
    active = processor.filter_active_customers()
    assert len(active) == 3


def test_filter_no_active_customers():
    data = [
        {"name": "A", "age": 30, "spend": 2000, "status": "inactive"},
        {"name": "B", "age": 40, "spend": 3000, "status": "inactive"},
    ]
    processor = CustomerProcessor(data)
    active = processor.filter_active_customers()
    assert len(active) == 0


def test_total_revenue_calculation():
    data = load_customers()
    processor = CustomerProcessor(data)
    revenue = processor.total_revenue()
    assert revenue == 37000


def test_total_revenue_empty():
    processor = CustomerProcessor([])
    assert processor.total_revenue() == 0


def test_discount_for_senior_customer():
    processor = CustomerProcessor([])
    customer = {"age": 65, "spend": 2000}
    assert processor.calculate_discount(customer) == 0.20


def test_discount_for_high_spender():
    processor = CustomerProcessor([])
    customer = {"age": 40, "spend": 12000}
    assert processor.calculate_discount(customer) == 0.15


def test_discount_for_medium_spender():
    processor = CustomerProcessor([])
    customer = {"age": 40, "spend": 6000}
    assert processor.calculate_discount(customer) == 0.10


def test_discount_for_low_spender():
    processor = CustomerProcessor([])
    customer = {"age": 25, "spend": 1000}
    assert processor.calculate_discount(customer) == 0.05


def test_enrich_customer_data_adds_fields():
    data = load_customers()
    processor = CustomerProcessor(data)
    enriched = processor.enrich_customer_data()

    assert "discount" in enriched[0]
    assert "loyalty_score" in enriched[0]


def test_enrich_customer_data_length():
    data = load_customers()
    processor = CustomerProcessor(data)
    enriched = processor.enrich_customer_data()
    assert len(enriched) == len(data)


def test_run_etl_output():
    active, enriched, revenue = run_etl()

    assert len(active) == 3
    assert revenue == 37000
    assert isinstance(enriched, list)