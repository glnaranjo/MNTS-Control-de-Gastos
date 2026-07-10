using System;
using System.Collections.Generic;
using System.Text;

using ClosedXML.Excel;
using mnts.Models;

namespace mnts.Services;

public class ExportService
{
    private string ObtenerRutaCarpetaExportacion()
    {
        var carpeta = Path.Combine(FileSystem.AppDataDirectory, "Exportaciones");
        Directory.CreateDirectory(carpeta);
        return carpeta;
    }

    public string ExportarExcel(ResumenExportData datos)
    {
        var nombreArchivo = $"{datos.Mes}-{datos.Anio}.xlsx";
        var ruta = Path.Combine(ObtenerRutaCarpetaExportacion(), nombreArchivo);

        using var workbook = new XLWorkbook();
        var hoja = workbook.Worksheets.Add("Resumen");

        hoja.Cell("A1").Value = $"Resumen de {datos.Mes}/{datos.Anio}";
        hoja.Cell("A1").Style.Font.Bold = true;
        hoja.Cell("A1").Style.Font.FontSize = 14;

        hoja.Cell("A3").Value = "Categoría";
        hoja.Cell("B3").Value = "Monto";
        hoja.Cell("C3").Value = "% del total";
        hoja.Range("A3:C3").Style.Font.Bold = true;

        var fila = 4;
        foreach (var item in datos.Categorias)
        {
            var porcentaje = datos.TotalGastos > 0 ? (item.Total / datos.TotalGastos) * 100 : 0;

            hoja.Cell(fila, 1).Value = item.Categoria;
            hoja.Cell(fila, 2).Value = item.Total;
            hoja.Cell(fila, 2).Style.NumberFormat.Format = "$#,##0.00";
            hoja.Cell(fila, 3).Value = porcentaje / 100;
            hoja.Cell(fila, 3).Style.NumberFormat.Format = "0.00%";
            fila++;
        }

        fila++;
        hoja.Cell(fila, 1).Value = "Gasto total";
        hoja.Cell(fila, 2).Value = -datos.TotalGastos;
        hoja.Cell(fila, 2).Style.NumberFormat.Format = "$#,##0.00";
        fila++;

        hoja.Cell(fila, 1).Value = "Ingreso total";
        hoja.Cell(fila, 2).Value = datos.TotalIngresos;
        hoja.Cell(fila, 2).Style.NumberFormat.Format = "$#,##0.00";
        fila++;

        hoja.Cell(fila, 1).Value = "Diferencia";
        hoja.Cell(fila, 2).Value = datos.Diferencia;
        hoja.Cell(fila, 2).Style.NumberFormat.Format = "$#,##0.00";
        fila += 2;

        if (datos.DiaMayor is not null)
        {
            hoja.Cell(fila, 1).Value = $"Día con mayor gasto: {datos.DiaMayor} (${datos.MontoDiaMayor:N2})";
            fila++;
        }

        if (datos.DiaMenor is not null)
        {
            hoja.Cell(fila, 1).Value = $"Día con menor gasto: {datos.DiaMenor} (${datos.MontoDiaMenor:N2})";
        }

        hoja.Columns().AdjustToContents();
        workbook.SaveAs(ruta);

        return ruta;
    }
}