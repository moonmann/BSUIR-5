using MediatR;

namespace Application.Employee.Commands.DeleteEmployee;

public class DeleteEmployeeCommand : IRequest
{
    public int Id { get; set; }
}