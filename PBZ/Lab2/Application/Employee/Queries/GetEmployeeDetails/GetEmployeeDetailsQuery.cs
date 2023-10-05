using MediatR;

namespace Application.Employee.Queries.GetEmployeeDetails;

public class GetEmployeeDetailsQuery : IRequest<EmployeeDetailsVm>
{
    public int Id { get; set; }
}