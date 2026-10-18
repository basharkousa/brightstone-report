import json
from pathlib import Path

import pytest

from report.exceptions import ReportWriteError
from report.models import ReportSummary
from report.writer import to_json, to_markdown, write_report


@pytest.fixture
def sample_summary() -> ReportSummary:
    """Provide a report summary for writer tests."""
    return ReportSummary(
        total_orders=3,
        total_revenue=2600.0,
        top_products=[("Laptop", 2500.0), ("Mouse", 100.0)],
        top_customers=[("John", 2500.0), ("Emma", 100.0)],
        revenue_by_category=[
            ("Electronics", 2500.0),
            ("Accessories", 100.0),
        ],
    )


def test_to_json(sample_summary: ReportSummary) -> None:
    """Serialize report data into valid JSON."""
    content = to_json(sample_summary)
    # json.loads() converts a JSON string back into Python data
    data = json.loads(content)

    assert data["total_orders"] == 3
    assert data["total_revenue"] == 2600.0
    assert data["top_products"][0] == ["Laptop", 2500.0]


def test_to_markdown(sample_summary: ReportSummary) -> None:
    """Render a report with all required Markdown sections."""
    content = to_markdown(sample_summary)

    assert "## Top 5 Products" in content
    assert "# Brightstone Logistics" in content
    assert "**Total orders:** 3" in content
    assert "**Total revenue:** $2600.00" in content
    assert "## Top 5 Customers" in content
    assert "## Revenue by Category" in content
    assert "| Laptop | $2500.00 |" in content
    assert "| John | $2500.00 |" in content
    assert "| Electronics | $2500.00 |" in content


def test_write_report(tmp_path: Path) -> None:
    """Write report content to a UTF-8 file."""
    output_path = tmp_path / "reports" / "daily.md"

    write_report("# Test Report", output_path)

    assert output_path.exists()
    assert output_path.read_text(encoding="utf-8") == "# Test Report"


def test_write_report_failure(tmp_path: Path) -> None:
    """Convert filesystem writing failures into ReportWriteError."""
    with pytest.raises(ReportWriteError):
        write_report("content", tmp_path)
