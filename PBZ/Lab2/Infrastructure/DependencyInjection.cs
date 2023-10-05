using Application.Interfaces;
using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;

namespace Infrastructure;

public static class DependencyInjection
{
    public static IServiceCollection AddPersistence(this IServiceCollection services,
        IConfiguration configuration)
    {
        var connectionString = configuration["DbConnection"];
        services.AddDbContext<LabDbContext>(options =>
        {
            options.UseNpgsql(connectionString);
        });
        services.AddScoped<ILabDbContext>(provider => 
            provider.GetService<LabDbContext>()!);
        return services;
    }
}