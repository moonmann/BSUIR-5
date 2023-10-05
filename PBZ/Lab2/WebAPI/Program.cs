using System.Reflection;
using Application;
using Application.Common.Mappings;
using Application.Interfaces;
using Infrastructure;


var builder = WebApplication.CreateBuilder(args);

builder.Services.AddAutoMapper(config =>
{
    config.AddProfile(new AssemblyMappingProfile(Assembly.GetExecutingAssembly()));
    config.AddProfile(new AssemblyMappingProfile(typeof(ILabDbContext).Assembly));
});

builder.Services.AddApplication();
builder.Services.AddPersistence(builder.Configuration);
builder.Services.AddControllers();

builder.Services.AddCors(options =>
{
    options.AddPolicy("AllowAll", policy =>
    {
        policy.AllowAnyHeader();
        policy.AllowAnyMethod();
        policy.AllowAnyOrigin();
    });
});

var app = builder.Build();

if (app.Environment.IsDevelopment())
    app.UseDeveloperExceptionPage();



app.UseRouting();
app.UseHttpsRedirection();
app.UseCors("AllowAll");

using (var scope = app.Services.CreateScope())
{
    var serviceProvider = scope.ServiceProvider;
    try
    {
        var context = serviceProvider.GetRequiredService<LabDbContext>();
        DbInitializer.Initialize(context);
    }
    catch (Exception e)
    {
        Console.WriteLine(e);
        throw;
    }
}

app.MapControllers();

app.Run();