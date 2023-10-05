using Application.Common.Exceptions;
using Application.Interfaces;
using Domain.Entities;
using MediatR;

namespace Application.Employee.Commands.DeleteEmployee;

public class DeleteEmployeeCommandHandler : IRequestHandler<DeleteEmployeeCommand>
{
    private readonly ILabDbContext _dbContext;
    public DeleteEmployeeCommandHandler(ILabDbContext context) 
        => _dbContext = context;
    
    public async Task Handle(DeleteEmployeeCommand request, CancellationToken cancellationToken)
    {
        var entity =
            await _dbContext.Employees.FindAsync(new object[] {request.Id}, 
                cancellationToken);
        
        if (entity is null)
        {
            throw new NotFoundException(nameof(Employees), request.Id);
        }

        _dbContext.Employees.Remove(entity);
        await _dbContext.SaveChangesAsync(cancellationToken);
    }
}