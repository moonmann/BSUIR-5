using Application.Common.Mappings;
using AutoMapper;
using Domain.Entities;

namespace Application.Employee.Queries.GetEmployeeList;

public class GetLookupDto : IMapWith<Employees>
{
    public int Id { get; set; }
    public string FullName { get; set; }
    public byte Age { get; set; }
    public int Gender { get; set; }
    public bool FamilyStatus { get; set; }

    public void Mapping(Profile profile)
    {
        profile.CreateMap<Employees, Get>()
    }
    
}