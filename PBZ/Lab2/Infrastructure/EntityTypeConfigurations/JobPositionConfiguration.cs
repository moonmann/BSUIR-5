using Domain.Entities;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata.Builders;

namespace Infrastructure.EntityTypeConfigurations;

public class JobPositionConfiguration : IEntityTypeConfiguration<JobPosition>
{
    public void Configure(EntityTypeBuilder<JobPosition> builder)
    {
        builder.HasKey(id => id.Id);
        
        builder.HasIndex(id => id.Id).IsUnique();
        
        builder.Property(jobTitle => jobTitle.JobTitle)
            .HasMaxLength(250);
        
        builder.Property(shortName => shortName.ShortName)
            .HasMaxLength(50);
        
        builder.Property(positionCode => positionCode.PositionCode)
            .HasMaxLength(15);
        
        builder.Property(lowerDischargeLimit => 
            lowerDischargeLimit.LowerDischargeLimit);
        
        builder.Property(upperDischargeLimit => 
            upperDischargeLimit.UpperDischargeLimit);
        
        builder.Property(numberOfJobRates => 
            numberOfJobRates.NumberOfJobRates);
        
    }
}