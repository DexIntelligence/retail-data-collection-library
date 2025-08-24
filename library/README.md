# Research Library

This directory contains the core knowledge base for retail data collection, organized for incremental growth and easy maintenance.

## Directory Structure

### `/source_intelligence/`
Industry-specific data source profiles and access documentation.
- **Purpose**: Complete technical profiles for ALL data sources (brands, aggregators, government, directories) by industry
- **Growth Pattern**: Add industries based on `RESEARCH-MASTER-LIST.md` priority order
- **Maintenance**: Regular source availability testing and access method updates

### `/extraction_patterns/`
Reusable technical patterns for data extraction across industries.
- **api_templates/**: GraphQL/REST API query templates and response handlers
- **html_selectors/**: CSS/XPath selector sets for HTML scraping
- **pagination_strategies/**: Methods for handling paginated results
- **authentication_methods/**: OAuth, API key, and session management patterns

### `/geographic_intelligence/`
Regional market insights and geographic validation data.
- **Purpose**: Provincial market analysis, boundary validation, language patterns
- **Usage**: Geographic validation, market coverage analysis, regional adaptation

### `/quality_benchmarks/`
Expected results and validation standards for quality assurance.
- **store_count_estimates/**: Expected store counts per chain/province for validation
- **data_quality_profiles/**: Confidence score distributions and completeness metrics
- **geographic_boundaries/**: Coordinate validation ranges and postal code patterns

## Library Usage

### Adding a New Industry
1. Check `RESEARCH-MASTER-LIST.md` for next industry priority
2. Create industry directory in `source_intelligence/`
3. Research and document ALL data sources (brands, aggregators, government)
4. Extract common access patterns to `extraction_patterns/`
5. Establish source reliability benchmarks
6. Update master list with completion status

### Querying the Library
The library is designed to be programmatically accessible through standardized JSON schemas and file naming conventions.

### Maintenance Schedule
- **Daily**: Automated endpoint health checks
- **Weekly**: Pattern success rate analysis
- **Monthly**: Complete industry validation
- **Quarterly**: Deep pattern library review