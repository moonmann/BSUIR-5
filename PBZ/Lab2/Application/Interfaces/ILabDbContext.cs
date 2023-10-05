using Domain.Entities;
using Microsoft.EntityFrameworkCore;

namespace Application.Interfaces;

public interface ILabDbContext
{
    DbSet<Employees> Employees { get; set; }
    Task<int> SaveChangesAsync(CancellationToken cancellationToken);
}