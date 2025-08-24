# Agent Execution Queue

## Current Industry: Banking
**Status**: Phase 1 - Discovery COMPLETE, Ready for Phase 2

## Sequential Workflow Phases

### Phase 1: Source Discovery ✅
- **Agent**: `industry-source-discovery`
- **Status**: COMPLETE
- **Output**: `data/raw/banking_source_inventory_[timestamp].json`
- **Next**: Phase 2 ready to start

### Phase 2: Technical Profiling ⏳
- **Agent**: `source-technical-profiler`
- **Status**: READY TO START (corrected scope)
- **Prerequisites**: Phase 1 complete ✅
- **Input**: Source inventory from Phase 1
- **Focus**: ALL discovered sources for comprehensive market coverage
- **Goal**: Complete technical documentation enabling full Canadian banking data collection
- **Next**: Phase 3

### Phase 3: Coverage Analysis ⏳
- **Agent**: `source-coverage-analyst`  
- **Status**: WAITING
- **Prerequisites**: Phase 2 complete
- **Input**: Technical profiles + source inventory
- **Focus**: Comprehensive coverage analysis across ALL sources
- **Next**: Phase 4

### Phase 4: Specialized Analysis (Parallel) ⏳
- **Agent**: `brand-source-researcher`
  - **Status**: WAITING
  - **Prerequisites**: Phase 1 complete
  - **Focus**: Official brand sources only
  
- **Agent**: `government-source-researcher`
  - **Status**: WAITING  
  - **Prerequisites**: Phase 1 complete
  - **Focus**: Government/regulatory sources only
  
- **Agent**: `aggregator-source-researcher`
  - **Status**: WAITING
  - **Prerequisites**: Phase 1 complete
  - **Focus**: Commercial aggregators only
  
- **Agent**: `commercial-directory-researcher`
  - **Status**: WAITING
  - **Prerequisites**: Phase 1 complete
  - **Focus**: Commercial directories only

## Execution Rules
1. **Sequential**: Phases 1-3 must complete in order
2. **Parallel**: Phase 4 agents can run simultaneously after Phase 1
3. **Prerequisites**: Each agent checks for required input files before starting
4. **Coordination**: All agents update this file and research_progress.md
5. **Error Handling**: Missing prerequisites logged in research_issues.md

## Current Status
`source-technical-profiler` executing Phase 2 banking industry technical profiling (Started: 2025-08-24)