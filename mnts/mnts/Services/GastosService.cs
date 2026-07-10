using mnts.Models;
using SQLite;
using System;
using System.Collections.Generic;
using System.Text;

namespace mnts.Services;

public class GastosService
{
    private SQLiteAsyncConnection? _db;

    private async Task InitAsync()
    {
        if (_db is not null) return;

        var dbPath = Path.Combine(FileSystem.AppDataDirectory, "gastos.db");
        System.Diagnostics.Debug.WriteLine($"BASE DE DATOS EN: {dbPath}");

        _db = new SQLiteAsyncConnection(dbPath);

        await _db.CreateTableAsync<Gasto>();
        await _db.CreateTableAsync<Ingreso>();
    }

    // Gastos

    public async Task InsertarGastoAsync(int dia, int mes, int anio, string categoria, double monto)
    {
        await InitAsync();

        var gasto = new Gasto
        {
            Dia = dia,
            Mes = mes,
            Anio = anio,
            Categoria = categoria,
            Monto = monto
        };

        await _db!.InsertAsync(gasto);
    }

    public async Task<List<ResumenCategoria>> ObtenerResumenPorCategoriaAsync(int mes, int anio)
    {
        await InitAsync();

        var query = "SELECT Categoria, SUM(Monto) as Total FROM Gasto WHERE Mes = ? AND Anio = ? GROUP BY Categoria";
        return await _db!.QueryAsync<ResumenCategoria>(query, mes, anio);
    }

    public async Task<double> ObtenerTotalGastosAsync(int mes, int anio)
    {
        await InitAsync();

        var gastos = await _db!.Table<Gasto>()
            .Where(g => g.Mes == mes && g.Anio == anio)
            .ToListAsync();

        return gastos.Sum(g => g.Monto);
    }

    public async Task<int> BorrarGastosAsync(int? dia, int mes, int anio)
    {
        await InitAsync();

        if (dia is null)
        {
            return await _db!.Table<Gasto>()
                .DeleteAsync(g => g.Mes == mes && g.Anio == anio);
        }

        return await _db!.Table<Gasto>()
            .DeleteAsync(g => g.Dia == dia && g.Mes == mes && g.Anio == anio);
    }

    public async Task<(int? dia, double monto)> ObtenerDiaMayorGastoAsync(int mes, int anio)
    {
        await InitAsync();

        var query = @"SELECT Dia, SUM(Monto) as Total FROM Gasto 
                  WHERE Mes = ? AND Anio = ? 
                  GROUP BY Dia ORDER BY Total DESC LIMIT 1";

        var resultado = await _db!.QueryAsync<ResumenDia>(query, mes, anio);
        return resultado.Count > 0 ? (resultado[0].Dia, resultado[0].Total) : (null, 0);
    }

    public async Task<(int? dia, double monto)> ObtenerDiaMenorGastoAsync(int mes, int anio)
    {
        await InitAsync();

        var query = @"SELECT Dia, SUM(Monto) as Total FROM Gasto 
                  WHERE Mes = ? AND Anio = ? 
                  GROUP BY Dia ORDER BY Total ASC LIMIT 1";

        var resultado = await _db!.QueryAsync<ResumenDia>(query, mes, anio);
        return resultado.Count > 0 ? (resultado[0].Dia, resultado[0].Total) : (null, 0);
    }

    private class ResumenDia
    {
        public int Dia { get; set; }
        public double Total { get; set; }
    }

    // Ingresos

    public async Task InsertarIngresoAsync(int mes, int anio, double monto)
    {
        await InitAsync();

        var ingreso = new Ingreso
        {
            Mes = mes,
            Anio = anio,
            Monto = monto
        };

        await _db!.InsertAsync(ingreso);
    }

    public async Task<double> ObtenerTotalIngresosAsync(int mes, int anio)
    {
        await InitAsync();

        var ingresos = await _db!.Table<Ingreso>()
            .Where(i => i.Mes == mes && i.Anio == anio)
            .ToListAsync();

        return ingresos.Sum(i => i.Monto);
    }

    public async Task<int> BorrarPresupuestoAsync(int mes, int anio)
    {
        await InitAsync();

        return await _db!.Table<Ingreso>()
            .DeleteAsync(i => i.Mes == mes && i.Anio == anio);
    }
}