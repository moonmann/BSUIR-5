using Application.Interfaces;
using AutoMapper;
using MediatR;
using AutoMapper.QueryableExtensions;
using Microsoft.EntityFrameworkCore;

namespace Application.Employee.Queries.GetEmployeeList;

public class GetEmployeeListQueryHandler
    : IRequestHandler<GetEmployeeListQuery, EmployeeListVm>
{
    private readonly ILabDbContext _dbContext;
    private readonly IMapper _mapper;

    public GetEmployeeListQueryHandler(ILabDbContext context, IMapper mapper) =>
        (_dbContext, _mapper) = (context, mapper);

    public async Task<EmployeeListVm> Handle(GetEmployeeListQuery request, CancellationToken cancellationToken)
    {
        var employeesQuery = await _dbContext.Employees.Skip(request.SkipPosition).Take(request.SkipPosition + 10)
            .ProjectTo<EmployeeLookupDto>(_mapper.ConfigurationProvider).ToListAsync(cancellationToken);

        return new EmployeeListVm { Employees = employeesQuery };
    }
}