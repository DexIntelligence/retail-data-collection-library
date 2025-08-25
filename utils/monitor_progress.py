#!/usr/bin/env python3
"""
Progress Monitor - Ensures research stays focused on priority completion
Run this every 15-20 minutes to check research progress and course-correct if needed
"""

import os
import json
from datetime import datetime

def read_file(filepath):
    """Read file content safely"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return f"ERROR: File not found: {filepath}"
    except Exception as e:
        return f"ERROR reading {filepath}: {str(e)}"

def monitor_progress():
    """Main monitoring function"""
    
    print("=== PROGRESS MONITOR REPORT ===")
    print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # 1. Read current status files
    progress_file = "workspace/research_progress.md"
    master_list = "RESEARCH-MASTER-LIST.md"
    current_research = "workspace/current_research.md"
    
    progress_content = read_file(progress_file)
    master_content = read_file(master_list)
    
    # 2. Determine current priority industry
    priority_order = ["banking", "credit unions", "pharmacy", "grocery", "retail gasoline", 
                     "quick serve restaurants", "veterinary services", "dentistry", "convenience stores"]
    
    current_priority = None
    current_priority_status = None
    
    # Find first non-completed industry
    for industry in priority_order:
        if f"{industry} [COMPLETED" in master_content:
            continue
        else:
            current_priority = industry
            if f"{industry} [Phase" in master_content:
                current_priority_status = "IN PROGRESS"
            else:
                current_priority_status = "NOT STARTED"
            break
    
    print(f"Current Priority Industry: {current_priority}")
    print(f"Priority Status: {current_priority_status}")
    
    # 3. Analyze current phase status for priority industry
    if current_priority:
        phases = {
            1: "Source Discovery",
            2: "Technical Access Documentation", 
            3: "Domain Analysis",
            4: "Coverage Integration"
        }
        
        phase_status = {}
        next_required_phase = None
        
        # Look for specific phase sections for current priority industry
        industry_section = ""
        in_industry_section = False
        for line in progress_content.split('\n'):
            if f"## {current_priority.title()}" in line:
                in_industry_section = True
                industry_section = line + "\n"
            elif line.startswith("## ") and in_industry_section:
                break  # End of this industry section
            elif in_industry_section:
                industry_section += line + "\n"
        
        for phase_num, phase_name in phases.items():
            phase_section = f"### Phase {phase_num}"
            if phase_section in industry_section:
                if "- **Status**: COMPLETED" in industry_section:
                    phase_status[phase_num] = "[COMPLETED]"
                elif "- **Status**: IN PROGRESS" in industry_section:
                    phase_status[phase_num] = "[IN PROGRESS]"
                    if next_required_phase is None:
                        next_required_phase = phase_num
                else:
                    phase_status[phase_num] = "[PENDING]"
                    if next_required_phase is None:
                        next_required_phase = phase_num
            else:
                phase_status[phase_num] = "[PENDING]"
                if next_required_phase is None:
                    next_required_phase = phase_num
        
        print()
        print("Phase Status:")
        for phase_num, status in phase_status.items():
            print(f"  Phase {phase_num} ({phases[phase_num]}): {status}")
        
        if next_required_phase:
            print(f"Next Required Phase: {next_required_phase} - {phases[next_required_phase]}")
        else:
            print("Next Required Phase: Industry completion - ready for next industry")
    
    # 4. Check for violations and issues
    print()
    print("COMPLIANCE CHECKS:")
    
    issues = []
    course_corrections_needed = []
    
    # Check for multiple industries in progress
    industries_in_progress = []
    for industry in priority_order:
        if f"{industry} [Phase" in master_content and "[COMPLETED" not in master_content:
            industries_in_progress.append(industry)
    
    if len(industries_in_progress) > 1:
        issues.append(f"PRIORITY VIOLATION: Multiple industries in progress: {', '.join(industries_in_progress)}")
        course_corrections_needed.append("Stop work on lower-priority industries")
    elif len(industries_in_progress) == 1:
        print("Single Industry Focus: GOOD")
    else:
        print("No industries currently in progress")
    
    # Check phase sequence
    if current_priority and "Phase 3" in progress_content and "IN PROGRESS" in progress_content:
        if "Phase 2" not in progress_content or "COMPLETED" not in progress_content:
            issues.append("SEQUENCE VIOLATION: Phase 3 started before Phase 2 completion")
            course_corrections_needed.append("Complete Phase 2 before continuing Phase 3")
    
    if current_priority and "Phase 4" in progress_content and "IN PROGRESS" in progress_content:
        incomplete_previous = []
        for phase in [1, 2, 3]:
            if f"Phase {phase}" not in progress_content or "COMPLETED" not in progress_content:
                incomplete_previous.append(f"Phase {phase}")
        if incomplete_previous:
            issues.append(f"SEQUENCE VIOLATION: Phase 4 started before completion of: {', '.join(incomplete_previous)}")
            course_corrections_needed.append(f"Complete {', '.join(incomplete_previous)} before Phase 4")
    
    if not issues:
        print("Sequential Workflow: GOOD")
    
    # Print issues
    if issues:
        print()
        print("ISSUES DETECTED:")
        for issue in issues:
            print(f"  {issue}")
    
    # Print course corrections needed
    if course_corrections_needed:
        print()
        print("COURSE CORRECTIONS NEEDED:")
        for correction in course_corrections_needed:
            print(f"  → {correction}")
    
    # 5. Generate next action recommendation
    print()
    if current_priority and next_required_phase:
        phase_actions = {
            1: "Launch industry-source-discovery agent",
            2: "Launch source-technical-profiler agent", 
            3: "Launch domain analysis specialists (brand, government, aggregator, commercial)",
            4: "Launch source-coverage-analyst agent"
        }
        print(f"NEXT RECOMMENDED ACTION: {phase_actions.get(next_required_phase, 'Unknown phase')}")
    elif current_priority is None:
        print("NEXT RECOMMENDED ACTION: All industries completed!")
    else:
        print("NEXT RECOMMENDED ACTION: Complete current phase, then move to next industry")
    
    print()
    print("=== END MONITOR REPORT ===")
    return len(issues) == 0  # Return True if no issues detected

if __name__ == "__main__":
    # Change to project directory
    import sys
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(project_root)
    print(f"Working directory: {os.getcwd()}")
    print()
    
    # Run monitor
    success = monitor_progress()
    
    # Exit with appropriate code
    sys.exit(0 if success else 1)