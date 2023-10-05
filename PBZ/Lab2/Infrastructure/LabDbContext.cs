using Application.Interfaces;
using Domain.Entities;
using Infrastructure.EntityTypeConfigurations;
using Microsoft.EntityFrameworkCore;

namespace Infrastructure;

public class LabDbContext : DbContext, ILabDbContext
{
    public DbSet<Employees> Employees { get; set; }
    public LabDbContext(DbContextOptions<LabDbContext> options)
        : base(options){}

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        modelBuilder.ApplyConfiguration(new EmployeeConfiguration());
        base.OnModelCreating(modelBuilder);
    }
}