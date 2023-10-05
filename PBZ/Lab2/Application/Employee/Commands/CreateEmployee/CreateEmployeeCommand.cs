using Domain.Entities;
using MediatR;

namespace Application.Employee.Commands.CreateEmployee;

public class CreateEmployeeCommand : IRequest<string>
{
    public string FullName { get; set; }
    public byte Age { get; set; }
    public int Gender { get; set; }
    public bool FamilyStatus { get; set; }
}