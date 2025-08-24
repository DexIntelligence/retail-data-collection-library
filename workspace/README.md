# Research Workspace

Active coordination space for current research activities and agent communication.

## Master Research List Coordination

The `RESEARCH-MASTER-LIST.md` file in the project root determines research priorities. This workspace coordinates the execution of research for industries listed there:
- Current industry being researched is tracked in `current_research.md`
- Status updates are reflected back to the master list upon completion
- Industries are processed in order from top to bottom of the master list

## Workspace Files

### `current_research.md`
**Master coordination document** for ongoing research activities.
- **Purpose**: Track current industry/chain being researched
- **Usage**: Agent coordination, progress tracking, issue management
- **Updates**: Real-time updates from all active agents

### `research_progress.md` 
**Detailed progress tracking** for multi-step research processes.
- **Purpose**: Step-by-step progress within current research phase
- **Usage**: Monitor completion status, identify bottlenecks
- **Updates**: Agents update upon task completion

### `research_issues.md`
**Problem resolution tracking** for technical and research issues.
- **Purpose**: Document problems, solutions, and lessons learned
- **Usage**: Issue escalation, pattern recognition, troubleshooting
- **Updates**: Agents log issues and resolutions

### `chain_queue.md`
**Research queue management** for batch processing multiple chains.
- **Purpose**: Prioritize and track chain research within an industry
- **Usage**: Load balancing, progress visualization
- **Updates**: Updated as chains are researched and completed

## Workspace Workflow

### Starting New Industry Research
1. Check `RESEARCH-MASTER-LIST.md` for next industry to research
2. Initialize `current_research.md` with industry from master list
3. Update master list status to `[initiated]`
4. Execute source discovery agents for the industry
5. Track progress in `research_progress.md`
6. Log issues and solutions in `research_issues.md`
7. Upon completion, update master list to `[completed pass on YYYY-MM-DD]`

### Agent Coordination
- Agents check `current_research.md` for assignments
- Agents update progress in real-time
- Agents log issues for cross-agent awareness
- Completed work moves to `data/` directories

### Research Completion
- Archive workspace files to `logs/` with timestamps
- Initialize new workspace for next industry
- Update library with completed research