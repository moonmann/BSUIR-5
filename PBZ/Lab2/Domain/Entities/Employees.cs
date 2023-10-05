using Domain.Entities;

namespace Domain.Entities;

public enum Genders
{
    Male, Female, Other, Timofei
}

public class Employees
{
    public int Id { get; set; }
    public string FullName { get; set; }
    public byte Age { get; set; }
    public int Gender { get; set; }
    public bool FamilyStatus { get; set; }
}