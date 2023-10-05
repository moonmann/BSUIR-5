using Domain.Entities;
using MediatR;

namespace Application.Employees.Commands.CreateEmployee;

public class CreateEmployeeCommand : IRequest<int>
{
    public int Id { get; set; }
    public string FullName { get; set; }
    public byte Age { get; set; }
    public Genders Genders { get; set; }
    public bool FamilyStatus { get; set; }
}