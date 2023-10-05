using MediatR;

namespace Application.Employee.Commands.UpdateEmployee;

public class UpdateEmployeeCommand : IRequest
{
    public int Id { get; set; }
    public string FullName { get; set; }
    public byte Age { get; set; }
    public int Gender { get; set; }
    public bool FamilyStatus { get; set; }
}