using Application.Interfaces;
using Domain.Entities;
using MediatR;
using Microsoft.EntityFrameworkCore;

namespace Application.Employee.Commands.CreateEmployee;

public class CreateEmployeeCommandHandler
    : IRequestHandler<CreateEmployeeCommand, string>
{
    private readonly ILabDbContext _dbContext;
    public CreateEmployeeCommandHandler(ILabDbContext dbContext) => _dbContext = dbContext;
    
    public async Task<string> Handle(CreateEmployeeCommand request, CancellationToken cancellationToken)
    {
        var employee = new Employees
        {
            FullName = request.FullName,
            Age = request.Age,
            Gender = request.Gender,
            FamilyStatus = request.FamilyStatus
        };
        await _dbContext.Employees.AddAsync(employee, cancellationToken);
        await _dbContext.SaveChangesAsync(cancellationToken);
        return employee.FullName;
    }
}