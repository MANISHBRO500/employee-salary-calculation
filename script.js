document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('salary-form');
    const output = document.getElementById('output');

    form.addEventListener('submit', (event) => {
        event.preventDefault();

        const employeeName = document.getElementById('employeeName').value.trim() || 'Employee';
        const basicSalary = Number(document.getElementById('basicSalary').value) || 0;
        const allowance = Number(document.getElementById('allowance').value) || 0;
        const pfDeduction = Number(document.getElementById('pfDeduction').value) || 0;
        const taxDeduction = Number(document.getElementById('taxDeduction').value) || 0;

        if (basicSalary < 0 || allowance < 0 || pfDeduction < 0 || taxDeduction < 0) {
            output.innerHTML = '>>> Error: Salary values cannot be negative.';
            return;
        }

        const grossSalary = basicSalary + allowance;
        const totalDeductions = pfDeduction + taxDeduction;
        const netSalary = grossSalary - totalDeductions;

        output.innerHTML = `
>>> Employee Salary Details<br>
>>> -------------------------------<br>
>>> Employee Name: ${employeeName}<br>
>>> Basic Salary: ₹${basicSalary.toFixed(2)}<br>
>>> Allowance: ₹${allowance.toFixed(2)}<br>
>>> Gross Salary: ₹${grossSalary.toFixed(2)}<br>
>>> PF Deduction: ₹${pfDeduction.toFixed(2)}<br>
>>> Tax Deduction: ₹${taxDeduction.toFixed(2)}<br>
>>> Total Deductions: ₹${totalDeductions.toFixed(2)}<br>
>>> Net Salary: ₹${netSalary.toFixed(2)}
        `;
    });
});
