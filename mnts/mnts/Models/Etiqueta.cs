using System;
using System.Collections.Generic;
using System.Text;
using SQLite;

namespace mnts.Models;

public class Etiqueta
{
    [PrimaryKey]
    public int Id { get; set; }

    public string ClaveInterna { get; set; } = string.Empty;
    public string Nombre { get; set; } = string.Empty;
    public string Icono { get; set; } = "📌";
}