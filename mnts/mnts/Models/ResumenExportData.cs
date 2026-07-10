using System;
using System.Collections.Generic;
using System.Text;

namespace mnts.Models;

public class ResumenExportData
{
    public int Mes { get; set; }
    public int Anio { get; set; }
    public List<ResumenCategoria> Categorias { get; set; } = new();
    public double TotalGastos { get; set; }
    public double TotalIngresos { get; set; }
    public double Diferencia { get; set; }
    public int? DiaMayor { get; set; }
    public double MontoDiaMayor { get; set; }
    public int? DiaMenor { get; set; }
    public double MontoDiaMenor { get; set; }
}