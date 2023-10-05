using Application.Common.Exceptions;
using Application.Interfaces;
using AutoMapper;
using Domain.Entities;
using MediatR;
using Microsoft.EntityFrameworkCore;

namespace Application.Employee.Queries.GetEmployeeDetails;

public class GetEmployeeDetailsQueryHandler
    : IRequestHandler<GetEmployeeDetailsQuery, EmployeeDetailsVm>
{
    private readonly ILabDbContext _dbContext;
    private readonly IMapper _mapper;
    
    public GetEmployeeDetailsQueryHandler(ILabDbContext context, IMapper mapper)
        => (_dbContext, _mapper )= (context, mapper);
    
    public async Task<EmployeeDetailsVm> Handle(GetEmployeeDetailsQuery request, CancellationToken cancellationToken)
    {
        var entity =
            await _dbContext.Employees.FirstOrDefaultAsync(employee =>
                employee.Id == request.Id, cancellationToken);

        if (entity is null)
        {
            throw new NotFoundException(nameof(Employees), request.Id);
        }

        return _mapper.Map<EmployeeDetailsVm>(entity);

    }
}