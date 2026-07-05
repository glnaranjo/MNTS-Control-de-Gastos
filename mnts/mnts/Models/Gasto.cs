using System;
using System.Collections.Generic;
using System.Text;
using SQLite;

namespace mnts.Models;

public class Gasto
{
    [PrimaryKey, AutoIncrement]
    public int Id { get; set; }

    public int Dia { get; set; }
    public int Mes { get; set; }
    public int Anio { get; set; }
    public string Categoria { get; set; } = string.Empty;
    public double Monto { get; set; }
}