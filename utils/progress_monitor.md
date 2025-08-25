# Progress Monitoring Routine

## Purpose
A systematic check routine to ensure research agents stay focused on priority completion and maintain proper sequential workflow.

## Monitor Execution Steps

### 1. Read Current Status
```
- Read workspace/research_progress.md
- Read workspace/current_research.md  
- Read RESEARCH-MASTER-LIST.md
```

### 2. Priority Assessment
```
PRIORITY_ORDER = ["banking", "credit unions", "pharmacy", "grocery", ...]

FOR each industry in PRIORITY_ORDER:
  IF industry.status != "COMPLETED":
    current_priority = industry
    BREAK
```

### 3. Phase Completion Check
```
FOR current_priority industry:
  - Phase 1 (Source Discovery): COMPLETED?
  - Phase 2 (Technical Access): COMPLETED?  
  - Phase 3 (Domain Analysis): COMPLETED?
  - Phase 4 (Coverage Integration): COMPLETED?
  
  IF any phase != COMPLETED:
    next_required_phase = first_incomplete_phase
```

### 4. Agent Focus Verification
```
CHECK: Are all active agents working on current_priority industry?
CHECK: Is next_required_phase being executed?
CHECK: Are agents updating logs properly?

IF agents working on wrong industry:
  REDIRECT to current_priority
  
IF required phase not started:
  LAUNCH appropriate agent for next_required_phase
```

### 5. Sequential Workflow Validation
```
VALIDATE:
- Only ONE industry should be "IN PROGRESS" at a time
- Phases should complete in order: 1 → 2 → 3 → 4
- No Phase 3 starting before Phase 2 completion
- No new industry starting before current industry completion
```

### 6. Course Correction Actions

#### If Priority Violation Detected:
```
ACTION: Stop lower-priority work
ACTION: Redirect agents to current_priority industry
ACTION: Update workspace logs with course correction
```

#### If Phase Sequence Violation:
```
ACTION: Complete missing prerequisite phases first
ACTION: Hold advanced phases until prerequisites done
ACTION: Update agent instructions for proper sequence
```

#### If Logging Gaps Detected:
```
ACTION: Update workspace/research_progress.md
ACTION: Update workspace/current_research.md
ACTION: Enforce agent logging requirements
```

### 7. Progress Report Generation
```
REPORT:
- Current priority industry: [industry_name]
- Current phase: [phase_number] - [phase_status]
- Active agents: [agent_list]
- Completion percentage: [X%]
- Next required action: [specific_task]
- Any course corrections made: [yes/no with details]
```

## Monitor Frequency
- Run every 15-20 minutes during active research
- Run after each major agent completion
- Run when user requests progress update

## Success Indicators
- ✅ Only one industry IN PROGRESS at a time
- ✅ Phases completing in proper sequence (1→2→3→4)
- ✅ All agents focused on current priority
- ✅ Logs properly updated
- ✅ Clear next action identified

## Alert Conditions
- 🚨 Multiple industries IN PROGRESS simultaneously  
- 🚨 Phase sequence violation (Phase 3 without Phase 2 complete)
- 🚨 Agents working on wrong priority industry
- 🚨 Logging gaps longer than 30 minutes
- 🚨 No progress on current priority for 60+ minutes

## Example Monitor Output
```
=== PROGRESS MONITOR REPORT ===
Timestamp: 2025-08-25 15:30:00
Current Priority: credit unions
Current Phase: Phase 2 - Technical Access Documentation  
Status: IN PROGRESS
Active Agent: source-technical-profiler
Progress: 40% complete (Phase 1 ✅, Phase 2 🔄, Phase 3 ⏳, Phase 4 ⏳)
Next Action: Complete Phase 2, then launch Phase 3 domain specialists
Course Corrections: None required
Priority Compliance: ✅ GOOD
Sequential Workflow: ✅ GOOD  
Logging Status: ✅ GOOD
```