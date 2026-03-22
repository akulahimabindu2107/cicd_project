from etl_processing import CustomerProcessor, load_customers, run_etl


def test_filter_active_customers():
    data = load_customers()
    processor = CustomerProcessor(data)
    active = processor.filter_active_customers()
    assert len(active) == 3


def test_total_revenue_calculation():
    data = load_customers()
    processor = CustomerProcessor(data)
    revenue = processor.total_revenue()
    assert revenue == 37000


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


def test_run_etl_executes_without_error():
    # This ensures main ETL workflow runs
    run_etl()
    assert True
def test_filter_no_active_customers():
    data = [
        {"name": "A", "age": 30, "spend": 2000, "status": "inactive"},
        {"name": "B", "age": 40, "spend": 3000, "status": "inactive"},
    ]
    processor = CustomerProcessor(data)
    active = processor.filter_active_customers()
    assert len(active) == 0


def test_total_revenue_zero_case():
    processor = CustomerProcessor([])
    assert processor.total_revenue() == 0


def test_enrich_customer_data_length():
    data = load_customers()
    processor = CustomerProcessor(data)
    enriched = processor.enrich_customer_data()
    assert len(enriched) == len(data)


def test_enrich_customer_discount_values():
    data = load_customers()
    processor = CustomerProcessor(data)
    enriched = processor.enrich_customer_data()

    discounts = [c["discount"] for c in enriched]
    assert 0.20 in discounts
    assert 0.15 in discounts or 0.10 in discounts or 0.05 in discounts
def test_run_etl_multiple_times():
    for _ in range(3):
        run_etl()
    assert True


def test_enrich_with_custom_data():
    data = [
        {"name": "X", "age": 80, "spend": 20000, "status": "active"},
        {"name": "Y", "age": 20, "spend": 100, "status": "inactive"},
        {"name": "Z", "age": 55, "spend": 6000, "status": "active"},
    ]
    processor = CustomerProcessor(data)
    enriched = processor.enrich_customer_data()

    assert enriched[0]["discount"] == 0.20
    assert enriched[2]["discount"] == 0.10


def test_total_revenue_large_dataset():
    data = [{"name": str(i), "age": 30, "spend": 1000, "status": "active"} for i in range(20)]
    processor = CustomerProcessor(data)
    assert processor.total_revenue() == 20000