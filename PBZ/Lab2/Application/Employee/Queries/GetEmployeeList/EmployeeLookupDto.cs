using Application.Common.Mappings;
using AutoMapper;
using Domain.Entities;

namespace Application.Employee.Queries.GetEmployeeList;

public class EmployeeLookupDto : IMapWith<Employees>
{
    public int Id { get; set; }
    public string FullName { get; set; }
    public byte Age { get; set; }
    public int Gender { get; set; }
    public bool FamilyStatus { get; set; }

    public void Mapping(Profile profile)
    {
        profile.CreateMap<Employees, EmployeeLookupDto>()
            .ForMember(employeeDto => employeeDto.Id,
                opt => opt.MapFrom(employee => employee.Id))
            .ForMember(employeeDto => employeeDto.FullName,
                opt => opt.MapFrom(employee => employee.FullName))
            .ForMember(employeeDto => employeeDto.Age,
                opt => opt.MapFrom(employee => employee.Age))
            .ForMember(employeeDto => employeeDto.Gender,
                opt => opt.MapFrom(employee => employee.Gender))
            .ForMember(employeeDto => employeeDto.FamilyStatus,
                opt => opt.MapFrom(employee => employee.FamilyStatus));
    }
    
}