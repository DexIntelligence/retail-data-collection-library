# Configuration

Central configuration management for research parameters, geographic data, and system settings.

## Master Research List Integration

Industry research priorities are determined by `RESEARCH-MASTER-LIST.md` in the project root. Configuration for each industry should be created when that industry appears at the top of the master list and is marked as `[initiated]`.

## Configuration Files

### `/industries/`
Industry-specific research configuration and metadata.
- **Purpose**: Define research scope, success criteria, and industry-specific patterns
- **Usage**: Initialize new industry research with proper parameters
- **Format**: JSON files with standardized schema

### `/provinces/`
Canadian provincial data for geographic validation and market analysis.
- **Purpose**: Coordinate boundaries, postal code patterns, market characteristics
- **Usage**: Geographic validation, market size estimation, regional adaptation
- **Format**: JSON files with geographic and demographic data

### `settings.py`
Global system configuration and rate limiting parameters.
- **Purpose**: API rate limits, timeout settings, quality thresholds
- **Usage**: Ensure responsible web scraping and API usage
- **Maintenance**: Update based on discovered rate limits and best practices

## Adding New Configuration

### New Industry
1. Check `RESEARCH-MASTER-LIST.md` for next industry to configure
2. Copy template from `industries/template.json`
3. Name file after industry from master list (e.g., `banking.json`)
4. Define industry-specific search terms and validation rules
5. Set expected market characteristics and geographic scope
6. Configure industry-specific source discovery parameters

### Province Updates
Provincial data is relatively static but may need updates for:
- Postal code pattern changes
- Municipal boundary updates  
- Market characteristic evolution
- New regional retail patterns

## Configuration Schema
All configuration files follow standardized JSON schemas for programmatic access and validation.