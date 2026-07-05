using System;
using System.Collections.Generic;
using System.Text;
using SQLite;

namespace mnts.Models;

public class Ingreso
{
    [PrimaryKey, AutoIncrement]
    public int Id { get; set; }

    public int Mes { get; set; }
    public int Anio { get; set; }
    public double Monto { get; set; }
}