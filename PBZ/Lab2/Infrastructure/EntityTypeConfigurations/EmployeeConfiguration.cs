using Domain.Entities;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata.Builders;

namespace Infrastructure.EntityTypeConfigurations;

public class EmployeeConfiguration : IEntityTypeConfiguration<Employees>
{
    public void Configure(EntityTypeBuilder<Employees> builder)
    {
        builder.HasKey(id => id.Id);
        builder.HasIndex(id => id.Id).IsUnique();
        builder.Property(name => name.FullName);
        builder.Property(fStatus => fStatus.FamilyStatus);
        builder.Property(age => age.Age);
        builder.Property(gender => gender.Gender);
    }
}