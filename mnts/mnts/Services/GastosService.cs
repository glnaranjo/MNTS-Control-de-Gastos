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
        _db = new SQLiteAsyncConnection(dbPath);

        await _db.CreateTableAsync<Gasto>();
        await _db.CreateTableAsync<Ingreso>();
        await _db.CreateTableAsync<Etiqueta>();

        var cantidadEtiquetas = await _db.Table<Etiqueta>().CountAsync();
        if (cantidadEtiquetas == 0)
        {
            foreach (var etiqueta in ObtenerEtiquetasPorDefecto())
            {
                await _db.InsertAsync(etiqueta);
            }
        }
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

    public async Task<List<HistorialMes>> ObtenerHistorialGastosAsync(int mesFinal, int anioFinal, int cantidadMeses)
    {
        var resultado = new List<HistorialMes>();

        var mes = mesFinal;
        var anio = anioFinal;

        for (int i = 0; i < cantidadMeses; i++)
        {
            var total = await ObtenerTotalGastosAsync(mes, anio);
            resultado.Add(new HistorialMes { Mes = mes, Anio = anio, Total = total });

            mes--;
            if (mes < 1)
            {
                mes = 12;
                anio--;
            }
        }

        resultado.Reverse(); // para que quede en orden cronológico (mas viejo -> mas nuevo)
        return resultado;
    }

    // ---------- GASTOS INDIVIDUALES ----------

    public async Task<List<Gasto>> ObtenerGastosPorFechaAsync(int? dia, int mes, int anio)
    {
        await InitAsync();

        if (dia is null)
        {
            return await _db!.Table<Gasto>()
                .Where(g => g.Mes == mes && g.Anio == anio)
                .OrderBy(g => g.Dia)
                .ToListAsync();
        }

        return await _db!.Table<Gasto>()
            .Where(g => g.Dia == dia && g.Mes == mes && g.Anio == anio)
            .ToListAsync();
    }

    public async Task ActualizarGastoAsync(int id, string categoria, double monto)
    {
        await InitAsync();

        var gasto = await _db!.Table<Gasto>().Where(g => g.Id == id).FirstOrDefaultAsync();
        if (gasto is not null)
        {
            gasto.Categoria = categoria;
            gasto.Monto = monto;
            await _db!.UpdateAsync(gasto);
        }
    }

    public async Task BorrarGastoPorIdAsync(int id)
    {
        await InitAsync();
        await _db!.DeleteAsync<Gasto>(id);
    }

    // ---------- INGRESOS INDIVIDUALES ----------

    public async Task<List<Ingreso>> ObtenerIngresosPorFechaAsync(int mes, int anio)
    {
        await InitAsync();

        return await _db!.Table<Ingreso>()
            .Where(i => i.Mes == mes && i.Anio == anio)
            .ToListAsync();
    }

    public async Task ActualizarIngresoAsync(int id, double monto)
    {
        await InitAsync();

        var ingreso = await _db!.Table<Ingreso>().Where(i => i.Id == id).FirstOrDefaultAsync();
        if (ingreso is not null)
        {
            ingreso.Monto = monto;
            await _db!.UpdateAsync(ingreso);
        }
    }

    public async Task BorrarIngresoPorIdAsync(int id)
    {
        await InitAsync();
        await _db!.DeleteAsync<Ingreso>(id);
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

    // Borrar/Delete db

    public async Task ReiniciarBaseDatosAsync()
    {
        await InitAsync();

        await _db!.DeleteAllAsync<Gasto>();
        await _db!.DeleteAllAsync<Ingreso>();
        await RestaurarEtiquetasAsync();
    }

    private static List<Etiqueta> ObtenerEtiquetasPorDefecto() => new()
    {
        new Etiqueta { Id = 1, ClaveInterna = "comida", Nombre = "Comida", Icono = "🍔" },
        new Etiqueta { Id = 2, ClaveInterna = "vivienda", Nombre = "Vivienda", Icono = "🏠" },
        new Etiqueta { Id = 3, ClaveInterna = "servicios", Nombre = "Servicios", Icono = "💡" },
        new Etiqueta { Id = 4, ClaveInterna = "ocio", Nombre = "Ocio", Icono = "🎮" },
        new Etiqueta { Id = 5, ClaveInterna = "salud", Nombre = "Salud", Icono = "❤️" },
        new Etiqueta { Id = 6, ClaveInterna = "extras", Nombre = "Extras", Icono = "📦" },
    };

    public async Task<List<Etiqueta>> ObtenerEtiquetasAsync()
    {
        await InitAsync();
        return await _db!.Table<Etiqueta>().OrderBy(e => e.Id).ToListAsync();
    }

    public async Task ActualizarEtiquetaAsync(int id, string nuevoNombre, string nuevoIcono)
    {
        await InitAsync();

        var etiqueta = await _db!.Table<Etiqueta>().Where(e => e.Id == id).FirstOrDefaultAsync();
        if (etiqueta is not null)
        {
            etiqueta.Nombre = nuevoNombre;
            etiqueta.Icono = nuevoIcono;
            await _db!.UpdateAsync(etiqueta);
        }
    }

    public async Task RestaurarEtiquetasAsync()
    {
        await InitAsync();

        foreach (var etiquetaDefault in ObtenerEtiquetasPorDefecto())
        {
            await _db!.UpdateAsync(etiquetaDefault);
        }
    }
}