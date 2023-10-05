using Domain.Entities;
using Microsoft.EntityFrameworkCore;

namespace Application.Interfaces;

public interface IEmployeesDbContext
{
    DbSet<Employees> Employees { get; set; }
    Task<int> SaveChengesAsync(CancellationToken cancellationToken);
}