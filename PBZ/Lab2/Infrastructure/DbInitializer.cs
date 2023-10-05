namespace Infrastructure;

public class DbInitializer
{
    public static void Initialize(LabDbContext context)
    {
        context.Database.EnsureCreated();
    }
}