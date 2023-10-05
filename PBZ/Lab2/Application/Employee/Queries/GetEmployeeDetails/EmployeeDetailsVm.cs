using Application.Common.Mappings;
using AutoMapper;
using Domain.Entities;

namespace Application.Employee.Queries.GetEmployeeDetails;

public class EmployeeDetailsVm : IMapWith<Employees>
{
    public int Id { get; set; }
    public string FullName { get; set; }
    public byte Age { get; set; }
    public int Gender { get; set; }
    public bool FamilyStatus { get; set; }

    public void Mapping(Profile profile)
    {
        profile.CreateMap<Employees, EmployeeDetailsVm>()
            .ForMember(employeeVm => employeeVm.Id,
                opt => opt.MapFrom(employee => employee.Id))
            .ForMember(employeeVm => employeeVm.FullName,
                opt => opt.MapFrom(employee => employee.FullName))
            .ForMember(employeeVm => employeeVm.Age,
                opt => opt.MapFrom(employee => employee.Age))
            .ForMember(employeeVm => employeeVm.Gender,
                opt => opt.MapFrom(employee => employee.Gender))
            .ForMember(employeeVm => employeeVm.FamilyStatus,
                opt => opt.MapFrom(employee => employee.FamilyStatus));
    }
}