from typing import Dict, Any
from fastmcp import FastMCP
# Initialize FastMCP server
mcp = FastMCP("Employee Leave System")

# Dummy Employee Database (In-Memory)
EMPLOYEE_DB: Dict[str, Dict[str, Any]] = {
    "EMP101": {
        "name": "Sarah Connor",
        "role": "Software Engineer",
        "balances": {"vacation": 12, "sick": 5, "personal": 3},
        "leave_requests": []
    },
    "EMP102": {
        "name": "Alex Mercer",
        "role": "Product Manager",
        "balances": {"vacation": 4, "sick": 8, "personal": 1},
        "leave_requests": []
    },
    "EMP103": {
        "name": "Elena Rostova",
        "role": "UI/UX Designer",
        "balances": {"vacation": 18, "sick": 10, "personal": 4},
        "leave_requests": []
    }
}

# Dummy Company Leave Policies
POLICY_DB: Dict[str, str] = {
    "vacation": "Vacation days accrue monthly. A maximum of 5 unused days can be carried over to the next calendar year.",
    "sick": "Sick leave requires a doctor's note if taking more than 3 consecutive working days.",
    "maternity": "Eligible employees receive 12 weeks of fully paid parental leave.",
    "bereavement": "Employees receive up to 5 days of paid leave for immediate family members."
}


@mcp.tool()
async def get_leave_balance(employee_id: str) -> str:
    """Get remaining leave balances (vacation, sick, personal) for an employee.

    Args:
        employee_id: The unique identifier of the employee (e.g. EMP101, EMP102, EMP103)
    """
    emp_id = employee_id.upper().strip()
    employee = EMPLOYEE_DB.get(emp_id)

    if not employee:
        available_ids = ", ".join(EMPLOYEE_DB.keys())
        return f"Employee '{employee_id}' not found. Available IDs: {available_ids}"

    balances = employee["balances"]
    return (
        f"Leave Balances for {employee['name']} ({employee['role']}):\n"
        f"- Vacation: {balances['vacation']} days remaining\n"
        f"- Sick Leave: {balances['sick']} days remaining\n"
        f"- Personal: {balances['personal']} days remaining"
    )


@mcp.tool()
async def request_time_off(
    employee_id: str, 
    leave_type: str, 
    start_date: str, 
    end_date: str, 
    reason: str = "Not specified"
) -> str:
    """Submit a formal time-off request for an employee.

    Args:
        employee_id: The unique identifier of the employee (e.g. EMP101)
        leave_type: Type of leave ('vacation', 'sick', or 'personal')
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        reason: Optional description or reason for the leave
    """
    emp_id = employee_id.upper().strip()
    leave_type_clean = leave_type.lower().strip()
    employee = EMPLOYEE_DB.get(emp_id)

    if not employee:
        return f"Error: Employee '{employee_id}' does not exist."

    if leave_type_clean not in employee["balances"]:
        return f"Error: Invalid leave type '{leave_type}'. Choose from: vacation, sick, personal."

    current_balance = employee["balances"][leave_type_clean]
    if current_balance <= 0:
        return f"Request Failed: {employee['name']} has 0 days of {leave_type_clean} leave remaining."

    # Create dummy request record
    request_id = f"REQ-{len(employee['leave_requests']) + 101}"
    request_data = {
        "request_id": request_id,
        "type": leave_type_clean,
        "start_date": start_date,
        "end_date": end_date,
        "reason": reason,
        "status": "Pending Manager Approval"
    }
    
    employee["leave_requests"].append(request_data)

    return (
        f"Successfully submitted {leave_type_clean} request for {employee['name']}!\n"
        f"- Request ID: {request_id}\n"
        f"- Dates: {start_date} to {end_date}\n"
        f"- Reason: {reason}\n"
        f"- Status: Pending Manager Approval\n"
        f"- Remaining Balance: {current_balance} days (will deduct upon approval)"
    )


@mcp.tool()
async def check_leave_policy(topic: str) -> str:
    """Search company policy rules regarding employee leaves.

    Args:
        topic: Keyword or topic to search (e.g. 'vacation', 'sick', 'maternity', 'bereavement')
    """
    topic_clean = topic.lower().strip()
    
    matches = [
        f"**{key.capitalize()} Policy:** {value}" 
        for key, value in POLICY_DB.items() 
        if topic_clean in key or key in topic_clean
    ]

    if not matches:
        available_topics = ", ".join(POLICY_DB.keys())
        return f"No direct policy matches found for '{topic}'. Available topics: {available_topics}"

    return "\n---\n".join(matches)