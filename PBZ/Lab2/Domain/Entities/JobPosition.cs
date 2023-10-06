using System.Diagnostics.CodeAnalysis;

namespace Domain.Entities;

public class JobPosition
{
    public int Id { get; set; }
    public string JobTitle { get; set; }
    public string ShortName { get; set; }
    public string PositionCode { get; set; }
    public int LowerDischargeLimit { get; set; }
    public int UpperDischargeLimit { get; set; }
    public int NumberOfJobRates { get; set; }
}