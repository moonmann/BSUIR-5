using Application.Common.Exceptions;
using Application.Interfaces;
using Domain.Entities;
using MediatR;
using Microsoft.EntityFrameworkCore;

namespace Application.Employee.Commands.UpdateEmployee;

public class UpdateEmployeeCommandHandler 
    : IRequestHandler<UpdateEmployeeCommand>
{
    private readonly ILabDbContext _dbContext;
    public UpdateEmployeeCommandHandler(ILabDbContext context) => _dbContext = context;
    
    public async Task Handle(UpdateEmployeeCommand request, CancellationToken cancellationToken)
    {
        var entity =
            await _dbContext.Employees.FirstOrDefaultAsync(
                employee => employee.Id == request.Id,
                cancellationToken);
        if (entity is null)
        {
            throw new NotFoundException(nameof(Employees), request.Id);
        }

        entity.FullName = request.FullName;
        entity.Age = request.Age;
        entity.Gender = request.Gender;
        entity.FamilyStatus = request.FamilyStatus;

        await _dbContext.SaveChangesAsync(cancellationToken);
    }
}