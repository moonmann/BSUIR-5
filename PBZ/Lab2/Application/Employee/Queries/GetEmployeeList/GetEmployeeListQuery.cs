using MediatR;

namespace Application.Employee.Queries.GetEmployeeList;

public class GetEmployeeListQuery : IRequest<EmployeeListVm>
{
     public int SkipPosition { get; set; }
}