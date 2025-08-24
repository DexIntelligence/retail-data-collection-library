# Canadian Data Source Research Agents

This directory contains Claude subagent instructions for systematic research and documentation of **CANADIAN** retail data SOURCES (not the data itself).

**CRITICAL**: All agents must focus exclusively on Canadian sources - Canadian government databases, Canadian operations of retail chains, Canadian industry associations, and Canadian aggregators only.

## Master Research List Integration

All agents must consult `RESEARCH-MASTER-LIST.md` in the project root to determine:
- Which industry to research next (top non-completed entry)
- Current research status for each industry
- Priority order established by the user

The master list is the **single source of truth** for research priorities and progress.

## Core Source Research Agents

### `industry-source-discovery`
**Purpose**: Comprehensive discovery of ALL available data sources for an industry
**Input**: Industry category (e.g., "grocery", "pharmacy") and geographic scope (Canada)
**Output**: Complete inventory of data sources including brands, aggregators, directories, and government databases
**Research Focus**: WHERE to find store location data, not the data itself

### `source-technical-profiler`
**Purpose**: Deep technical analysis of how to ACCESS each discovered data source
**Input**: Data source URL and basic information
**Output**: Technical profile documenting access methods, authentication, data formats, and limitations
**Research Focus**: HOW to access the source, API documentation, query parameters, rate limits

### `source-coverage-analyst`
**Purpose**: Analyze what data is AVAILABLE from each source
**Input**: Data source profile and industry context
**Output**: Coverage analysis including chains covered, geographic scope, data freshness, and completeness
**Research Focus**: WHAT data the source provides, coverage gaps, reliability assessment

## Specialized Source Type Agents

### `brand-source-researcher`
**Purpose**: Research official brand and franchise data sources
**Input**: Brand/chain name and industry context
**Output**: Documentation of official store locators, APIs, and franchise directories
**Examples**: Tim Hortons store locator, McDonald's API, Subway franchise portal

### `aggregator-source-researcher`
**Purpose**: Research multi-brand aggregator platforms and directories
**Input**: Industry category and geographic scope
**Output**: Technical profiles of aggregator platforms with access documentation
**Examples**: Yellow Pages, Yelp, Google Places, Foursquare, industry-specific directories

### `government-source-researcher`
**Purpose**: Research government and regulatory data sources
**Input**: Industry category and jurisdiction (federal/provincial/municipal)
**Output**: Government database profiles with access methods and data scope
**Examples**: Business registrations, health inspection databases, liquor licensing, municipal permits

### `commercial-directory-researcher`
**Purpose**: Research commercial and trade directory sources
**Input**: Industry category and business type
**Output**: Commercial platform profiles with subscription/access requirements
**Examples**: Dun & Bradstreet, franchise databases, commercial real estate listings, trade associations

## Agent Coordination for Source Research

### Source Research Workflow
1. **Check Master List** → Review `RESEARCH-MASTER-LIST.md` for next industry
2. **Industry Source Discovery** → Comprehensive inventory of all available sources
3. **Source Type Classification** → Categorize sources (brand, aggregator, government, commercial)
4. **Technical Profiling** → Document access methods for each source
5. **Coverage Analysis** → Assess data availability and gaps
6. **Source Documentation** → Create comprehensive source profiles for library
7. **Update Master List** → Mark industry as completed with date

### Research Output Structure
Each source gets documented with:
- **Source Identification**: Name, URL, type, industry coverage
- **Access Methods**: API endpoints, web interfaces, data downloads
- **Technical Specifications**: Authentication, rate limits, data formats
- **Coverage Details**: Chains included, geographic scope, update frequency
- **Cost & Restrictions**: Free/paid tiers, usage limitations, terms of service

### Source Reliability Hierarchy
1. **Official Brand Sources**: Store locators, franchise portals (most accurate)
2. **Government Databases**: Business registrations, licensing (authoritative)
3. **Major Aggregators**: Yellow Pages, Google Places (comprehensive coverage)
4. **Industry Directories**: Trade associations, specialized databases (industry-specific)
5. **Commercial Platforms**: Real estate, classifieds (supplementary data)

### Library Integration
All researched sources are cataloged in standardized JSON format:
```json
{
  "source_name": "Yellow Pages Canada",
  "source_type": "aggregator",
  "industries_covered": ["grocery", "pharmacy", "restaurants"],
  "access_method": "web_api",
  "api_endpoint": "https://api.yellowpages.ca/...",
  "authentication": "api_key_required",
  "data_coverage": "nationwide",
  "update_frequency": "monthly"
}
```