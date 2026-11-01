import argparse


def calculate_salary(employee_name, basic_salary, allowance, pf_deduction=0, tax_deduction=0):
    if basic_salary < 0 or allowance < 0 or pf_deduction < 0 or tax_deduction < 0:
        raise ValueError("Salary values cannot be negative.")

    gross_salary = basic_salary + allowance
    deductions = pf_deduction + tax_deduction
    net_salary = gross_salary - deductions

    return {
        "employee_name": employee_name,
        "basic_salary": basic_salary,
        "allowance": allowance,
        "gross_salary": gross_salary,
        "pf_deduction": pf_deduction,
        "tax_deduction": tax_deduction,
        "deductions": deductions,
        "net_salary": net_salary,
    }


def format_currency(amount):
    return f"{amount:.2f}"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate employee salary and deductions.")
    parser.add_argument("--name", required=True, help="Employee name")
    parser.add_argument("--basic", type=float, required=True, help="Basic salary")
    parser.add_argument("--allowance", type=float, default=0.0, help="Allowance")
    parser.add_argument("--pf", type=float, default=0.0, help="PF deduction")
    parser.add_argument("--tax", type=float, default=0.0, help="Tax deduction")
    args = parser.parse_args()

    try:
        result = calculate_salary(args.name, args.basic, args.allowance, args.pf, args.tax)

        print(f"Employee Name: {result['employee_name']}")
        print(f"Basic Salary: {format_currency(result['basic_salary'])}")
        print(f"Allowance: {format_currency(result['allowance'])}")
        print(f"Gross Salary: {format_currency(result['gross_salary'])}")
        print(f"PF Deduction: {format_currency(result['pf_deduction'])}")
        print(f"Tax Deduction: {format_currency(result['tax_deduction'])}")
        print(f"Total Deductions: {format_currency(result['deductions'])}")
        print(f"Net Salary: {format_currency(result['net_salary'])}")
    except ValueError as exc:
        print(f"Error: {exc}")
