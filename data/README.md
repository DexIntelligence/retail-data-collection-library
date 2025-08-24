# Data Storage

Organized storage for research results, processed data, and final outputs.

## Directory Structure

### `/raw/`
**Unprocessed research results** directly from agents.
- **Purpose**: Store initial research outputs before processing
- **Format**: JSON files with agent metadata and timestamps
- **Naming**: `{agent_type}_{industry}_{timestamp}.json`
- **Retention**: Keep all raw data for research audit trails

### `/processed/`
**Cleaned and standardized research data** ready for library integration.
- **Purpose**: Validated, formatted data meeting library standards
- **Format**: Standardized JSON schemas for programmatic access
- **Naming**: `{industry}_{data_type}_{version}.json`
- **Usage**: Direct integration into library directories

### `/exports/`
**User-friendly research summaries** and reports.
- **Purpose**: Human-readable research reports and summaries
- **Format**: Markdown reports, Excel summaries, JSON API exports
- **Naming**: `{industry}_research_report_{date}.md`
- **Usage**: Documentation, stakeholder communication, research validation

## Data Flow

### Research Pipeline
1. **Agents** → `/raw/` (unprocessed results)
2. **Processing** → `/processed/` (standardized format)
3. **Integration** → `/library/` (permanent storage)
4. **Reporting** → `/exports/` (human consumption)

### Data Lifecycle
- **Raw Data**: Permanent retention for audit and re-processing
- **Processed Data**: Version controlled, previous versions archived
- **Exports**: Generated on-demand, not version controlled
- **Library Integration**: Processed data moves to library, references maintained

### Quality Assurance
All data includes:
- Timestamp and agent version metadata
- Confidence scores and validation flags
- Source attribution and extraction methods
- Quality metrics and success indicators